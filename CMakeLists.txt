cmake_minimum_required(VERSION 3.20)
project(tdesktop-mtproto VERSION 0.1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Manually set OpenSSL paths (built by tdesktop prepare script)
set(OPENSSL_INCLUDE_DIR "C:/TBuild/Libraries/win64/openssl3/include")
set(OPENSSL_CRYPTO_LIBRARY "C:/TBuild/Libraries/win64/openssl3/out/libcrypto.lib")
set(OPENSSL_SSL_LIBRARY "C:/TBuild/Libraries/win64/openssl3/out/libssl.lib")

# Core library
add_library(tdesktop_mtproto STATIC
    src/crypto/aes_ige.cpp
    src/crypto/sha.cpp
    src/tl/serializer.cpp
    src/mtproto/transport.cpp
    src/mtproto/msg_id.cpp
)

target_include_directories(tdesktop_mtproto PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
    ${OPENSSL_INCLUDE_DIR}
)

target_link_libraries(tdesktop_mtproto PUBLIC
    ${OPENSSL_CRYPTO_LIBRARY}
    ${OPENSSL_SSL_LIBRARY}
    crypt32
    ws2_32
)

# Test
add_executable(test_mtproto tests/test_main.cpp)
target_link_libraries(test_mtproto PRIVATE tdesktop_mtproto)
