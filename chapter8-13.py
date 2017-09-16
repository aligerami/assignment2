def prefix(s1, s2):
    n = len(s2) if len(s1)<len(s2) else len(s1)
    result=""
    for i in range (0,n):
        if s1[i] == s2[i]:
            print(s1[i])
            result+=s1[i]
        else:
            break;
          
    return result
def main():
    s1=input("please enter first string: ")
    s2=input("please enter second string: ")
    print(prefix(s1,s2))

main()    
    