import random
from re import A

word_bank=['giraffe','monkey','zebra','whale','fish','shark','horse']
word = random.choice(word_bank)

display = []
wordLen =len(word)
for letter in range(wordLen):
    display += "_"
    
lives = 6   

end_game = False    
while not end_game:    
    guess = input("Guess a letter: ").lower()
    for position in range(wordLen):
        letter = word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if guess not in word:
        lives -= 1
        livesStr =str(lives)
        print(livesStr + " lifes left")
        if lives == 0:
            end_game = True
            print("You lost")
    
    if "_" not in display:
        end_game = True
        print("You win")