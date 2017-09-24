from os import listdir
from os.path import isfile, join,isdir

location=input("Enter the name of directory: ")

def number_of_files(address):
    onlyfiles = [f for f in listdir(address) if isfile(join(address, f))]
    directories = [d for d in listdir(address) if isdir(join(address, d))]
    if len(directories)==0:
        return onlyfiles
    for i in directories:
        onlyfiles=onlyfiles +(number_of_files(join(address, i)))
    
    return (onlyfiles)
    

print(number_of_files(location))