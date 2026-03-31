import math
import re
from collections import Counter

def text_analysis(title,text):
    counted = Counter(text)
    letter_frequencies=[]
    for i in range(len(counted)):
        letter_frequencies.append(list(counted.values())[i]/len(text))
    total = 0
    for i in range(len(letter_frequencies)):
        total+=(letter_frequencies[i]*math.log2(letter_frequencies[i]))
    total *= -1
    print(title+ str(total))



letter_frequencies = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]

with open('english_texts/bible.txt', 'r', encoding='utf-8') as f:
    bible = f.read().lower()
with open('english_texts/science.txt', 'r', encoding='utf-8') as f:
    science = f.read().lower()
with open('english_texts/literature.txt', 'r', encoding='utf-8') as f:
    literature = f.read().lower()

total = 0
for i in range(len(letter_frequencies)):
    total+=(letter_frequencies[i]*math.log2(letter_frequencies[i]))
total *= -1
print("Statistical: "+str(total))

converted_literature = re.sub(r'[^A-Za-z]', '', literature)
converted_science = re.sub(r'[^A-Za-z]', '', science)
converted_bible = re.sub(r'[^A-Za-z]', '', bible)


text_analysis("literature:  ",converted_literature)
text_analysis("science:     ",converted_science)
text_analysis("bible:       ",converted_bible)
text_analysis("test:        ","thequickbrownfoxjumpsoverthelazydog")
text_analysis("test2:       ",converted_bible[0:26])





