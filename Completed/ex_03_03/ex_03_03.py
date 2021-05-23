enter_score = input ("Enter a score between 0.0 and 1.0: ")
try :
    float_e_s = float(enter_score)
except : 
    print("Error! Please enter in numerical form.")
    quit()

if float_e_s < 0 :
    print ("Please pick a score between one and zero.")
    quit()
elif float_e_s > 1 :
    print ("Please enter a score between one and zero")
    quit()
elif float_e_s >= 0.9 :
    Grade = "A"
elif float_e_s >= 0.8 :
    Grade = "B"
elif float_e_s >= 0.7 :
    Grade ="C"
elif float_e_s >= 0.6 :
    Grade = "D"
else :
    Grade = "F"

print(Grade)