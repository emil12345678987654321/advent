if __name__ == '__main__':
    with open('/6/data.txt') as f:
        contents = f.read()
        print(contents)
        move = True
        start, stop = 0, 4
        while move:
            message = contents[start:stop]
            unique = ''.join(set(message))
            if len(unique) == 4:
                move = False
                print(stop)
            start += 1
            stop += 1
