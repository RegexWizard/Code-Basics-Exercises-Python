import json

book = {}
book["tom"] = {
    "name": "tom",
    "address": "1 red street, NY",
    "phone": 98989898
}
book["bob"] = {
    "name": "bob",
    "address": "1 green street, NY",
    "phone": 234234234
}

s = json.dumps(book)
with open(r"C:\Users\AdeYu\Downloads\book.json", "w") as f:
    f.write(s)
print(s)
