import pyshorteners

url = input('Enter Your URL : ')
print('URL Shortening : ', pyshorteners.Shortener().tinyurl.short(url))