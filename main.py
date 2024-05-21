#das ist ein comment

def main():
    path = "/home/luna/Documents/Code/Github/bookbot/books/frankenstein.txt" 


    with open(path, "r") as book:
        read = book.read()
        lowread = read.lower()
        dic = {}
        
        for i in lowread:
            if i not in dic:
                dic.update({i:1})
            else:
                dic[i] += 1

        print(dic)


main()

