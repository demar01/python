from collections import Counter
from urllib import request
import os
import re

#print(dir(request))
#resp= request.urlopen("https://www.wikipedia.org")
#type(resp)
#print(dir(resp))
#print(resp.code) #if 200 ok ; resp.peek() html file

text= "hi , I say hi at least 3 times. Hi , do you see three?"

words = text.split()

counter=Counter(map(str.lower, words))
print(counter)
top_three=counter.most_common(3)
print(top_three)

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)
def get_harry_most_common_word():
    harry_words = re.sub(r'[^a-zA-Z\s*]', "",open(harry_text).read().lower()).split()
    words = (word for word in harry_words if word not in open(stopwords_file).read())
    return Counter(words).most_common(1)[0]
