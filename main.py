
def main():
    book = "frankenstein.txt"
    book_path = ("books/" + book)
    book_contents = get_book(book_path)
    words = word_count(book_contents)
    letters = letter_count(book_contents)

    output = gen_report(book_path, words, letters)
    print(output)


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
    import collections
    report_letters = ""
    word_count = str(word_count)

    #take letter_count and put it in value:key reverse order. return front end string.
    ordered_letters = collections.OrderedDict(sorted(letter_count.items(), key=lambda x: x[1], reverse=True))
    for j in ordered_letters.keys():
        report_letters = report_letters + "\n" + "The " + j + " character was found " + str(letter_count[j]) + " times"
    
    final_report = ("--- Begin report of " + book_path + " ---" + "\n" + word_count + " words found in the document" + "\n" + report_letters + "\n" + "--- End report ---" )
    return final_report

if __name__ == "__main__":
    main()