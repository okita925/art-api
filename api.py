import requests
from bs4 import BeautifulSoup
import json

#URLを変数に置き換えるべき？無駄？
url = "https://collectionapi.metmuseum.org/public/collection/v1/search"

keyword = input("キーワードを入力してください：")

parameter = {"q":keyword}

#第２引数はparams = parameterのほうがいい？
r = requests.get(url, parameter)


jsonText = json.loads(r.text)
opuses = jsonText["objectIDs"]
if opuses:
    for opus in opuses:
        r2 = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{opus}")
        jsonText2 = json.loads(r2.text)
        if jsonText2["isPublicDomain"]:    
            #まとめられる？
            print(jsonText2["title"])
            print(jsonText2["artistDisplayName"])
            print(jsonText2["primaryImage"])
            print(jsonText2["objectDate"])
            print(jsonText2["country"])
        #必要？    
        else:
            print("一致する情報がありませんでした")
else:
    print("一致する情報がありませんでした")