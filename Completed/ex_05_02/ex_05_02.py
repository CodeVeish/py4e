largest = None
smallest = None
while True :
    feed = input('Enter a number: ')
    if feed == 'done' : 
        break
    try :
        float_feed = float(feed)
    except : 
        print('Invalid Input')
        continue
    if largest is None :
        largest = float_feed
    if smallest is None : 
        smallest = float_feed
    if float_feed > largest :
        largest = float_feed
        # print(largest)
    if float_feed < smallest :
        smallest = float_feed
        # print(smallest)
print('Maximimum is', largest)
print('Minimum is', smallest)