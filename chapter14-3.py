
def main():
    file_name=input("enter the python file name: ")
    ifile=open(file_name,"r")
    result=dict()
    for line in ifile:
        word_list=line.strip().split(" ")
        for i in word_list:
            if i in result:
                result[i] += 1
            else:
                result[i] = 1 
    
    for j in result:
        print(j, "  " ,result[j])
            

main()