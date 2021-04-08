count = 0
total = 0
entry = input('Enter a file name: ')
grab = open(entry)
for strings in grab : 
    if not strings.startswith("X-DSPAM-Confidence:") :
        continue
    unc_vars = strings
    lc_unc_vars = unc_vars.find(':')
    # print(lc_unc_var)
    tc_unc_vars = len(unc_vars)
    # print(tc_unc_vars)
    target = unc_vars[lc_unc_vars + 1 : tc_unc_vars] 
    target = target.strip()
    # print(target)
    count = count + 1
    cln_vars = float(target)
    # print(cln_vars)
    total = total + cln_vars

average = total / count
# print(average, total, count)
print('Average spam confidence:', average)
# print('Done')