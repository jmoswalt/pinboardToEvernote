#!/usr/bin/python
import urllib2
import datetime
from xml.dom.minidom import *


def getRecentBookmarks(auth_token):
	"""
	Takes the Pinboard API Token (which is of the form username:HEXADECIMALSTRING)
	Returns a list of (href, title, extended) tuples for recent bookmarks.
	"""
	checkToken(auth_token)
	url = "https://api.pinboard.in/v1/posts/recent?auth_token=%s" % (auth_token)
	return getList(url)


def getAllBookmarks(auth_token):
	"""
	Takes the Pinboard API Token (which is of the form username:HEXADECIMALSTRING)
	Returns a list of (href, title, extended) tuples for all bookmarks.
	"""
	checkToken(auth_token)
	url = "https://api.pinboard.in/v1/posts/all?auth_token=%s" % (auth_token)
	return getList(url)


def getTodaysBookmarks(auth_token):
	"""
	Takes the Pinboard API Token (which is of the form username:HEXADECIMALSTRING)
	Returns a list of (href, title, extended) tuples for all bookmarks created today.
	"""
	checkToken(auth_token)
	url = "https://api.pinboard.in/v1/posts/get?auth_token=%s&dt=%s" % (auth_token, str(datetime.datetime.utcnow().date()))
	return getList(url)


def getBookmarksFromDate(auth_token, fromdt):
	"""
	Takes the Pinboard API Token (which is of the form username:HEXADECIMALSTRING) and a datetime.date() object.
	Returns a list of (href, title, extended) tuples for all bookmarks created after fromdt.
	"""
	checkToken(auth_token)
	url = "https://api.pinboard.in/v1/posts/all?auth_token=%s&fromdt=%s" % (auth_token, str(fromdt))
	return getList(url)


def checkToken(auth_token):
	if not auth_token:
		print "Please fill in your pinboard api token"
		print "You can find your token on your https://pinboard.in/settings/password page"
		exit(1)


def getList(url):
	rawXML = urllib2.urlopen(url)
	parsedXML = xml.dom.minidom.parse(rawXML)
	bookmarkList = []
	for post in parsedXML.getElementsByTagName("post"):
		href = post.getAttribute("href").strip()
		title = post.getAttribute("description").strip()
		extended = post.getAttribute("extended").strip()
		bookmark = (href, title, extended)
		bookmarkList.append(bookmark)
	return bookmarkList
