#!/usr/bin/env python

URL_SERVER='www.mysongbook.com'
URL_FORMAT='/files/-/-%d/%s.%s'
URL_FORMAT2='/files/%s/%s/%s'


def downloadFile(artistId,artist,title,fileFormat,outputFileName):
	url=findUrlForTab(artistId,artist,title,fileFormat)
	if not url:
		return False
	import urllib2
	inputFile=urllib2.urlopen('http://'+URL_SERVER+url)
	outputFile=open(outputFileName,'wb')
	outputFile.write(inputFile.read())
	outputFile.close()
	print 'Written:',outputFileName
	return True

def findUrlForTab(artistId,artist,title,fileFormat):
	import httplib
	for url in allUrls(artistId,artist,title,fileFormat):
		conn=httplib.HTTPConnection(URL_SERVER)
		conn.request("HEAD",url)
		print "Contacting:",URL_SERVER+url
		response=conn.getresponse()
		code=response.status
		if code==200:
			print "["+str(code)+"]"
			return url
	return None

def allUrls(artistId,artist,title,fileFormat):
	artistId=int(artistId)
	fileFormat=fileFormat.lower()
	out=[]
	#Most likely option
	if '\'' in (artist+title):
		artist=artist.replace('\'',' ')
		title=title.replace('\'',' ')
	#out.append(u(artistId,artist+' - '+title,fileFormat))
	out.append(u2(artist,artist+' - '+title,fileFormat))
	#if ',' in artist:
	#	split=artist.replace(' ','').split(',')
	#	out.append(u(artistId,split[1]+' '+split[0]+' - '+title,fileFormat))
	#	a2=artist.replace(',',' ')
	#	t2=title.replace(',',' ')
	#	out.append(u(artistId,a2+' - '+t2,fileFormat))
	#out.append(u(artistId,artist+' - '+title.lower(),fileFormat))
	#out.append(u(artistId,artist.lower()+' - '+title,fileFormat))
	#out.append(u(artistId,artist.lower()+' - '+title.lower(),fileFormat))


	#out.append(u(artistId,artist+' - '+title,fileFormat.upper()))
	#if ',' in artist:
	#	names=artist.replace(' ','').split(',')
	#	name=names[1]+' '+names[0]
	#	out.append(u(artistId,name+' - '+title,fileFormat))

	
	#for name in allPossibleNames(artist,title):
	#	name=name.replace(' ','%20')
	#	url=URL_FORMAT % (int(artistId),name,fileFormat)
	#	out.append(url)
	return out

def u(artistId,filename,fileformat):
	url=URL_FORMAT % (artistId,filename,fileformat)
	import urllib
	return urllib.quote(url)

def u2(artistName,filename,fileformat):
	artistName=artistName.replace(' ','').lower()
	username=""
	for letter in artistName:
		if letter.isalpha(): username+=letter.lower()
	if len(username)>7: username=username[:7]
	url=URL_FORMAT2 % (username[0],username,filename+'.'+fileformat)
	import urllib
	return urllib.quote(url)

def allPossibleNames(artist,title):
	allTitles=recurPossibleNames([],"",title.split())
	allArtists=recurPossibleNames([],"",artist.split())

	joins=[" - ","-","- "," -"]
	out=[]
	for join in joins:
		for artist in allArtists:
			for title in allTitles:
				out.append(artist+join+title)
	return out

def recurPossibleNames(output, constructing, remaining):
	if len(remaining)==0:
		output.append(constructing)
	else:
		first=remaining[0]
		camel=camelCase(first)
		lower=first.lower()
		remaining=remaining[1:]
		# Try out the possible constructions in the optimal order
		if not len(constructing)==0:
			recurPossibleNames(output, constructing+' '+first, remaining)
			if not first==lower: recurPossibleNames(output, constructing+' '+lower, remaining)
			if not first==camel: recurPossibleNames(output, constructing+' '+camel, remaining)
		if not first==camel: recurPossibleNames(output, constructing+camel, remaining)
		recurPossibleNames(output, constructing+first, remaining)
		if not first==lower: recurPossibleNames(output, constructing+lower, remaining)
	return output
	
def camelCase(string):
	return string[0].upper()+string[1:].lower()

if __name__=="__main__":
	import sys
	arg=sys.argv[1:]
	if not arg or not len(arg)==4:
		print "Usage",sys.argv[0],"artistId 'artist name' 'song name' (gp2|gp3|...)"
		sys.exit(-1)
	
	artistId=arg[0]
	artist=arg[1]
	title=arg[2]
	fileFormat=arg[3]
#	Should work:
#	artistId=7155
#	artist='A'
#	title='Fog Horn'
#	fileFormat='gp4'
	outputFileName=artist+" - "+title+'.'+fileFormat

	downloadFile(artistId,artist,title,fileFormat,outputFileName)
