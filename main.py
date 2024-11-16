def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = word_count(text)
    characters = character_count(text)
    print(text)
    print(f"Word count: {words}")
    character_report(characters)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    lowered_text = text.lower()
    characters = {}
    for character in lowered_text:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def character_report(characters):
    for char in characters:
        print(f"The '{char}' character was found {characters[char]} times")
    print("--- End Report ---")


main()