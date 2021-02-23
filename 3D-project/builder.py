#!/usr/bin/python3

from os import path

import subprocess

subprocess.run('bash', input=bytes(f'''
cd '{path.abspath('')}'
cd .c_lib
make
mv lib/test_3d.cpython-38-x86_64-linux-gnu.so ../c_lib/''', encoding='utf-8'))

import sys

try:
    sys.path.append('./c_lib')
    import test_3d
    print('Ok')
except Exception as err:
    print('error:', err, sep='\n')

print('exit')
