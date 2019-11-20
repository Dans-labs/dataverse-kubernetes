#!/usr/bin/python
# Script to read custom metadata blocks from remote URL to github folder specified in CUSTOM_METADATA_URL environmental variable
# Returns nothing if there are no files with custom blocks available 

import urllib2
import re
import os

customurl = os.getenv("CUSTOM_METADATA_URL")
directurl = 'https://raw.githubusercontent.com'
directuri = customurl.replace('https://github.com/','')
directuri = directuri.replace('/tree','')

content = urllib2.urlopen(customurl).read()
customenv = ''
for eachline in content.split('\n'):
    tsvmatch = re.search('.+>(.+?\.tsv.*?)<', eachline, re.IGNORECASE)
    if tsvmatch:
        customfile = "%s/%s/%s" % (directurl, directuri, tsvmatch.group(1))
        customenv+=customfile + ' '
print(customenv)
