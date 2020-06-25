# Library for JSON
import json
data = '''{
    "name" : "Adrian",
    "phone" : {
        "type" : "intl",
        "number" : "+48 000 000 000"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:' ,info["email"]["hide"])