def emoji_converter(message):

    words = message.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "😔",
        # Add more key-value pairs to work with more emojis
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
print(emoji_converter(message))
