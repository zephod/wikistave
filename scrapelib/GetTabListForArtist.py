#!/usr/bin/env python

#Dump a list of all tabs

#RE_URL='test_artist=%d&start=%d.html'

def scrapeTabList(artistId,artistName,out):
	"""Dump a list of all tabs for this artist"""
	RE_URL='http://mysongbook.com/tab-tab_list-id_artist=%d&start=%d.htm'
	RE_NUM_TABS=r'- (\d+) tab'

	import urllib
	import re
	url=RE_URL % (int(artistId), 0)
	firstpage=urllib.urlopen(url)
	firstpagetext=firstpage.read()
	numtabs=int(re.search(RE_NUM_TABS,firstpagetext).group(1))

	#Read each page in turn, scraping tab names into our list
	allTuples=extractTuples(firstpagetext)
 	for offset in range(10,numtabs,10):
		url2=RE_URL % (int(artistId),offset)
		page=urllib.urlopen(url2)
		pagetext=page.read()
		allTuples+=extractTuples(pagetext)

	print >>out,artistId
	print >>out,artistName
	print >>out,len(allTuples)
	for tuple in allTuples:
		print >>out,tuple[0]
		print >>out,tuple[1]


def extractTuples(pagetext):
	RE_TAB_ENTRY=r'<span class="titBLEU1">([^<]+)</span>&nbsp[^\[]+\[(\w+)\]'

	import re
	return re.findall(RE_TAB_ENTRY,pagetext,flags=re.MULTILINE)


if __name__=="__main__":
	import sys
	arg=sys.argv[1:]
	if not arg or not len(arg)==2:
		print 'Usage:',sys.argv[0],'artistId artistName'
		sys.exit(-1)
	artistId=arg[0]
	artistName=arg[1]
	scrapeTabList(artistId,artistName,sys.stdout)

