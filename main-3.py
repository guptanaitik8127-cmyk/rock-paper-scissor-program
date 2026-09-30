'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import random
l =["rock","scissor","paper"]
'''

rock vs pepar ->paper wins
rock vs scissor ->rock wins
paper vs scissor ->scissor wins

'''

while True:
    ccount=0
    ucount=0
    uc=int(input('''
Game start.....
1 Yes
2 No | Exit
    
    '''))
    if uc==1:
        for a in range (1,6):
            userInput=int(input('''
1 Rock
2 Scissor
3 Paper
            
            '''))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="scissor"
            elif userInput==3:
                uchoice="paper"
            Cchoice=random.choice(l)
            if  Cchoice==uchoice:
                print("computer value",Cchoice)
                print("user value",uchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice == "rock" and Cchoice == "scissor") or (uchoice=="paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="paper"):
    
                print("computer value",Cchoice)
                print("user value",uchoice)
                print("you win")
                ucount=ucount+1
            else:
                print("computer value",Cchoice)
                print("user value",uchoice)
                print("computer win")
                ccount=ccount+1 
        
        
        if  ucount==ccount:
            print("final game draw....")
            print("user score",ucount)
            print("computer score",ccount)
        elif ucount>ccount: 
            print("final you win the game....")
            print("user score",ucount)
            print("computer score",ccount)
        else:
             print("final computer win the game....")
             print("user score",ucount)
             print("computer score",ccount)
             

    else:
        break