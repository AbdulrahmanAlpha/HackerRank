def swap_case(s):
    s_c=''
    for i in s :
        if i == i.lower():
           s_c += i.upper()
        else:
           s_c += i.lower()
    return s_c

