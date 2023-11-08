print(''' 
██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝ \n\n''')

word=["python","array","function","chips","processors","java","html","current","loop","transistor","engine","engenium","scanner","software","radiation","algorithm","blockchain","errors","firewall"]
stages=['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
used_letters = []
import random
i=random.choice(word)
print("_ "*len(i))
# print(f"The chosen word is {i}")
display=[]
for letter in i:
    display+="_"
print(display)
s=0
count=display.count("_")
while count>0:
    guess=input("Guess a letter ")
    guess=guess.lower()
    if guess in used_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue

    used_letters.append(guess)
    for z in range(0,len(i)):
        if(guess==i[z]):
            display[z]= guess
    print(display)
    count=display.count("_")
    if(display.count(guess)==0):
        print(stages[s])
        s+=1
    if(s>6):
        count=0
        print(f"The word is {i}")
        print("You loose")
    
if(display.count("_")==0):
    print("You win")
    
