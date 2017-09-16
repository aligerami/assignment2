def count_letters(s):
    counter=0
    for char in s:
        if char.isalpha()==True:
            counter+=1
    return counter

test=input("Please enter The string: ")
print("number of letter is ",count_letters(test))


        