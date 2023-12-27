

def get():
    f = open("words.txt", "r")
    file = (f.read())
    lines = file.splitlines()
    return lines


print(get())



