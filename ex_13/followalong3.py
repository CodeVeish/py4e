import json
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
} '''

info = json.loads(data) #because of the curley brace, data is a dictionary and we can use normal python syntax
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
print('phone:', info["phone"]["number"])