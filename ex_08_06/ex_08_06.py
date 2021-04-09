numlist = list()

while True :
    numlist_input = input('Enter a number: ')
    if numlist_input == 'done' :
        break 
    value = float(numlist_input)
    numlist.append(value)

print(max(numlist))
print(min(numlist))