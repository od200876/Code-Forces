n = int(input())
while n > 0:
    word = input()

    if len(word) > 10:
        print(f'{word[0]}{len(word[1:-1:])}{word[-1]}')
        n -= 1
    else:
        print(f'{word}')
        n -= 1