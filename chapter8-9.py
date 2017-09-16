def binary_to_hex(s):
    result=""
    s= s if len(s)%4== 0  else s.rjust(((len(s)//4)+1)*4)  
    for i in range (0,len(s)//4):
        result+=convert_to_hex(s[i*4:4*(i+1)])
    return result
def convert_to_hex(s):
    number=int(s, 2)
    if(number==10):
        return 'A';
    elif(number==11):
        return 'B'
    elif(number==12):
        return 'C'
    elif(number==13):
        return 'D'
    elif(number==14):
        return 'E'
    elif(number==15):
        return 'F'
    return str(number)

def main():
    test=input("please enter your string:")
    print(binary_to_hex(test))

main()
    