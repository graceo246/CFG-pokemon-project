import random
import requests

def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight']
    }

def game():
    my_pokemon = random_pokemon()
    print('Your pokemon is {}'.format(my_pokemon['name']))
    print('ID: ' + str(my_pokemon['id']))
    print('Height: ' + str(my_pokemon['height']))
    print('Weight: ' + str(my_pokemon['weight']))

    stat_choice = input('Which stat do you want to use? (id, height, weight) ')
    opponent_pokemon = random_pokemon()
    print('Your opponent\'s pokemon is {}'.format(opponent_pokemon['name']))
    print('ID: ' + str(opponent_pokemon['id']))
    print('Height: ' + str(opponent_pokemon['height']))
    print('Weight: ' + str(opponent_pokemon['weight']))

    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]

    if my_stat > opponent_stat:
        print('You Win!')
        return 3
    elif my_stat < opponent_stat:
        print('You Lose!')
        return 0
    else:
        print('Draw!')
        return 1


def replay():
        response = input('Do you want to play another round? (y/n)')
        while response == 'y':
            game()
        if response == 'n':
            print('Thank you for playing!')
        else:
            print('Invalid input. Please enter y or n.')




def tournamentgame():
    score = 0
    for round_num in range(1, 4):
        print("ROUND", round_num)
        result = game()
        score += result
        print("Your current score is " + str(score))

    print("Your final score is " + str(score) + " out of 9")
    if score >= 6:
        print("Congratulations! You won the tournament!")
    elif score <= 3:
        print("Unfortunately! You lost the tournament.")
    else:
        print("It's a tie! The tournament ended in a draw.")

    name = input('Enter your name')
    file = open("score.txt", "a")
    file.write(str(score) + " \t " + name + "\n")
    file.close()

    file = open("score.txt", "r")
    readthefile = file.readlines()
    sortedData = sorted(readthefile, reverse=True)
    print("Tournament leaderboard")
    print("Pos| points |Name")
    for i in range(10):
        print(str(i + 1) + " \t " + str(sortedData[i] ) )



def tournament():
    tournament = input('Do you want to play a 3-round tournament? (y/n) ')
    print('You and your opponent will play 3 rounds, the player with the most points wins!')
    if tournament == 'y':
        tournamentgame()
        replay()
    else:
        print('Thank you for playing!')

def main():
    instruction = (
        'INSTRUCTIONS  \n 1. You will be given a random card with different stats \n 2. You will decide your best stat \n 3. Your opponent will choose a random card \n 4. Both stats will be compared and the card with the highest stat wins'
    )
    print('Welcome to the Pokemon card game!')
    instructions = input('Do you know how to play? (y/n)')

    if instructions == 'y':
        game()
        tournament()
        replay()
    elif instructions == 'n':
        print(instruction)
        response = input('Would you like to open your surprise pokeball? (y/n)')
        if response == 'y':
            game()
            tournament()
            replay()
        else:
            print('Then you must be Team Rocket!')

main()
