import json 

input = '''[
    { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
    },
    { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
    }
]'''

info = json.loads(input) #because of the square brackets, we treat it like a list in py. But that list contains two dictionaries '{}'
print(info)
print('User count:', len(info))
for item in info:
    print('Name', item['name'])
    print('ID', item['id'])
    print('Attribute', item['x'])