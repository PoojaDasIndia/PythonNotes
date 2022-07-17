# To create address book and write some records into it

book={}  # empty dictionary

book['tom']={
    "Name": "Tom",
    "Address":"1 red Road",
    "Phone":78514565
}

book["bob"]={
    "Name":"Bob",
    "Address":"2 Green Road",
    "Phone":758815752

}

import json

s=json.dumps(book)  # dump as string

with open ("Data Science//book.txt","w") as f:
    f.write(s)


