fh = open('mbox-short.txt')
for x in fh :
    x = x.upper()
    x = x.strip()
    print(x)

    # or use print(x.upper())
