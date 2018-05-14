#!/usr/bin/env python
##
# Copyright (c) 2018 P.N. Giubelli <paoloniccolo.giubelli@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
##

import string
import sys

lower=string.ascii_lowercase
upper=string.ascii_uppercase

lower_13=lower[13:]+lower[:13]
upper_13=upper[13:]+upper[:13]

def rot13(str):
	ret = ''
	for code in str:
		if lower.find(code) != -1:
			ret = ret+lower_13[lower.index(code)]
		elif upper.find(code) != -1:
			ret = ret+upper_13[upper.index(code)]
		else:
			ret = ret+code
	return ret

if len(sys.argv) > 1:
	inf=open(sys.argv[1], 'r')
else:
	inf=sys.stdin

for line in inf:
	sys.stdout.write(rot13(line))
sys.stdout.flush()
