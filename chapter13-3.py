def main():
    file_name=input("enter the file name :")
    ifile=open(file_name,"r")
    score_count=0
    score_sum=0
    for line in ifile:
        score_list=line.split(" ")
        score_count=score_count+len(score_list)
        for i in score_list:score_sum=score_sum+int(i)
    print("There are ",str(score_count)," scores")
    print("The total is",score_sum)
    print("The avarage is",score_sum/score_count)
    
    
main()