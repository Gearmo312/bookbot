def main():
    book_path = "/home/eduardo/workspace/github.com/Gearmo312/bookbot/books/frankenstein.txt"
    text = text_read(book_path)
    word_count = print_count(text)
    letter_count = letter_dict(text)
    report = write_report(word_count, letter_count)
    print("Report of Frankenstein")
    print(f"There are {word_count} words in this story")
    for k, v in letter_count.items():
         if k.isalpha():
              print(f"{k} appears {v} times")
         


def text_read(book_path):
    with open(book_path) as f:
        text = f.read()
        return text
    
def print_count(text):
        words = text.split()
    
        count = len(words)

        return count

  

def letter_dict(text):

        letters = {}
        for letter in text:
            lowered = letter.lower()
            if lowered in letters:
                letters[lowered] += 1
            else:
                letters[lowered] = 1
        ordered_dict = dict(sorted(letters.items()))
        return ordered_dict

def write_report(word_count, letter_count):
    sorted_list = [(key, value) for key, value in letter_count.items()]
    sorted_list.sort()
    
    return sorted_list
    
    


    
main()    