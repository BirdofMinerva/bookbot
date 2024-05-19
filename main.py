#das ist ein comment

def main():
    path = "/home/luna/Documents/Workspace/Github/BirdofMinerva/bookbot/books/frankenstein.txt"


    with open(path, "r") as book:
        read = book.read()
        lowread = read.lower()
        dic = {
            
            "a": 0,
            "b": 0,
            "c": 0,
        }

main()

