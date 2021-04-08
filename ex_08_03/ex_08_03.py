han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
#    print('Line:',line)
#    if line == '' :
#        print('Skip blank')
#        continue
    words = line.split()
#    print('Words',words)
    #Guardian Pattern
#    if len(words) < 3 :
#        continue
# the above gp was combined to the below statement
    if len(words) < 3 or words[0] != 'From' :
#        print('ignore')
        continue
    print(words[2])