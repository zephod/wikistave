#!/usr/bin/env python

MODE_MISSING='-missing'
MODE_FOUND='-found'
MODE_DL='-dl'
MODE_DRY='-dry'
MODES=[MODE_MISSING,MODE_FOUND,MODE_DRY,MODE_DL]

def parseTabFile(tabFile,outDir,mode):
	"""Opens a list of artists and creates a tab list for each one."""
	import os
	import Download
	artistId=tabFile.readline()[:-1]
	artistName=tabFile.readline()[:-1]
	count=int(tabFile.readline()[:-1])

	for i in range(count):
		title=tabFile.readline()[:-1]
		fileFormat=tabFile.readline()[:-1]
		outFileName=os.path.join(outDir,fileNameFor(title,fileFormat))
		if os.path.exists(outFileName):
			if mode==MODE_FOUND:
				print outFileName
		else:
			if mode==MODE_MISSING:
				print outFileName
			if mode==MODE_DRY:
				print outFileName
				for url in Download.allUrls(artistId,artistName,title,fileFormat):
					print url
			if mode==MODE_DL:
				Download.downloadFile(artistId,artistName,title,fileFormat,outFileName)


		#success=Download.downloadFile(artistId,artistName,title,fileFormat,outFileName)


def fileNameFor(title,fileFormat):
	validCharacters=' ()._-&:,'
	name=''
	for letter in title:
		if letter.isalnum() or not validCharacters.find(letter)==-1:
			name+=letter
	return name+'.'+fileFormat

def die():
	import sys
	print 'Usage:',sys.argv[0],'('+'|'.join(MODES)+') tabList1 tabList2 ...'
	sys.exit(-1)

if __name__=='__main__':
	import sys
	import os
	import time
	arg=sys.argv[1:]
	if not arg: die()
	mode=arg[0]
	arg=arg[1:]
	if not arg or not mode in MODES: die()
	for tabFileName in arg:
		tabFile=open(tabFileName,'r')
		basename='scrape.'+os.path.basename(tabFile.name).replace('.tablist','')
		dirname=os.path.dirname(tabFile.name)
		outdir=os.path.join(dirname,basename)
		if not os.path.exists(outdir):
			os.mkdir(outdir)
		parseTabFile(tabFile,outdir,mode)
		tabFile.close()

