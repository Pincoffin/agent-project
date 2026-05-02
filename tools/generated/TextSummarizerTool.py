def text_summarizer_tool(**kwargs):
    text = kwargs.get('text', '')
    return summarize_text(text)