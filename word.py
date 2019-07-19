user_input=input("Enter a word: ")
x=len(user_input)
#variables of certain datatypes
word=[]
record_guesses=[]
fails=0
maxFails=7
correct=0
tries=0

#makes a corresponding list of underscores for each letter in the input
for i in range(x):
    word.extend("_")
    
#little intro, just lets the player know how many chances they have
print("You have "+str(maxFails)+" attempts to figure out this word")
print("Good Luck!\n")

#while the number of FAILS is not at maximum the following loop happens
#DID NOT MAKE IT TRIES
while fails != maxFails:
    tries+=1 #everytime it enters the loop, whether right or wrong, is a try
    print(word) # prints current word solved
    guess=input("Guess a letter: ")
    if len(guess)> 1: #if the guess is more than one letter, try again
        record_guesses.append(guess)
        guess=input("Try again with one letter:")
        fails+=1
    else:
        record_guesses.extend(guess)
        for k in range(x):  #if the guess is in the user_input, switch the corresponding "_" out
            if guess==user_input[k]:
                word[k]=user_input[k]
                correct+=1
                if(correct==x): #if the correct number of guesses is the length of the word= end the loop
                    print("Congrats the correct answer was: "+user_input)
                    print("You solved it in "+str(tries)+" tries")
                    exit()
    fails+=1
    print("You have "+str(maxFails-fails)+" tries left")
    print("Remember you have already guessed: "+ str(record_guesses)+"\n")
if fails == maxFails: #if the user does not solve it, error message
    print("Sorry, you lose! :(")
    print("The correct answer was: "+user_input)
    exit()
