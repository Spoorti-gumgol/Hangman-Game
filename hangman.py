#part 1 of the game 
import random
from word_list_hangman import word_list
from stages_hangman import logo,stages
import os







print(logo)
#word_list = ["aardvark", "baboon", "camel"]
lives = 6

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
chosen_word = random.choice(word_list)
#print(f'Pssst, the solution is {chosen_word}.')
#user_guess = input("Guess a letter: ")
#guess = user_guess.lower()
#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].


#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
word = []
for p in range(0,len(chosen_word)):
    word.append("_")
end_of_game = False
while end_of_game == False:
    user_guess = input("Guess a letter: ")
    guess = user_guess.lower()
    os.system('cls')
    if guess in word:
        print(f"You've already guessed this letter {guess}")
    for i in range(0,len(chosen_word)):
        let = chosen_word[i]
        if user_guess == let:
            word[i] = user_guess    
    if user_guess not in chosen_word:
        print(f"The letter you have guesses {guess} is not in the word hence you lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!!!")
            print(f"The word was {chosen_word}")
        
        

    if "_" not in word:
        end_of_game = True
        print("You Won!!!")
    print(f"{' '.join(word)}")
    print(f"Number of lives left: {lives}")

    print(stages[lives])      
#Testing code

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

 #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.





