import json

f=open(r"C:\Users\AdeYu\Downloads\book.json", "r")
s=f.read()

book = json.loads(s)
print(type(book))
print(book)