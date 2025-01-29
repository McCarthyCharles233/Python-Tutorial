sentence = input("Input a sentence: ")
words = sentence.split()
word_count = 0

for i in words:
    word_count+=1
print(word_count)

# most appropriate answer
# sentence = input("Input a sentence: ")  # No need for str()
# words = sentence.split()  # Split the sentence into words
# word_count = len(words)  # Use len() to count the words
# print(word_count)