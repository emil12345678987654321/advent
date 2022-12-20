
if __name__ == '__main__':
    with open('C:/Users/Emil/PycharmProjects/advent/3/data.txt') as f:
        result = 0
        contents = f.read()
        backpacks = contents.split()
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        arr = []
        for item in backpacks:
            if len(arr) <= 3:
                if item not in arr:
                    arr.append(item)
            if len(arr) == 3:
                for j in arr[0]:
                    if j in arr[1] and j in arr[2]:
                        smilar = j
                value = alphabet.find(smilar) + 1
                result += value
                arr = []
        print(result)
