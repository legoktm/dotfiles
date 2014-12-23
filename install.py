#!/usr/bin/env python3
from __future__ import print_function

import hashlib
import os
import shutil
import subprocess

mapping = {
    'gitconfig': '~/.gitconfig',
    'gitignore_global': '~/.gitignore_global',
    'bash_profile': '~/.bash_profile'
}


def get_hash(path):
    with open(path, 'rb') as f:
        h = hashlib.sha256(f.read()).hexdigest()
    return h


def ask(question):
    i = input(question + ' [y/N] ').strip().lower()
    return i == 'y'


def process_file(name, dest):
    dest = os.path.expanduser(dest)
    if get_hash(name) != get_hash(dest):
        print(dest)
        subprocess.call(['diff', dest, name, '-N'])
        if not ask('Do you want to overwrite the modified file?'):
            return
        print('Updating %s' % dest)
        shutil.copy(name, dest)

if __name__ == '__main__':
    for key, val in mapping.items():
        process_file(key, val)
