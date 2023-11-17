def print_count():
    with open("/home/eduardo/workspace/github.com/Gearmo312/bookbot/books/frankenstein.txt") as f:
    #...

        file_contents = f.read()

        words = file_contents.split()
    
        count = len(words)

        print(count)

print_count()