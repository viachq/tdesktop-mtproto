cmake_minimum_required(VERSION 3.20)
project(desktop-mtproto VERSION 0.1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# OpenSSL
set(OPENSSL_ROOT_DIR "C:/TBuild/Libraries/win64/openssl3")
set(OPENSSL_INCLUDE_DIR "C:/TBuild/Libraries/win64/openssl3/include")
set(OPENSSL_CRYPTO_LIBRARY "C:/TBuild/Libraries/win64/openssl3/out/libcrypto.lib")

# Library
add_library(desktop_mtproto SHARED src/core/core.cpp)
target_include_directories(desktop_mtproto PUBLIC include ${OPENSSL_INCLUDE_DIR})
target_link_libraries(desktop_mtproto ${OPENSSL_CRYPTO_LIBRARY} ws2_32 crypt32)
target_compile_definitions(desktop_mtproto PRIVATE _CRT_SECURE_NO_WARNINGS WIN32_LEAN_AND_MEAN)
