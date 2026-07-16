#!/usr/bin/env python3
"""
TL Schema → C++ serializer generator.
Parses api.tl from tdesktop and generates C++ serialization functions.
"""
import re, json, sys
from pathlib import Path

# === PARSE TL SCHEMA ===
def parse_tl(filepath):
    content = Path(filepath).read_text(encoding='utf-8', errors='replace')
    # Remove comments and multi-line
    lines = []
    for line in content.split('\n'):
        line = re.sub(r'//.*', '', line).strip()
        if not line: continue
        lines.append(line)
    
    text = ' '.join(lines)
    
    # Split by semicolons (statement boundaries)
    statements = []
    depth = 0
    current = []
    for ch in text:
        if ch == '{': depth += 1
        elif ch == '}': depth -= 1
        if ch == ';' and depth == 0:
            statements.append(''.join(current).strip())
            current = []
        else:
            current.append(ch)
    if current:
        statements.append(''.join(current).strip())
    
    # Parse each statement
    functions = []
    types = {}
    
    for stmt in statements:
        if not stmt or stmt.startswith('---'):
            continue
        
        # Check if it's a function definition: ns.funcName#hex args = ReturnType;
        m = re.match(r'(\w+)\.(\w+)#([0-9a-fA-F]+)\s+(.*?)=\s*(\w+)\s*$', stmt)
        if m:
            ns, name, hexval, args_str, ret = m.groups()
            args = parse_args(args_str) if args_str else []
            functions.append({
                'ns': ns, 'name': name, 'hex': hexval, 
                'args': args, 'returns': ret
            })
            continue
        
        # Type definition: typeName#hex args = TypeConstructor;
        m = re.match(r'(\w+)#([0-9a-fA-F]+)\s+(.*?)=\s*(\w+)\s*$', stmt)
        if m:
            name, hexval, args_str, type_cons = m.groups()
            args = parse_args(args_str) if args_str else []
            if type_cons not in types:
                types[type_cons] = []
            types[type_cons].append({
                'name': name, 'hex': hexval, 'args': args
            })
            continue
        
        # Bare type: typeName args = TypeConstructor;
        m = re.match(r'(\w+)\s*=\s*(\w+)\s*$', stmt)
        if m:
            name, type_cons = m.groups()
            if type_cons not in types:
                types[type_cons] = []
            types[type_cons].append({
                'name': name, 'hex': None, 'args': []
            })
    
    return functions, types

def parse_args(args_str):
    args = []
    # Handle flags:# pattern
    for part in args_str.split():
        # Parse: name:type
        m = re.match(r'(\w+):(.+)', part)
        if m:
            name, typ = m.groups()
            if typ == '#':  # flags field
                args.append({'name': name, 'type': 'flags', 'is_flag': True})
                continue
            # Check for conditional: flags.N?type
            cond = None
            true_val = None
            cm = re.match(r'flags\.(\d+)\?(.+):(.+)', name + ':' + typ)
            if cm:
                # This is more complex parsing needed
                pass
            
            base_type = typ.split('.')[0] if '.' in typ else typ
            args.append({'name': name, 'type': base_type, 'full_type': typ, 'is_flag': False})
    return args

# === GENERATE C++ CODE ===
def generate_serializers(functions, types):
    lines = []
    lines.append('#include "desktop_mtproto/client.h"')
    lines.append('#include <nlohmann/json.hpp>')
    lines.append('using json = nlohmann::json;')
    lines.append('')
    lines.append('namespace desktop_mtproto::generated {')
    lines.append('')
    
    # Generate type serializers
    for type_name, variants in sorted(types.items()):
        if len(variants) > 20:  # Skip huge generic types
            continue
        lines.append(f'// {type_name} — {len(variants)} variant(s)')
        for v in variants:
            if v['hex'] and not v['args']:
                lines.append(f'constexpr uint32_t k{v["name"]} = 0x{v["hex"]};')
        lines.append('')
    
    # Generate function serializers
    lines.append('// === FUNCTION SERIALIZERS ===')
    lines.append('')
    
    for f in functions:
        fn_name = f"{f['ns']}_{f['name']}"
        lines.append(f'// {f["ns"]}.{f["name"]}#{f["hex"]} → {f["returns"]}')
        lines.append(f'std::vector<uint8_t> serialize_{fn_name}(const json& params) {{')
        lines.append(f'    TLS t;')
        lines.append(f'    t.write_uint32(0x{f["hex"]});')
        
        # Generate parameter serialization
        for arg in f['args']:
            if arg['is_flag']:
                lines.append(f'    // flags field')
                lines.append(f'    uint32_t flags = 0;')
                # Calculate flags from conditional fields
                lines.append(f'    t.write_uint32(flags);')
                continue
            
            type_map = {
                'int': 'int32',
                'long': 'int64', 
                'double': 'double',
                'string': 'string',
                'bytes': 'bytes',
                'Bool': 'bool',
                'int128': 'int128',
                'int256': 'int256',
            }
            tl_type = type_map.get(arg['type'])
            
            if tl_type:
                lines.append(f'    t.write_{tl_type}(params["{arg["name"]}"]);')
            elif arg['type'] == 'Vector':
                lines.append(f'    // Vector<{arg["full_type"]}> — TODO')
            else:
                # Complex type - serialize as object
                lines.append(f'    serialize_type_{arg["type"]}(t, params["{arg["name"]}"]);')
        
        lines.append(f'    return t.buf_;')
        lines.append(f'}}')
        lines.append('')
    
    # Generate generic dispatcher
    lines.append('// === DISPATCHER ===')
    lines.append('std::vector<uint8_t> serialize_method(const std::string& method, const json& params) {')
    lines.append('    static const std::map<std::string, std::function<std::vector<uint8_t>(const json&)>> dispatch = {')
    for f in functions[:50]:  # Top 50 for now
        fn_name = f"{f['ns']}_{f['name']}"
        lines.append(f'        {{"{f["ns"]}.{f["name"]}", serialize_{fn_name}}},')
    lines.append('    };')
    lines.append('    auto it = dispatch.find(method);')
    lines.append('    if (it != dispatch.end()) return it->second(params);')
    lines.append('    throw std::runtime_error("Unknown method: " + method);')
    lines.append('}')
    lines.append('')
    lines.append('} // namespace desktop_mtproto::generated')
    
    return '\n'.join(lines)

if __name__ == '__main__':
    fork = Path("E:/code/tdesktop-fork")
    api_tl = fork / "Telegram/SourceFiles/mtproto/scheme/api.tl"
    mtproto_tl = fork / "Telegram/SourceFiles/mtproto/scheme/mtproto.tl"
    
    functions, types = parse_tl(api_tl)
    print(f"Parsed {len(functions)} functions, {sum(len(v) for v in types.values())} type variants")
    
    code = generate_serializers(functions, types)
    output = Path("E:/tdesktop-mtproto/src/generated/telegram_api.cpp")
    output.parent.mkdir(exist_ok=True)
    output.write_text(code)
    print(f"Generated: {output} ({len(code.splitlines())} lines)")
    
    # Print key methods found
    key_methods = ['auth.sendCode', 'auth.signIn', 'messages.sendMessage', 
                   'messages.getDialogs', 'help.getConfig', 'contacts.resolveUsername']
    print("\nKey methods:")
    for f in functions:
        fn = f"{f['ns']}.{f['name']}"
        if fn in key_methods:
            print(f"  {fn}#{f['hex']} → {f['returns']}")
