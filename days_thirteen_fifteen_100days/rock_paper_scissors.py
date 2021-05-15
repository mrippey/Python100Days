from rps_game_choices import Roll, Player
import random 


def main():
    print_header()
    rolls = build_choices() 
    name = get_player_name()

    p1 = Player(name)
    p2 = Player('computer')
    
    game_loop(p1, p2, rolls)


def print_header():
    print('-------------------------')
    print('         Rock, Paper, Scissors')
    print('-------------------------')
    print()

def build_choices():
    rock = Roll('rock')
    paper = Roll('paper')
    scissors = Roll('scissors')

    rolls = [rock, paper, scissors]

    return rolls
    

def get_player_name():
    game_prompt_for_name = str(input('What is your name? ')).capitalize()
    return game_prompt_for_name


def get_player_choice():
    user_input = input('Do you pick [r]ock, [p]aper, or [s]cissors? ')
    print(user_input)

    if user_input == 'r':
        return Roll('rock')
    elif user_input == 'p':
        return Roll('paper')
    elif user_input == 's':
        return Roll('scissors')
    else:
        print('Sorry your choice was not recongized, exiting...')
    

def game_loop(p1, p2, rolls):
    game_count = 0
    while game_count < 3:

        print(f'1st round {game_count+1}')
        p1_choose = get_player_choice()
        p2_choose = random.choice(rolls)

        print(f'Player 1 chose {p1_choose.name}')
        print(f'Player 2 chose {p2_choose.name}')
        print()

        if p1_choose.name == p2_choose.name:
            print('Both players chose the same object, re-do')
            continue 
        
        p1_wins = p1_choose.which_wins(p2_choose)

        if p1_wins:
            print(f'{p1.name} wins with {p1_choose.name}')

        else:
            print(f'{p2.name} wins with {p2_choose.name}')

        game_count += 1
        

 
if __name__ == '__main__':
    main()
