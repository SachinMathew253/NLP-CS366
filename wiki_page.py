import wikipedia
import string
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 


f = open("number.txt" , 'w' , encoding = 'utf-8')
f.write((wikipedia.page("number")).content)
f.close()
f = open("number.txt" , 'r' , encoding = 'utf-8')
text = f.read()
words = text.split()
print("WikiPage on 'Number' is scraped. \nTotal No of Words: %d" %len(words))
print("\nRemoving Punctuations!")
for c in string.punctuation:
    text = text.replace(c,"")
words = text.split()
print("Completed! \nNo of Words: %d \n\nRemoving Numbers!" %len(words))
for c in list(range(0,10)):
	text = text.replace(str(c),"")
print("Completed!")
words = text.split()
print("No of Words: %d" %len(words))

f.close()
f = open("number_wiki.txt" , 'w' , encoding = 'utf-8')
f.write(text)
f.close()
print("\nRemoving Stopwords!")
stop_words = set(stopwords.words('english')) 
f = open("number_wiki.txt" , 'r')
appendFile = open('number_wikiEdit.txt','a') 
line = f.read()
words = line.split() 
for r in words: 
    if not r in stop_words: 
        appendFile.write(" "+r) 
appendFile.close()
appendFile = open('number_wikiEdit.txt','r') 
line = appendFile.read()
words = line.split() 
f.close() 
print("Completed!  File saved as 'number_wikiEdit.txt'")
print("No of Words: %d" %len(words))
appendFile.close()
