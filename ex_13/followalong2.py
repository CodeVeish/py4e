import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2" hottie = "Kevin">
            <id>001</id>
            <name nickname = "bra">Chuck</name>
        </user>
        <user x="7" hottie = "Nati">
            <id>009</id>
            <name nickname = "dude">Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('ID', item.find('id').text)
    print('Name', item.find('name').text)
    print('Attribute', item.get('x'))
    print('Attribute', item.get('hottie'))


