s=input("Enter string: ")
def make_dict(x):
    dictionary = {}
    for letter in x:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary
def most_frequent(s):
    letters = [letter.lower() for letter in s]
    dictionary = make_dict(letters)
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print (letter,":",count, end="   ")
most_frequent(s)
