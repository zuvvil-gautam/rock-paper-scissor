import random

def rockpaperscissor(computer,player):
    if computer == player:
        return None
    elif computer == 'rock' and player == 'paper':
        return True
    elif computer == 'scissor' and player == 'rock':
        return True
    elif computer == 'paper' and player == 'scissor':
        return True
    else:
        return False

while True:
    choice=('rock','paper','scissor')
    computer=random.randint(0,2)
    computer=choice[computer]
    player = None

    while player not in choice:
        player=input('Choose either rock, paper or scissor: ')
    win=rockpaperscissor(computer,player)
    print(f"Computer: {computer}\nPlayer: {player}")
    if win is None:
        print('Tie!')
    elif win:
        print('You win')
    else:
        print('You lose')

    play_again=input("Wanna Play again? (yes/no): ").lower()

    if play_again != 'yes':
        break
print('Bye Bye!!')