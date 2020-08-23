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

def p1_pokemon():
    chosen_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(p1_pokemon_name)
    chosen_response = requests.get(chosen_url)
    chosen_pokemon_info = chosen_response.json()

    return {
        'name': chosen_pokemon_info['name'],
        'id': chosen_pokemon_info['id'],
        'height': chosen_pokemon_info['height'],
        'weight': chosen_pokemon_info['weight'],
    }

def p2_pokemon():
    chosen_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(p2_pokemon_name)
    chosen_response = requests.get(chosen_url)
    chosen_pokemon_info = chosen_response.json()

    return {
        'name': chosen_pokemon_info['name'],
        'id': chosen_pokemon_info['id'],
        'height': chosen_pokemon_info['height'],
        'weight': chosen_pokemon_info['weight'],
    }
opponent_pokemon = random_pokemon()

pokemon_hand1 = []
for _ in range(5):
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    pokemon_hand1.append(pokemon['name'])

pokemon_hand2 = []
for _ in range(5):
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    pokemon_hand2.append(pokemon['name'])

print("Welcome to Top Trumps- Pokemon style.")
player_mode = input("Would you like to play singleplayer or multiplayer mode?")
print("You have selected {} mode".format(player_mode))

if player_mode == "singleplayer":
    print("CHOOSE YOUR FIGHTER. You have been given:")
    print(*pokemon_hand1, sep="\n")

    while 1:
        my_pokemon_name = input("Which Pokemon would you like to select?")

        if my_pokemon_name in pokemon_hand1:
            my_pokemon = chosen_pokemon()
            print("Great,you have chosen: {}".format(my_pokemon_name))
            break
        else:
            print("Sorry, that pokemon is not an option, please choose another!")
=======
my_score = 0
computer_score = 0

stat_options = ["id","height","weight"]

for games in range(5):

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
    print(*pokemon_hand1, sep="\n") 
    
    while 1:
        p1_pokemon_name = input("Which Pokemon would you like to select?")

        if p1_pokemon_name in pokemon_hand1:
            p1_pokemon = p1_pokemon()
            print("Great, you have chosen: {}".format(p1_pokemon_name))
            break
        else:
            print("Sorry, that pokemon is not an option, please choose another!")
            
    print("{} CHOOSE YOUR FIGHTER. You have been given:" .format(p2_name.upper()))
    print(*pokemon_hand2, sep="\n")
    
    while 1:
        p2_pokemon_name = input("Which Pokemon would you like to select?")

        if p2_pokemon_name == p1_pokemon:
            print("Sorry, that pokemon is not an option, please choose another!")
            break
        elif p2_pokemon_name in pokemon_hand2:
            p2_pokemon = p2_pokemon()
            print("Great, you have chosen: {}".format(p2_pokemon_name))
            break
        else:
            print("Sorry, that pokemon is not an option, please choose another!")


    stat_choices = ['id', 'height', 'weight']
    ran_stat_choice = stat_choices[random.randint(0,2)]
    print('The stat chosen to compete is: {}'.format(ran_stat_choice))
=======
    while 1:
        my_pokemon_name = input("Which Pokemon would you like to select?")

        if my_pokemon_name in pokemon_hand:
            my_pokemon = chosen_pokemon()
            print("Great,you have chosen: {}".format(my_pokemon_name))
            break
        else:
            print("Sorry, that pokemon is not an option, please choose another!")


    print('The opponent chose {}'.format(opponent_pokemon['name']))

    while 1:
        stat_choice = input("Which stat would you like to use? (id,height,weight)")

        if stat_choice in stat_options:
            my_stat = my_pokemon[stat_choice]
            opponent_stat = opponent_pokemon[stat_choice]
            break
        else:
            print("Sorry, that pokemon is not an option, please choose another!")



    if my_stat > opponent_stat:
        my_score+=1
        print("You Win this round! The opponents {} is {} but your's is {}.".format(stat_choice,opponent_stat,my_stat))
    elif my_stat < opponent_stat:
        computer_score+=1
        print("You Lose this round! The opponents {} is {} but your's is {}.".format(stat_choice,opponent_stat,my_stat))
    else:
        print("It's a draw! Both you and the opponent have a {} of {}.".format(stat_choice,my_stat))

    print("The overall scores are \n You: {} Opponent: {}".format(my_score,computer_score))

if my_score > computer_score:
    print("Congratulations you won!!! In the end you scored {} and your opponent scored {}".format(my_score,computer_score))
elif my_score < computer_score:
    print("Sorry, you lost!!! In the end you scored {} and your opponent scored {}. Better luck next time!".format(my_score,computer_score))


    p1_stat = p1_pokemon[ran_stat_choice]
    p2_stat = p2_pokemon[ran_stat_choice]

    if p1_stat > p2_stat:
        print("{} wins this round! {}'s {} is {} and {}'s is {}.".format(p1_name,p1_name,ran_stat_choice,p1_stat,p2_name,p2_stat))
    elif p1_stat < p2_stat:
        print("{} wins this round! {}'s {} is {} and {}'s is {}.".format(p2_name,p2_name,ran_stat_choice,p2_stat,p1_name,p1_stat))
    else:
        print("It's a draw! Both {} and the {} have a {} of {}.".format(p1_name, p2_name,ran_stat_choice,p1_stat))

advance = input("Would you like to continue to the next round? (y/n")
if advance == 'y':
    print('next round loading...')
else:
    print('You have finished the game. Thank you for playing.')