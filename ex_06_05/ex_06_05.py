#this is the work I did myself
text = "X-DSPAM-Confidence:    0.8475"
ltext = text.find(':')
#print(ltext)
rtext = len(text)
#print(rtext)
target = text[ltext + 1 : rtext]
target = target.strip()
#print(target)
f_target = float(target)
print(f_target)

