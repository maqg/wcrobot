#!usr/bin/python

from os import popen
import signal
import sys


def octUnicode(src):
	if (type(src) == str):
		return src
	else:
		try:
			return str(src, "utf-8")
		except:
			return src

def toString(src, encoding="utf-8"):
	if (type(src) == str):
		try:
			return (src.encode(encoding)).decode('utf-8')
		except:
			return (octUnicode(src).encode(encoding)).decode('utf-8')
	else:
		return src
	
def get_tuple(msg):

	if (type(msg) == int):
		return (msg)

	if (not msg):
		return ()

	if (type(msg) == tuple):
		tempList = []
		for item in msg:
			if (type(item) == int):
				tempList.append(item)
			else:
				tempList.append(toString(item))
		return tuple(tempList)
	else:
		return (toString(msg))
	
def TSHPrint(formatStr, args = {}):
	print((formatStr % get_tuple(args)))

if __name__ == '__main__':
	TSHPrint("%d", 0);
