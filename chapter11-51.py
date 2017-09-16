import string
def validate_latin_square(m):
    list=[chr(i) for i in range(ord('a'),ord('z')+1)]
    flag=True
    list=list[0:len(m)]
    result=[0]*len(m)
    for i in range (0,len(m)):
        for j in range (0,len(m)):
            if not flag:
                return False
            flag=False
            for k in range (0,len(m)):
                if list[k]==(m[i][j]).lower():
                    result[k]=result[k]+j+i
                    flag=True
    for h in result:
        if(h!=len(result)*(len(result)-1)):
            return False
                
    return True
def main():
    n=int(input("Enter number n:"))
    counter=0
    m=n*[0]
    alphabet=[chr(i) for i in range(ord('a'),ord('z')+1)]
    alphabet=alphabet[0:n]
    print(alphabet)
    while counter<n:
        list= input("Enter "+str(n)+" rows of letters separated by spaces: ").split(" ")
        m[counter]=[str(i) for i in list]
        
        print()
        flag=True
        for j in range (0,len(m)):
            flag=False
            for k in range (0,len(alphabet)):
                if str(alphabet[k])==(str(m[counter][j])).lower():
                    flag=True
            if not flag:
                print("Wrong input the letter should be from",str(alphabet[0:1]),"to",str(alphabet[len(list)-1:len(list)]))
                return False
        counter=counter+1
        
    
    print(validate_latin_square(m))
    m=[['a','b','c'],['b','c','a'],['c','a','b']]
main()
#print('A'.lower())