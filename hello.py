import random

import requests

def chosen_pokemon():
    chosen_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(my_pokemon_name)
    chosen_response = requests.get(chosen_url)
    chosen_pokemon_info = chosen_response.json()

    return {
        'name': chosen_pokemon_info['name'],
        'id': chosen_pokemon_info['id'],
        'height': chosen_pokemon_info['height'],
        'weight': chosen_pokemon_info['weight'],
    }

def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],    
    }

opponent_pokemon = random_pokemon()

pokemon_hand = []
for _ in range(5):
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    pokemon_hand.append(pokemon['name'])

print("CHOOSE YOUR FIGHTER. You have been given:")
print(*pokemon_hand, sep="\n")

while 1:
    my_pokemon_name = input("Which Pokemon would you like to select?")

    if my_pokemon_name in pokemon_hand:
        my_pokemon = chosen_pokemon()
        print("Great,you have chosen: {}".format(my_pokemon_name))
        break
    else:
        print("Sorry, that pokemon is not an option, please choose another!")


print('The opponent chose {}'.format(opponent_pokemon['name']))

stat_choice = input("Which stat would you like to use? (id,height,weight)")

my_stat = my_pokemon[stat_choice]
opponent_stat = opponent_pokemon[stat_choice]

if my_stat > opponent_stat:
    print("You Win! The opponents {} is {} but your's is {}.".format(stat_choice,opponent_stat,my_stat))
elif my_stat < opponent_stat:
    print("You Lose! The opponents {} is {} but your's is {}.".format(stat_choice,opponent_stat,my_stat))
else:
    print("It's a draw! Both you and the opponent have a {} of {}.".format(stat_choice,my_stat))

