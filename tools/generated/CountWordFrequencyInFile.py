
def CountWordFrequencyInFile(**kwargs):
    path = kwargs.get('path', '')
    content = read_file_content(path)['content']
    words = content.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
