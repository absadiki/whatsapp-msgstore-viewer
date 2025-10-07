#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Decryption module

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

import subprocess
import os

def decrypt_db(keyfile: str, encrypted: str, decrypted: str):
    key = keyfile
    if keyfile.lower().endswith('.txt') and os.path.isfile(keyfile):
        # Use key content if keyfile is a .txt file
        with open(keyfile) as f:
            key = f.read().strip()
    subprocess.run([
        "wadecrypt",
        "--verbose",
        key,
        encrypted,
        decrypted
    ], check=True)

if __name__ == '__main__':
    pass
