def computepay(hours, rate) :
    #print("In computepay", hours, rate)
    if hours > 40 :
        reg_pay = hours * rate
        ovt_pay = (hours-40) * (rate*.5)
        total_pay = reg_pay + ovt_pay
    else :
        total_pay = hours * rate
    #print("Returning", total_pay)
    return total_pay

entry_hours = input("Enter Total Hours Worked: ")
entry_rate = input("Enter Employee Pay Rate: ")
fe_h = float(entry_hours)
fe_r = float(entry_rate)
t_p = computepay(fe_h,fe_r)

print("Pay:",t_p) 