def main():
    file_name=input("enter file name : ")
    ifile=open(file_name,"r")
    line_number=0
    char_number=0
    word_number=0
    for line in ifile:
        line_number=1+line_number
        char_number=char_number+len(line)
        word_number=word_number+ len(line.split(" "))
    
    print(char_number, " characters")
    print(word_number, " word")
    print(line_number, " line")
        
    
main()