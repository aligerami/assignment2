import os
TEMP_FILE_NAME="temp"
def main():
    file_name=input("enter the file name: ")
    removed_string=input("Enter the string to be removed: ")
    infile=open(file_name,"r")
    temp=open(TEMP_FILE_NAME,"w")
    for line in infile:
        temp.write(line.replace(removed_string,""))
    infile.close()
    temp.close()
    os.remove(file_name)
    os.rename(TEMP_FILE_NAME,file_name)
main()
