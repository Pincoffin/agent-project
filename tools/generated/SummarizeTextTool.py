import nltk
def summarize_text(text, num_sentences=3):
    sentences = nltk.sent_tokenize(text)
    score_sentences = [(sentence, len(sentence.split())) for sentence in sentences]
    scores = sorted(score_sentences, key=lambda x: x[1], reverse=True)
    summary = ' '.join([scores[i][0] for i in range(num_sentences)])
    return summary