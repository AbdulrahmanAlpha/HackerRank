def count_substring(string, sub_string):
    start = 0 
    end = len(sub_string)
    counter = 0
    while end <= len(string):
        if string[start:end] == sub_string:
            counter +=1
        start += 1 
        end+=1  
        
    return counter

