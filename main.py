import random


def main():
    print('\nThis is a word guessing game. The word will be 5 letters long and you will be told if each letter of your\n'
          'guess appears in the word or not and if it is in the right position or not.')
    with open("words.txt") as file:
        wordle = file.readlines()
        x = len(wordle)
        for i in range(x):
            wordle[i] = wordle[i].strip('\n')
    y = random.randint(0, x)
    word = wordle[y]
    print(word)
    while True:
        guess = raw_input("Guess a word\n")
        if guess.strip() == word.strip():
            print('Congratulations, You Win')
            break
        else:
            if guess in wordle:
                for t in range(len(guess)):
                    if guess[t] == word[t]:
                        print(guess[t])
                    else:
                        if guess[t] == word[1] or guess[t] == word[2] or guess[t] == word[3] or guess[t] == word[4]:
                            print('? ' + '(' + guess[t] + ')')
                        else:
                            print('.')
            else:
                print('That is not a real word, please try again')
            print('That is not the word, try again please')


if __name__ == '__main__':
    main()
