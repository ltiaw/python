# -*- coding: utf-8 -*-

import os
import re
import sys

ssl_path = os.path.join([i for i in sys.path if i[-13:]=="site-packages"][0], "urllib3/util/ssl_.py")

if sys.version[0] == "2":
    print("it's run in python3")
    exit()
if not os.path.exists(ssl_path):
    print("please pip install urllib3 and run again")
    exit()

with open(ssl_path, "r") as f:
    text = f.read()

ciphers = re.findall('DEFAULT_CIPHERS.*?\)', text, re.S)
if ciphers:
    new_text = text.replace(ciphers[0], 'DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMPLEMENTOFDEFAULT"')
    with open(ssl_path, "w") as f:
        f.write(new_text)
else:
    print("Repair failed")
