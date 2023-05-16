correct = False
f = open("hangman_word.txt",'r')

letter_list = []
already_guesses = []

for word in f:
    for letters in word:
        letters = letters.lower()
        if letters == '!' or letters == '.' or letters == ',' or letters == '\'' or letters == '-' or letters == '?' or letters == " ":
            pass
        else:
            letter_list.append(letters)

def showing():
    og_word = None
    f = open("hangman_word.txt", 'r')
    for word in f:
        og_word = word
        og_word = og_word.lower()
        word = word.lower()
        for letters in word:
            if letters not in already_guesses:
                if letters == '!' or letters == '.' or letters == ',' or letters == '\'' or letters == '-' or letters == " ":
                    pass
                else:
                    og_word = og_word.replace(f'{letters}','_')

    print(og_word)

guesses = 5
while correct != True:
    ans = input('What is your guess? ')
    ans = ans.lower()
    if ans in letter_list:
        if ans in already_guesses:
            print('You have already guessed this letter.')
            showing()
        else:
            print('You got the letter correct')
            already_guesses.append(f'{ans}')
            showing()
            all_right = True
            for letters in letter_list:
                if letters in already_guesses:
                        continue
                else:
                    all_right = False
                    break
            if all_right == True:
                print('You got the word. Congrats!')
                break
    else:
        if ans in already_guesses:
            print('You have already guesses this letter.')
            showing()
        else:
            guesses = guesses - 1
            if guesses == 0:
                print('You have lost the game.')
                words = None
                for word in f:
                    words = word
                print(f'The word was {words}')
                break
            else:
                print(f'That is not correct. You have {guesses} tries left')
                already_guesses.append(f'{ans}')
                showing()

