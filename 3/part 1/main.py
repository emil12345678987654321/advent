
if __name__ == '__main__':
    with open('C:/Users/Emil/PycharmProjects/advent/3/data.txt') as f:
        result = 0
        contents = f.read()
        backpacks = contents.split()
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for item in backpacks:
            length = len(item) // 2
            sliced_text1 = slice(length)
            sliced_text2 = slice(length, length * 2, 1)
            part1 = item[sliced_text1]
            part2 = item[sliced_text2]
            smilar = ""
            for i in part1:
                if i in part2:
                    smilar = i
            value = alphabet.find(smilar) + 1
            result += value
        print(result)
