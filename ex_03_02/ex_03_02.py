entry_hours = input("Enter Total Hours Worked: ")
entry_rate = input("Enter Employee Pay Rate: ")
try :
    fe_h = float(entry_hours)
    fe_r = float(entry_rate)
except :
    print("Error, please enter numeric input.")
    quit()
print(fe_h,fe_r)
if fe_h > 40 :
    reg_pay = fe_h * fe_r
    ovt_pay = (fe_h-40) * (fe_r*.5)
    total_pay = reg_pay + ovt_pay
else :
    total_pay = fe_h * fe_r
print("Pay:",total_pay) 