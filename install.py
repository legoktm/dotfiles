#!/usr/bin/env python3
from __future__ import print_function

from collections import OrderedDict
import hashlib
import os
import platform
import shutil
import subprocess
import sys

if sys.version[0] == '2':
    input = raw_input

mapping = OrderedDict([
    ('gitconfig', '~/.gitconfig'),
    ('gitignore_global', '~/.gitignore_global'),
    ('bash_profile', '~/.bash_profile'),
    ('{os}/bash_profile', '~/.bash_profile_os'),
])


def format_vars():
    vars = {
        'host': platform.node(),
        'system': platform.system()
    }
    if vars['system'] == 'Darwin':
        vars['os'] = 'osx'
    elif vars['system'] == 'Linux':
        vars['os'] = platform.dist()[0]

    return vars


def get_hash(path):
    with open(path, 'rb') as f:
        h = hashlib.sha256(f.read()).hexdigest()
    return h


def ask(question):
    i = input(question + ' [y/N] ').strip().lower()
    return i == 'y'


def process_file(name, dest):
    name = name.format(**format_vars())
    if not os.path.exists(name):
        print('%s does not exist, skipping' % name)
        return
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
