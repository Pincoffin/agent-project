
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def summarize_text(text, summary_length=10):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    
    freq_table = dict()
    for word in words:
        if word.lower() not in stop_words and word.isalnum():
            if word.lower() in freq_table:
                freq_table[word.lower()] += 1
            else:
                freq_table[word.lower()] = 1
                
    sentences = sent_tokenize(text)
    sentence_value = dict()
    
    for sentence in sentences:
        for word, freq in freq_table.items():
            if word in sentence.lower():
                if sentence in sentence_value:
                    sentence_value[sentence] += freq
                else:
                    sentence_value[sentence] = freq
                    
    summary_sentences = sorted(sentence_value, key=sentence_value.get, reverse=True)
    summary_sentences = summary_sentences[:summary_length]
    
    summary = ' '.join(summary_sentences)
    return summary
