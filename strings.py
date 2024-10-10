#Work Play game

word = input("Enter a word: ")

#Length of the word
print("Length of word: ", len(word))

#Uppercase of the word
print("Uppercase of the word: ", word.upper())

#Lowercase of the word
print("Lowercase of the word: ", word.lower())

#Counting occurences
letter = input("Enter a letter: ")
print(f"'{letter}' occurs {word.count(letter)} times in '{word}'")

substring = input("Enter a substring: ")
print(f"'{substring}' occurs {word.count(substring)} times in '{word}'")

#Reversing the word
reverse_word = word[::-1]
print("Reversed word: ", reverse_word)

#Slicing  the word
start_index = int(input("Enter a starting index: "))
end_index = int(input("Enter an ending index: "))
sliced_word = word[start_index:end_index]
print("Sliced word:", sliced_word)

# Replacing a character
char_to_replace = input("Enter a character to replace: ")
replacement_char = input("Enter the replacement character: ")
new_word = word.replace(char_to_replace, replacement_char, 1)
print("Replaced:", new_word)

# Concatenating with another word
second_word = input("Enter a second word: ")
concatenated_word = word + second_word
print("Concatenated:", concatenated_word)

# Checking for palindrome and valid identifier
is_palindrome = word == reverse_word
is_valid_identifier = word.isidentifier()

print("Is a palindrome?", is_palindrome)
print("Is a valid Python identifier?", is_valid_identifier)


