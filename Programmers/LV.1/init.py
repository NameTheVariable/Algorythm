import nltk
import pickle
from nltk.corpus import stopwords
import re

nltk.download('all')
with open('words.txt', 'r', encoding='utf8') as f:
    content = f.read()
# String function인 replace를 사용하거나 re를 사용
cleaned_content = re.sub(r'[^\.\?\!\w\d\s]', '', content)  # 문장단위로 끊기
print(cleaned_content)
