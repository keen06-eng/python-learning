word='hope'
guess_count=0
hint_count =1
while True :
    guess=input("Enter your guess word(4 letter word):")
    if len(guess)!=4:
       print("Guess should be a 4 letter word")
       continue
    if guess==word:
        print("You won!!")
        break
    else:
        guess_count+=1
        if guess_count>3:
          print("You out of guesses!!")
          break
        print(f"Hint:{word[:hint_count]}")
        hint_count+=1
        
    




