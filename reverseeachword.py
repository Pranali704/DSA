sentence = input("Enter a sentence: ")

words = sentence.split()

for i in range(len(words)):
    words[i] = words[i][::-1]

result = " ".join(words)

print("Result =", result)