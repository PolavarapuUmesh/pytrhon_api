import pyshorteners
s = pyshorteners.Shortener()
print(s.tinyurl.short("http://www.vedantu.com"))
print(s.tinyurl.short("learning.vedantu.com"))