#!/usr/bin/env python3
"""
Generate complete TL_SCHEMA dictionary from api.tl.
Parses all type definitions and generates field-level serialization rules.
"""
import re, json
from pathlib import Path

def parse_tl(filepath):
    content = Path(filepath).read_text(encoding='utf-8', errors='replace')
    # Remove line comments
    lines = [re.sub(r'//.*', '', l).strip() for l in content.split('\n')]
    text = '\n'.join(l for l in lines if l)
    
    # Split into statements (semicolons at top level)
    stmts = []
    depth, cur = 0, []
    for ch in text:
        if ch == '{': depth += 1
        elif ch == '}': depth -= 1
        if ch == ';' and depth == 0:
            stmts.append(''.join(cur).strip())
            cur = []
        else:
            cur.append(ch)
    if cur: stmts.append(''.join(cur).strip())
    
    functions = {}
    types = {}  # type_name -> { variant_name -> {args} }
    type_order = {}  # type_name -> [variant_names] (preserve order)
    
    for stmt in stmts:
        if not stmt or stmt.startswith('---'):
            continue
        
        # Function definition
        m = re.match(r'(\w+)\.(\w+)#([0-9a-fA-F]+)\s+(.*?)=\s*(\w+)\s*$', stmt)
        if m:
            ns, name, hexval, args_str, ret = m.groups()
            fname = f"{ns}.{name}"
            functions[fname] = {
                'hex': f"0x{hexval}",
                'args': parse_args(args_str),
                'returns': ret
            }
            continue
        
        # Type definition with constructor
        m = re.match(r'(\w+)#([0-9a-fA-F]+)\s+(.*?)=\s*(\w+)\s*$', stmt)
        if m:
            name, hexval, args_str, parent = m.groups()
            args = parse_args(args_str)
            if parent not in types:
                types[parent] = {}
                type_order[parent] = []
            types[parent][name] = {'hex': f"0x{hexval}", 'args': args}
            type_order[parent].append(name)
            continue
        
        # Bare type (no constructor, no args)
        m = re.match(r'(\w+)\s*=\s*(\w+)\s*$', stmt)
        if m:
            name, parent = m.groups()
            if parent not in types:
                types[parent] = {}
                type_order[parent] = []
            types[parent][name] = {'hex': None, 'args': []}
            type_order[parent].append(name)
    
    return functions, types, type_order

def parse_args(args_str):
    args = []
    # Handle parenthesized generic args
    args_str = re.sub(r'<([^>]+)>', '', args_str)
    
    parts = args_str.split()
    for part in parts:
        if not part.strip():
            continue
        # Parse: name:type (possibly conditional)
        m = re.match(r'(\w+):(.+)', part)
        if m:
            name, typ = m.group(1), m.group(2)
            
            if typ == '#':
                args.append({'name': name, 'tl_type': 'flags', 'is_flag': True})
                continue
            
            # Check for conditional: flags.N?type
            cond_m = re.match(r'flags\.(\d+)\?(.+)', typ)
            if cond_m:
                bit = int(cond_m.group(1))
                base_type = cond_m.group(2)
                args.append({
                    'name': name,
                    'tl_type': base_type,
                    'cond': bit,
                    'is_flag': False
                })
                continue
            
            args.append({
                'name': name,
                'tl_type': typ,
                'is_flag': False
            })
    return args

def generate_python_schema(functions, types, type_order):
    """Generate Python code with full TL_SCHEMA."""
    lines = []
    lines.append('"""')
    lines.append('Auto-generated TL schema from Telegram API schema (api.tl).')
    lines.append('DO NOT EDIT — regenerate with tools/generate_code.py')
    lines.append('"""')
    lines.append('')
    
    # Generate TYPES dict with constructors
    lines.append('TYPES = {')
    for parent, variants in sorted(types.items()):
        lines.append(f'    "{parent}": {{')
        for name in type_order.get(parent, []):
            info = variants[name]
            hex_str = info['hex'] if info['hex'] else 'None'
            lines.append(f'        "{name}": {hex_str},')
        lines.append('    },')
    lines.append('}')
    lines.append('')
    
    # Generate FUNCTIONS dict
    lines.append('FUNCTIONS = {')
    for fname, info in sorted(functions.items()):
        lines.append(f'    "{fname}": {info["hex"]},  # → {info["returns"]}')
    lines.append('}')
    lines.append('')
    
    # Generate TL_SCHEMA dict with full field definitions
    lines.append('TL_SCHEMA = {')
    
    # Add all type variants with args
    for parent, variants in sorted(types.items()):
        for name in type_order.get(parent, []):
            info = variants[name]
            if not info['args']:
                continue
            lines.append(f'    "{name}": [')
            for arg in info['args']:
                extra = ''
                if arg.get('cond') is not None:
                    extra = f', "cond": {arg["cond"]}'
                if arg.get('is_flag'):
                    extra += ', "is_flag": True'
                lines.append(f'        {{"name": "{arg["name"]}", "tl_type": "{arg["tl_type"]}"{extra}}},')
            lines.append('    ],')
    
    # Also add functions as if they were types (for the serialization of args)
    # This allows call() to know the field order
    for fname, info in sorted(functions.items()):
        if not info['args']:
            continue
        lines.append(f'    "{fname}": [')
        for arg in info['args']:
            extra = ''
            if arg.get('cond') is not None:
                extra = f', "cond": {arg["cond"]}'
            if arg.get('is_flag'):
                extra += ', "is_flag": True'
            lines.append(f'        {{"name": "{arg["name"]}", "tl_type": "{arg["tl_type"]}"{extra}}},')
        lines.append('    ],')
    
    lines.append('}')
    lines.append('')
    
    # Also generate InputPeer constructors for convenience
    lines.append('''
# === Common InputPeer constructors ===
INPUT_PEER_SELF = 0x7da07ec9
INPUT_PEER_USER = 0x7b8e7de6
INPUT_PEER_CHAT = 0x179be863
INPUT_PEER_CHANNEL = 0x20adaef8
''')
    
    return '\n'.join(lines)

if __name__ == '__main__':
    api_tl = Path("E:/code/tdesktop-fork/Telegram/SourceFiles/mtproto/scheme/api.tl")
    functions, types, type_order = parse_tl(api_tl)
    
    print(f"Parsed: {len(functions)} functions, {sum(len(v) for v in types.values())} type variants")
    
    code = generate_python_schema(functions, types, type_order)
    output = Path("E:/tdesktop-mtproto/python/tl_schema.py")
    output.write_text(code)
    print(f"Generated: {output} ({len(code.splitlines())} lines)")
    print(f"  Types with args: {sum(1 for v in types.values() for n in v if v[n]['args'])}")
    print(f"  Functions with args: {sum(1 for f in functions.values() if f['args'])}")
