import io
from pprint import pprint

def custom_write(file_name, strings):

    file = open(file_name, 'w', encoding = 'utf - 8')
    string_positions = {}
    line_number = 0
    for i in strings:
        line_number +=1
        key = (line_number, file.tell())
        string_positions[key] = i
        file.write(f'{i}/n')
    file.close()
    return string_positions


if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)


