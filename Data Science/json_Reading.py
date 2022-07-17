with open("Data Science\\book.txt","r") as f:
    s=f.read()
    print(type(s))

import json
from pydoc import doc
book=json.loads(s)

print(type(book))

print(book["tom"])
print(book["bob"]["Phone"])


for key, value in book.items():
    print(key, " : ", value)

