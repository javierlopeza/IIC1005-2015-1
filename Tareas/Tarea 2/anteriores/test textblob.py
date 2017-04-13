from textblob import TextBlob
from statistics import pstdev

text = '''
The movie is good
'''

blob = TextBlob(text)

for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
# 0.060
# -0.341
for sentence in blob.sentences:
    print(sentence.sentiment.subjectivity)




data = [1,2,3,4,5]
print(pstdev(data))
