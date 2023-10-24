with open('file_demo.txt', 'r') as f:
    read_file = f.read()

words = read_file.split(' ')
word_count = len(words)
print(word_count)
