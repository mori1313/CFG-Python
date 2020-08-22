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

print("Welcome to Top Trumps- Pokemon style.")
player_mode = input("Would you like to play singleplayer or multiplayer mode?")
print("You have selected {} mode".format(player_mode))

if player_mode == "singleplayer":
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
else:
    p1_name = input("Player 1, what is your name?")
    p2_name = input("Player 2, what is your name?")
    
    print("{} CHOOSE YOUR FIGHTER. You have been given:" .format(p1_name.upper()))
    print(*pokemon_hand, sep="\n") 
    
    while 1:
        p1_pokemon_name = input("Which Pokemon would you like to select?")

        if p1_pokemon_name in pokemon_hand:
            p1_pokemon = chosen_pokemon()
            print("Great, you have chosen: {}".format(p1_pokemon_name))
            break
        else:
            print("Sorry, that pokemon is not an option, please choose another!")
            
    print("{} CHOOSE YOUR FIGHTER. You have been given:" .format(p2_name.upper()))
    print(*pokemon_hand, sep="\n")
    
    while 1:
        p2_pokemon_name = input("Which Pokemon would you like to select?")

        if p2_pokemon_name == p1_pokemon:
            print("Sorry, that pokemon is not an option, please choose another!")
            break
        elif p2_pokemon_name in pokemon_hand:
            p2_pokemon = chosen_pokemon()
            print("Great, you have chosen: {}".format(p2_pokemon_name))
        else:
            print("Sorry, that pokemon is not an option, please choose another!")


    stat_choice = input("Which stat would you like to compete? (id,height,weight)")

    p1_stat = p1_pokemon[stat_choice]
    p2_stat = p2_pokemon[stat_choice]

    if p1_stat > p2_stat:
        print("{} wins this round! {}'s {} is {} and {}'s is {}.".format(p1_name,p1_name,stat_choice,p1_stat,p2_name,p2_stat))
    elif p1_stat < p2_stat:
        print("{} wins this round! {}'s {} is {} and {}'s is {}.".format(p2_name,p2_name,stat_choice,p2_stat,p1_name,p1_stat))
    else:
        print("It's a draw! Both {} and the {} have a {} of {}.".format(p1_name, p2_name,stat_choice,p1_stat))