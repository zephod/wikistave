#!/usr/bin/env python
	
def scrapeArtistList(section,out):
	"""Pull down a list of every artist (plus their ID number) for this section."""
	RE_URL='http://www.mysongbook.com/tab-artist_list&%s&start=%d.htm'
	RE_NUM_ARTISTS=r'- (\d+) artists'
	import urllib
	import re
	#Scrape the first page and count the number of artists
	url=RE_URL % (section, 0)

	firstpage=urllib.urlopen(url)
	firstpagetext=firstpage.read()
	numartists=int(re.search(RE_NUM_ARTISTS,firstpagetext).group(1))

	print >>out,section
	print >>out,numartists

	#Scrape each page in turn, building a list of tuples
	for tuple in extractTuples(firstpagetext):
		print >>out,tuple[0]
		print >>out,tuple[1]
 	for offset in range(50,numartists,50):
		url2=RE_URL % (section,offset)
		page=urllib.urlopen(url2)
		pagetext=page.read()
		for tuple in extractTuples(pagetext):
			print >>out,tuple[0]
			print >>out,tuple[1]


def extractTuples(pagetext):
	RE_ARTIST_NAME=r'href=".*/tab-tab_list-id_artist=(\d+).htm"[^>]+>([^<]+)<'
	import re
	return re.findall(RE_ARTIST_NAME,pagetext)

if __name__=="__main__":
	import sys
	arg=sys.argv[1:]
	if not arg or not len(arg)==1:
		print 'Usage:',sys.argv[0],'[letter=A|letter=B|id_style=37...]'
		sys.exit(-1)
	section=arg[0]
	scrapeArtistList(section,sys.stdout)

