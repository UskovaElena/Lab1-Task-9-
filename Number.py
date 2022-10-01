import re
import roman
import os


def repl(m):
    n = roman.fromRoman(str(m.group(0)))
    return str(n)


def isStr(str_):
    res = re.sub(r"\b(?=[MDCLXVI])(.M{0,3}(?:CM|CD|D?C{0,3})?(?:XC|XL|L?X{0,3})?(?:IX|IV|V?I{0,3})?)\b", repl,
                 str(str_))

    print(res)

def isFile(file):
    f = open(file, 'r+')
    try:
        str_ = f.read()
        res = re.sub(r"\b(?=[MDCLXVI])(.M{0,3}(?:CM|CD|D?C{0,3})?(?:XC|XL|L?X{0,3})?(?:IX|IV|V?I{0,3})?)\b", repl,
                     str(str_))
        f.truncate(0)
        f.seek(0)
        f.write(res)
        print("Done")
    finally:
        f.close()

flag = True
s = input('Enter 1 to operate on a string and 2 to operate on a text file:\n')
if s == '1':
    string = input('Enter your string, please:\n')
    isStr(string)
elif s == '2':
    while (flag):
        path = input('Enter the file path, please:\n')
        #path = r"C:\Users\Алёна\PycharmProjects\numbers\1.txt"
        if os.path.exists(path):
            if os.path.isfile(path):
                flag = False
                isFile(path)
            elif os.path.isdir(path):
                print('This is not a .txt file. Please, try again\n')
        else:
            print('File not found. Please, try again\n')


