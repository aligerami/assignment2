def  q_1(s1,s2):
    counter=0
    for i in range (0,len(s2)-len(s1)):
        for j in range (0, len(s1)):
            if(s2[i+j]!=s1[j]):
                break
            else:
                counter=counter+1
        if counter==len(s1):
            return True
        else:
            counter=0
    return False
            
print(q_1("abcd","1aqbcde"))