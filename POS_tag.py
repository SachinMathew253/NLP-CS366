from textblob import TextBlob
f = open('textfield.txt', 'w')
f.write(raw_input("Enter the string:"))
f.close()

f = open('textfield.txt', 'r')
text = f.read()
text_with_tags = TextBlob(text)
print(text_with_tags.tags)
f.close()
