message = input("> ")
words = message.split(" ")
emojis = {
    ":)": "😀",
    ":(": "😔",
    # Add more key-value pairs to work with more emojis
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
