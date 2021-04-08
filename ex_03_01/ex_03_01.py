entry_hours = input("Enter Total Hours Worked: ")
entry_rate = input("Enter Employee Pay Rate: ")
fe_h = float(entry_hours)
fe_r = float(entry_rate)
# print(fe_h,fe_r)
if fe_h > 40 :
    # print("Overtime")
    reg_pay = fe_h * fe_r
    ovt_pay = (fe_h-40) * (fe_r*.5)
    # print(reg_pay,ovt_pay)
    total_pay = reg_pay + ovt_pay
    # print(total_pay)
else :
    # print("Regular")
    total_pay = fe_h * fe_r
print("Pay:",total_pay) 