# Write a Python function that takes a list of words and return the longest word and the length of the longest one.

# Solution:

def find_longest_word(words):
    if not words:
        return None, 0

    longest_word = words[0]
    max_length = len(longest_word)

    for word in words[1:]:
        word_length = len(word)
        if word_length > max_length:
            longest_word = word
            max_length = word_length

    return longest_word, max_length

towns = ["New York", "Los Angeles", "Chicago", "San Francisco", "Seattle"]
longest, length = find_longest_word(towns)
print(f"The longest town name is '{longest}' with a length of {length} characters.")
