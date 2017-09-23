file_name=input("enter the file name")
ifile=open(file_name,"r")
list_vows=(['a','e','i','o','u'])
consonants_number=0
vows_number=0
list_vows=(['a','e','i','o','u'])
for line in ifile:
    for i in line:
        if i in list_vows:
            vows_number+=1
        else:
            consonants_number+=1
print("the number of vowels  is ",vows_number,"and consonants",consonants_number)

