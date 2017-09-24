def display_permuation(s):
    if len(s)==1:
        return s 
    else:
        temp = []
        for k in range(len(s)):
            part = s[:k] + s[k+1:]
            print(s[:k])
            print(s[k+1:])
            for m in display_permuation(part):
                temp.append(s[k:k+1] + m)
        return temp
    
print(display_permuation("abc"))
    