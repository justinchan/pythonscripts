import urllib2
from xml.dom import minidom
import re

def main():
	response = urllib2.urlopen("http://partner.mlb.com/partnerxml/gen/news/rss/oak.xml")
	xml = response.read()
	xmldoc = minidom.parseString(xml)
	descList = xmldoc.getElementsByTagName("description")
	win_pattern = re.compile('(.)*\d-\d.{0,30}(victory|win)(.)*')
	lose_pattern = re.compile('(.)*\d-\d.{0,30}loss(.)*')
	for desc in descList:
		headline = desc.childNodes[0].nodeValue
		winquiry = win_pattern.match(headline)
		losequiry = lose_pattern.match(headline)
		if winquiry:
			print winquiry.group()
			print "Win!"
			break
		elif losequiry:
			print losequiry.group(0)
			print "Lose!"
			break

if __name__ == "__main__":
	main()