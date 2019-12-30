import random

def get_secret_word(word_file="/usr/share/dict/words"):
    good_words = []
    with open(word_file) as f:
        for word in f:
            word = word.strip()
            if not word.isalpha():
                continue
            if len(word) < 5:
                continue
            if word[0].isupper():
                continue
            good_words.append(word)

    word = random.choice(good_words)
    return word.lower()



        
        
def hide_secret_word(secret_word, correct_letters):
    l= len(secret_word)
    word = ""
    for i in range(0, l):
        if secret_word[i] in correct_letters:
            word += secret_word[i]

        else:
            word += "_"

    return word


def turns(secret_word, correct_letters, wrong_letters, guess):
    c = False
    for i in secret_word:
        if i == guess:
            if i not in correct_letters:
                correct_letters += guess
            c = True

    if not c and guess.isalpha() and len(guess) == 1:
        if guess not in wrong_letters:
            wrong_letters += guess
        

    hidden_secret_word =hide_secret_word(secret_word, correct_letters)
    return [hidden_secret_word, correct_letters, wrong_letters]

##  state: 0 is dead , 1 is continue game, 2 is win
def dead_or_alive(secret_word= get_secret_word(), correct_letters="", wrong_letters="", guess=''):
    
    
    hidden_secret_word, correct_letters, wrong_letters =turns(secret_word, correct_letters, wrong_letters, guess)
    # print(f"Word:\t{hidden_secret_word}")
    
    # if len(guess)==0:
    #     guess= input("Guess:")

    if len(wrong_letters) < 7:
        state = 1

    else:
        state = 0

    c = False
    for i in secret_word:
        if i not in correct_letters:
            c = False
            break
        else:
            c = True

    if c:
        state=2

    
    return [hidden_secret_word, correct_letters, wrong_letters, state]

    
def main():
    p='y'
    while True:
    
        
        if p == 'y':

            secret_word = get_secret_word()
            print(secret_word)
            hidden_secret_word = hide_secret_word(secret_word, "")
            print(f"\n\nWord:\t {hidden_secret_word}")
            guess = input("Guess:")
            doa = dead_or_alive(secret_word,"","",guess)

            while doa[3]==0 or doa[3]==1 or doa[3]==2:
                
                if doa[3] == 0:
                    print(f"*****You are dead*****\n\nWord was {secret_word}")
                    p = input("Play?(y/n)")
                    break

                elif doa[3] == 1:
                    print(f"\n\nWord:\t { doa[0] }")
                    print(f"\nGuesses:\t{ doa[1] + doa[2]}")
                    print(f"\nChances remaining:{7 - len(doa[2])}")
                    guess = input("\nGuess:")
                    doa = dead_or_alive(secret_word, doa[1], doa[2], guess)

                if doa[3] == 2:
                    print("*****You Won****")
                    p = input("Play?(y/n)")
                    break

        else:
            break

        
main()

          
    
