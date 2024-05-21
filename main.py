def main():
    path = "/home/luna/Documents/Code/Github/bookbot/books/frankenstein.txt"

    def return_lower() -> dict:
        with open(path, "r") as book:
            read = book.read()
        lower_read = read.lower()
        dic = {}

        for i in lower_read:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        return dic

    def sort_dic(dic: dict):
        dic_list = []
        for key, value in dic.items():
            dic_list.append({'key': key, 'value': value})

        dic_list.sort(reverse=True, key=lambda x: x['value'])

        for item in dic_list:
            if item['key'] not in ['\n', ' ']:
                print(f"The '{item['key']}' character was found '{item['value']}' times")

    sort_dic(return_lower())

main()

