# Write a program to find the most frequent word in a given sentence. If multiple words have the same frequency, return the first one.

sentence = input("Enter a sentence: ")
words= sentence.split()

frequency = None
if not words:
    print("No words in the sentence!")
else:
    # Count word frequencies
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

max_count = max(frequency.values())

most_frequent_word = None
for word in words:
    if frequency[word] == max_count:
        most_frequent_word = word

    break

print("Most frequent word:", most_frequent_word)
