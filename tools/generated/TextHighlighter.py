def TextHighlighter(**kwargs):
    text = kwargs.get('text', '')
    highlight = kwargs.get('highlight', '')
    if not highlight:
        return text
    return text.replace(highlight, f'**{highlight}**')