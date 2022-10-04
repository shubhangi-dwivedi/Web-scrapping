import nltk
nltk.download('words')
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('averaged_perceptron_tagger')
nltk.download('state_union')
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import operator


train_text = state_union.raw()

text = open("keywords1.txt",'r')

dict1 = {}

for row in text:
    partitioned_string = row.partition(' :')
    str1= partitioned_string[0]

    custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
    tokenized = custom_sent_tokenizer.tokenize(str1)

    for i in tokenized:
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)
        # namedEnt = nltk.ne_chunk(tagged, binary=False)
        # print(tagged)
        selective_pos = ['NN']
        for word, tag in tagged:
            if tag not in selective_pos:
                    if word in dict1:
                        dict1[word] += 1
                    else:
                        dict1.update({word: 1})
        print(i)

dict1_sorted = dict(sorted(dict1.items(),key=operator.itemgetter(1),reverse=True))

file1 = open("pos_not_nn.txt", "a",encoding="utf-8")
for allKeys in dict1_sorted:
    txt=allKeys
    file1.write(txt)
    file1.write("\n")

file1.close()