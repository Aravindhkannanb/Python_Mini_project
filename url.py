import pyshorteners
url=input("Enter the url address:")
print("Url after shortening",pyshorteners.Shortener().tinyurl.short(url))