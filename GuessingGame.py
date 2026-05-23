import random
import time
# Enter your code here, Guessing Game made by me.

# - GAME MODE SELECTION -
guess = "NONE"
easy_mode = False
hard_mode = False
dev_mode = False
easy_or_hard = input("Do you want it the easy way or the hard way? The Choice is yours... ")

if easy_or_hard == "its me":
    print("DEV MODE GRANTED")
    dev_mode = True
    easy_or_hard = input("Do you want it the easy way or the hard way? The Choice is yours... ")

if easy_or_hard != "complex":
    easy_mode = True
    print("So you dont know? We'll take is easy then.")
    print("")
    time.sleep(1)
    
if easy_or_hard == "complex":
    hard_mode = True
    print("Be Prepared for a Hellish Time...")
    print("")
    time.sleep(1)



# - EASY MODE -

if easy_mode == True:
    special_number = int(random.randint(1, 100))
    if dev_mode == True:
        print(special_number)
        try:
            spec_num_change = int(input("Would you like to change number? (ENTER NON-INT IF NO) "))
            special_number = spec_num_change
            print("Target number has been changed to " +str(special_number))
        except ValueError:
            print("Alright then")
        
    print("The Number is [REDACTED]... and its your Job to guess it!")
    time.sleep(1.75)


# ~ - First Roll - ~
    while isinstance(guess, (str)):
            try:
                guess = int(input("What is your first Guess? (WHOLE NUMBER) "))
            except ValueError:
                print("")
                print("A. Whole. Number, what kinda Guess is that??")
                
    if guess == special_number: #FIRST TRY BABY
        print("WOW!!!, I cant believe you did that there hasnt been someone to do that in " +str(random.randint(100,1000000))+ " Years.")
        time.sleep(3.5)
        print("You truly are someone that deserves the praise.")
        time.sleep(2.5)
        print("Congratulations...")
        time.sleep(2)
        print("GRADE: SS || HARD-KEY: complex")
    
    elif guess > special_number: # OVER
        print("Close but its not that high, Just a few more times and you got it, Right?")
    elif guess < special_number: # UNDER
        print("Close but its higher than that, Just a few more times and you got it, Right?")

        
# ~ Next 99 Rolls ~
    for i in range(2, 101):
        if guess == special_number:
            break
        print("")
        if dev_mode == True:
            print(str(i))
        guess = "NONE"    
        while isinstance(guess, (str)):
            try:
                guess = int(input("Next Guess? "))
                if guess == int:
                    break
            except ValueError:
                print("What am i meant to do with thatt? come on try again, a number.")
                
        if guess == special_number and i < 5: # Get it under OR at 5 guesses
            print("Wow that was fast, You go it only took you " +str(i)+ " Guesses, thats pretty good")
            time.sleep(3)
            print("Good going it doesnt get much better than you!")
            time.sleep(2)
            print("GRADE: S ||  HARD-KEY: complex")
            break
            
        if guess == special_number and i < 15:  # Get it under OR at 15 guesses
            print("Great guesswork, " +str(i)+ " Guesses is all you needed.")
            time.sleep(2.5)
            print("Great Job!!")
            time.sleep(1.5)
            print("GRADE: A ||  HARD-KEY: complex")
            break
            
        if guess == special_number and i < 35:  # Get it under OR at 35 guesses
            print("There you go just took " +str(i + 1)+ " Guesses and your there.")
            time.sleep(2.5)
            print("Good job!")
            time.sleep(1)
            print("GRADE: B ||  HARD-KEY: complex")
            break
            
        if guess == special_number and i < 60: # Get it under OR at 60 guesses
            print("It took some effort but here we are " +str(i)+ " Guesses deep.")
            time.sleep(2.5)
            print("Good job!")
            time.sleep(1.5)
            print("GRADE: C")
            break
            
        if guess == special_number and i < 100: # Get it under OR at 100 guesses
            print("Its well about time so im happy thats done " +str(i)+ " Guesses.")
            time.sleep(2.75)
            print("You've Done It.")
            time.sleep(1.25)
            print("GRADE: D")
            break
        
        guess_range = special_number - guess
        
        if guess > special_number:
            if (guess_range * -1) <= 15: # In the range of 15
                if (guess_range * -1) <= 5: # In the range of 5
                     print("HOT HOT!, Go lower!")
                else:
                    print("Getting hot but thats not it, lower")
            else:
                print("Thats not it, less than that")
            
        if guess < special_number:
            if guess_range <= 15: # In the range of 15
                if guess_range <= 5: # In the range of 5
                    print("HOT HOT!, Go higher!")
                else:
                    print("Getting hot but thats not it, higher")
            else:
                print("Thats not it, more than that")


# - Every Roll Beyond 100, No way it gets to this point. -      
    if guess != special_number:
        count = 100
        time.sleep(2)
        print("Wow this is really gonna take you while huh, well im going on auto pilot see you when you make it")
        time.sleep(2.5)
    while guess != special_number:
        print("")
        count += 1
        guess = "NONE"
        while isinstance(guess, (str)):
            try:
                guess = int(input("Guess -> "))
                if guess == int:
                    break
            except ValueError:
                print("Dont know you know the drill? again.")
        
        
        if guess == special_number:
            print("Oh you got it hooray only took you " +str(count + 1)+ " Tries")
            time.sleep(2.75)
            print("glad thats over")
            time.sleep(1.25)
            print("GRADE: F")
            break
        
        guess_range = special_number - guess
        
        if guess > special_number:
            if (guess_range * -1) <= 15: # In the range of 15
                if (guess_range * -1) <= 5: # In the range of 5
                     print("Burning. come on and get lower")
                else:
                    print("Hot. lower")
            else:
                print("Cold, go low")
            
        if guess < special_number:
            if guess_range <= 15: # In the range of 15
                if guess_range <= 5: # In the range of 5
                    print("Burning. come on and get higher")
                else:
                    print("Hot. higher")
            else:
                print("Cold, go high")
        



# - HARD MODE -



if hard_mode == True:
    special_number = random.randint(1, 100000)
    if dev_mode == True:
        print(special_number)
        try:
            spec_num_change = int(input("Would you like to change number? (ENTER NON-INT IF NO) "))
            special_number = spec_num_change
            print("Target number has been changed to " +str(special_number))
        except ValueError:
            print("Alright then")
    print("The Number is [REDACTED]... lets get to the.. Fun?")
    time.sleep(1.75)
# ~ - First Roll - ~
    while isinstance(guess, (str)):
            try:
                guess = int(input("What is your first Guess? (WHOLE NUMBER) "))
            except ValueError:
                print("")
                print("A. Whole. Number, what kinda Guess is that??")
                
    if guess == special_number: #FIRST TRY BABY
        print("You have been spared the gods must be on your side. Its been "+str(random.randint(10000,1000000000))+ " Years since this has occured.")
        time.sleep(3.5)
        print("How Miraculous.")
        time.sleep(2.5)
        print("Embrace your rewards.")
        time.sleep(2)
        print("GRADE: X || Title Granted: The Chosen One || MASOCHIST-KEY: [COMING SOON]")
        print("Titles would be a thing if i new how to store data, would make masochist if i had more time")
    elif guess > special_number: # OVER
        print("Close but its not that high, Just a few more times and you got it, Right?")
    elif guess < special_number: # UNDER
        print("Close but its higher than that, Just a few more times and you got it, Right?")
    rollcounter = 20
    shift = 1
# ~ Next 99 Rolls ~
    for i in range(2, 101):
        if guess == special_number:
            break
        if i < 20 :
            time.sleep(.25)
            print("You have "+str((shift*(rollcounter))-i)+" Rolls until a number change.") 
        if i != 40 and shift > 1 and shift < 3:
            time.sleep(.25)
            print("You have "+str((shift*(rollcounter))-i)+" Rolls until number change")
        if i != 60 and shift > 2 and shift < 4:
            time.sleep(.25)
            print("You have "+str((shift*(rollcounter))-i)+" Rolls until a number change.")
        if i != 80 and shift > 3:
            time.sleep(.25)
            print("You have "+str((shift*(rollcounter))-i)+" Rolls until a number change.")
        if i == 20 or i == 40 or i == 60 or i == 80:
            special_number = random.randint(1, 100000)
            shift += 1
            print("The number has shifted... ")
            time.sleep(1.5)
            if dev_mode == True:
                print(special_number)
                try:
                    spec_num_change = int(input("Would you like to change number? (ENTER NON-INT IF NO) "))
                    special_number = spec_num_change
                    print("Target number has been changed to " +str(special_number))
                except ValueError:
                    print("Alright then")
                    
        print("")
        if dev_mode == True:
            print(str(i))
        guess = "NONE"
        while isinstance(guess, (str)):
            try:
                guess = int(input("Make a Guess. "))
                if guess == int:
                    break
            except ValueError:
                print("Whole Number.")
                
        if guess == special_number and i < 5: # Get it under OR at 5 guesses
            print("Done and with haste " +str(i)+ " Guesses, thats remarkable")
            time.sleep(3)
            print("It doesnt get much better than this so be proud")
            time.sleep(2)
            print("GRADE: SSS || TITLE GRANTED: Titan of Titaninum || MASOCHIST-KEY: [COMING SOON]")
            print("Titles would be a thing if i new how to store data, would make masochist if i had more time")
            break
            
        if guess == special_number and i < 15:  # Get it under OR at 15 guesses
            print("Great work, " +str(i)+ " Guesses is all you needed")
            time.sleep(2.5)
            print("Nicely Done")
            time.sleep(1.5)
            print("GRADE: SS || TITLE GRANTED: The Platinum Paladin || MASOCHIST-KEY: [COMING SOON]")
            break
            
        if guess == special_number and i < 40:  # Get it under OR at 35 guesses
            print("Just took you " +str(i)+ " Guesses and your there.")
            time.sleep(2.5)
            print("Be proud.")
            time.sleep(1)
            print("GRADE: S || TITLE GRANTED: Gilded-in-Gold Gladitor")
            break
            
        if guess == special_number and i < 60: # Get it under OR at 60 guesses
            print("Not half bad your only" +str(i)+ " Guesses deep.")
            time.sleep(2.5)
            print("Good work")
            time.sleep(1.5)
            print("GRADE: A || TITLE GRANTED: Savage in Sliver")
            break
            
        if guess == special_number and i < 100: # Get it under OR at 100 guesses
            print("Good Effort you've done it in " +str(i)+ " Guesses.")
            time.sleep(2.75)
            print("Keep your head high")
            time.sleep(1.25)
            print("GRADE: B || TITLE GRANTED: Bronze Barbarian")
            break
        
        guess_range = special_number - guess
        
        if guess > special_number:
            if (guess_range * -1) <= random.randint(900, 3000): # In the range of around 900 to 3000
                if (guess_range * -1) <= 50: # In the range of 50
                     print("Its almost there, just a bit lower.")
                else:
                    print("Your in its range just, go lower.")
            else:
                print("Its lower than this keep pushing.")
            
        if guess < special_number:
            if guess_range <= random.randint(900, 3000): # In the range of around 900 to 3000
                if guess_range <= 50: # In the range of 50
                    print("Its almost there, just a bit higher.")
                else:
                    print("Your in its range just, go higher.")
            else:
                print("Its higher than this keep pushing.")
    
    if guess != special_number:
        count = 100
        time.sleep(2)
        print("Keep on pressing and its sure to come.")
    
# - Every Roll Beyond 100, No way it gets to this point. -    
    while guess != special_number:
        print("")
        count += 1
        guess = "NONE"
        while isinstance(guess, (str)):
            try:
                guess = int(input("Guess... "))
            except ValueError:
                print("")
                print("Dont you know the Drill? Again.")
        
        
        if guess == special_number:
            print(str(count + 1)+ " Tries, Despite that you got it and that is comendable")
            time.sleep(2.75)
            print("Dont be Sad in the time it took, but glad in the freedom of the other side.")
            time.sleep(1.25)
            print("GRADE: [IRRELIVENT]")
            break
        
        guess_range = special_number - guess
        
        if guess > special_number:
            if (guess_range * -1) <= random.randint(900, 3000): # In the range of around 900 to 3000
                if (guess_range * -1) <= 50: # In the range of 50
                     print("wamer. lower")
                else:
                    print("warm. lower")
            else:
                print("freezing, lower")
            
        if guess < special_number:
            if guess_range <= random.randint(900, 3000): # In the range of around 900 to 3000
                if guess_range <= 50: # In the range of 50
                    print("wamer. higher")
                else:
                    print("warm. higher")
            else:
                print("freezing, higher")
                
        # yeah i would do more but ive got some things to get done