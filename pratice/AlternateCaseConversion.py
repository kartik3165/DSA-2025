def name(s):
    res = ""
    for i in range(len(s)):
        if i%2 == 0: 
            res += s[i].lower()
        else:
            res += s[i].upper()  
    return res

print(name('kartik'))