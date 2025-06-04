def read_input(file_path=None):
    if file_path:
        with open(file_path,'r',encodings='utf-8') as f:
            return f.read()
    else:
        import sys
        return sys.stdin.read()
    


#count functions
def count_lines(text):
    return text.count('\n')

def count_words(text):
    return len(text.split())

def count_chars(text):
    return len(text)

def count_bytes(text):
    return len(text.encode('utf-8'))
