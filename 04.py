#!/usr/bin/python3

import sys
import hashlib
import re

key = sys.stdin.readline().rstrip()
index = 1
hash = ''
pattern = re.compile('000000')
while True:
    input = "%s%d" % (key, index)
    hash = hashlib.md5(input.encode('utf-8')).hexdigest()
#    print("Input: %s Hash: %s" % (input, hash))
    if pattern.match(hash) != None:
#        print("Index: %d" % index)
        break
#    elif index > 100:
#        break
    else:
        index += 1
    
print("value: %s hash: %s" % (index, hash))
