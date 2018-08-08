def read_text():
    fd = open("./movie_quotes.txt")
    contents = fd.read()
    fd.close()
    print(contents)

read_text()
