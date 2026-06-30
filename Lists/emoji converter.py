emoji_dict={
    ":)":"😀",
    ":(":"😔"
}
message=input(">")
output=""
wordz=message.split(' ')
for word in wordz:
    output+=emoji_dict.get(word,word)+" "

print(output)