def check_string(s):
    print (any(i.isalnum() for i in s ))
    print (any(i.isalpha() for i in s ))
    print (any(i.isdigit() for i in s )) 
    print (any(i.islower() for i in s ))
    print (any(i.isupper() for i in s ))
if __name__ == '__main__':
    s = input()
    check_string(s)
