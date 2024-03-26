#!/bin/python3


#modules are existing in python builtin but importing are the modules not built in but available to us, ike sys

#sys is system functions and parameter
#Example: print(sys.version)

#Example 1
import sys

print(sys.version)

#Example 2
from datetime import datetime
print(datetime.now())

#Example 3
from datetime import datetime as dt #import with alias
print(dt.now())