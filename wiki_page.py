import wikipedia
import string
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from collections import defaultdict

end = "********************************************************************************************************************"
f = open("number.txt" , 'w' , encoding = 'utf-8')
f.write((wikipedia.page("number")).content)
f.close()
f = open("number.txt" , 'r' , encoding = 'utf-8')
text = f.read()
words = text.split()
print("WikiPage on 'Number' is scraped. \nTotal No of Initial Words: %d" %len(words))
print("\nRemoving Punctuations!")
for c in string.punctuation:
    text = text.replace(c,"")
text = text.replace('-',"")
words = text.split()
print("Completed! (kindly note the '−' is a minus and not a hyphen '-')\nNo of Words: %d \n\nRemoving Numbers!" %len(words))
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
print("\nFiles created during the execution. \n'number.txt' -> Original wikipage text\n'number_wiki.txt' -> edited with no Numbers and Punctuations\n'number_wikiEdit.txt' -> further edited with no stopwords")
print("\n Below is the Text containing no stop words:\n")
print(line)

d = defaultdict(int)
q = defaultdict(int)
for w in text.split():
  d[w] += 1

for w in sorted(d, key=d.get, reverse=True):
	q[w] = d[w]
print(end)
print("\nThe below is a dictionary containing the distinct words in file: 'number_wikiEdit.txt'\n")
print(q)	
uniq_word_value = list(q.values())
uniq_word = list(q.keys())

print(end)
print("\nTotal Words: %d\nTotal Distinct Words: %d\n\nTop 10 most frequent words along with its count and Total percentage:\n" % (len(words) , len(uniq_word)))
for i in range(10):
	print(uniq_word[i] + ":\t\tCount-> " + str(uniq_word_value[i])+ "\tPercentage-> "+str(round((uniq_word_value[i]/len(words))*100,2)) +"%")
