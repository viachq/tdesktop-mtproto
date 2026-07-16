@echo off
set OPENSSL_ROOT_DIR=C:\TBuild\Libraries\win64\openssl3
set OPENSSL_USE_STATIC_LIBS=ON
call "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat" 2>nul || call "C:\Program Files\Microsoft Visual Studio\18\BuildTools\VC\Auxiliary\Build\vcvars64.bat"
cd /d E:\tdesktop-mtproto
cmake -B build -D CMAKE_BUILD_TYPE=Release
