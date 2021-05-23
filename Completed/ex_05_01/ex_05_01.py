total = 0
count = 0
while True : 
    num_feed = input('Enter a number:')
    if num_feed == 'done' :
        break
    try :
        float_num_feed = float(num_feed)
    except :
        print('try again')
        continue
    # print(float_num_feed)
    total = total + float_num_feed
    count = count + 1
    average = total / count

# print ('all done')
print (total, count, average)   