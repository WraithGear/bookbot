def main():
    book = "frankenstein.txt"
    book_path = ("books/" + book)
    book_contents = get_book(book_path)
    words = word_count(book_contents)
    letters = letter_count(book_contents)

    #test = letter_count(book_contents)
    #test = word_count(book_contents)
    test = gen_report(book_path, words, letters)
    print(test)


def get_book(book_path):
    #opens book file and returns its contents as a string
    with open(book_path) as f:
        book_content = f.read()
        return book_content

def word_count(book_content):
    #takes the book contents, seperates the words, and returns the amount of words as a number
    book_words = book_content.split()
    return len(book_words)

def letter_count(book_content):
    #takes the book contents and returns a dictionary list with counts of each letter
    import string
    alphabet = {i: 0 for i in string.ascii_lowercase}
    book_letters = book_content.lower()
    for x in book_content.lower():
        if x in alphabet.keys():
            alphabet[x] += 1
    return alphabet

def gen_report(book_path, word_count, letter_count):
    #takes book data, and prints it in a readable format
    report_letters = ""

    value_order = list(letter_count.values())
    value_order.sort(reverse=True)


    print(value_order)
    #for j in letter_count.keys():
    #    report_letters = report_letters + "\n" + "The " + j + " character was found " + str(letter_count[j]) + " times"
    #return report_letters

if __name__ == "__main__":
    main()