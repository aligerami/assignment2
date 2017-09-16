import urllib.request
def main():
    URL="http://cs.armstrong.edu/liang/data/Lincoln.txt"

    file = urllib.request.urlopen(URL)
    file=file.read().decode()
    number_count=len(file.split(" "))
    print("number of words is ",number_count)

main()