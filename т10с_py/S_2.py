class EmptyFileError(Exception):
    pass

def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = f.read()
            if not data.strip():
                raise EmptyFileError("файл пустой")
            return data
    except EmptyFileError as e:
        print(e)

file1 = "empty.txt"
file2 = "data.txt"

print("Содержимое data.txt:")
result = read_file(file2)
if result:
    print(result)

print("\nСодержимое empty.txt:")
read_file(file1)