#!/usr/bin/env python

import urllib
import sys

try:
    data = urllib.urlopen('http://localhost:9002/health').read()
except:
    sys.exit(-1)
else:
    if "UNKNOWN" in data:
        sys.exit(-1)
    else:
        sys.exit(0)