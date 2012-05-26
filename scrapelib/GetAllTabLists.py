#!/usr/bin/env python

def parseArtistList(artistList,outDir):
	"""Opens an artistlist and creates a tablist for each one."""
	import os
	import GetTabListForArtist
	thissection=artistList.readline()
	count=int(artistList.readline()[:-1])

	for i in range(count):
		artistId=artistList.readline()[:-1]
		artistName=artistList.readline()[:-1]
		outFileName=os.path.join(outDir,fileNameFor(artistName))
		if os.path.exists(outFileName):
			print 'Skipping:',outFileName
		else:
			print 'Writing',outFileName
			outFile=open(outFileName,'w')
			try:
				GetTabListForArtist.scrapeTabList(artistId,artistName,outFile)
			except:
				print 'Error handling artist',artistId,artistName
			outFile.close()


def fileNameFor(artistName):
	validCharacters=' ()._-&:,'
	name=''
	for letter in artistName:
		if letter.isalnum() or letter in validCharacters:
			name+=letter
	return name+'.tablist'




if __name__=='__main__':
	import sys
	import os
	import time
	arg=sys.argv[1:]
	if not arg:
		print 'Usage:',sys.argv[0],'artistList1 artistList2 ...'
		sys.exit(-1)
	for artistListName in arg:
		basename=artistListName.split('.')[0]
		outdir='scrape.'+basename
		try:
			artistList=open(artistListName,'r')
			if not os.path.exists(outdir):
				os.mkdir(outdir)
			print artistListName,' >> ',outdir
			parseArtistList(artistList,outdir)
		except IOError:
			print 'Skipping',artistListName+': File not found.'


