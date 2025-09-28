string = 'hello'
values = [0, 2, 4, 6, 8, 10]
counter = 0
while counter <= 10:
    memory = string
    if counter in values:
        string = string + ' world'
    print(string)
    if counter < 10:
        string = memory
    counter += 1