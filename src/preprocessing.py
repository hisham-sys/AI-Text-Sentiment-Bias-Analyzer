import re
import nltk
from nltk.corpus import stopwords

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

def clean_text(text):
    text = str(text).lower()
    
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    
    text = re.sub(r'@[A-Za-z0-9]+', '', text)
    text = re.sub(r'#', '', text)
    
    text = re.sub(r'[^a-z\s]', '', text)
    
    stop_words = set(stopwords.words('english'))
    words = text.split()
    cleaned_words = [w for w in words if w not in stop_words]
    
    return " ".join(cleaned_words)

if __name__ == "__main__":
    test_text = "Hello! Check this link https://github.com/hisham #AI @Eng_Hisham 2026"
    print("Before:", test_text)
    print("After :", clean_text(test_text))