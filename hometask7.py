#1
n = int(input())
file = open('article.txt', 'r')
rows_number = len(file.readlines())

def read_last(lines, file):
    f = open(file, 'r')
    rows = f.readlines()
    for row in rows[lines:]:
        print(row)

if n > 0 and n < rows_number:
    read_last(n, 'article.txt')

#2
import os

def print_docs(directory):
    if os.path.exists(directory):
        for item in os.listdir(directory):
            path = os.path.join(directory,item)
            print(path)
            if os.path.isdir(path):
                print_docs(path)
    else:
        print(f'Папки {directory} не существует')

print_docs('check')

#3
def longest_words(file):
    with open(file, 'r') as f:
        content = f.read()
    words = content.split()
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    return longest_words

print(longest_words('article.txt'))

#4
def simple_text_editor():
    file_name = input()
    file_name += '.txt'
    with open(file_name, 'w') as f:
        while True:
            line = input()
            if line.strip() == '' or not line.isprintable():
                break
            f.write(line + '\n')
            
simple_text_editor()