#!/usr/bin/env python

def containsNoTabs(file):
	file.readline()
	file.readline()
	numTabs=int(file.readline()[:-1])
	return numTabs==0

def pullHere(path):
	print 'Pulling',path
	import shutil
	shutil.move(path,'.')

if __name__=='__main__':
	"""For each argument file, check if it contains no tabs. If not, drag the file to the cwd."""
	import sys
	arg=sys.argv[1:]
	for a in arg:
		try:
			file=open(a)
			if containsNoTabs(file):
				pullHere(a)
		except IOError:
			print 'File not found.',a

