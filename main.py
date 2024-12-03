# -*- coding: utf-8 -*-

template = [
    '''
It was about {number} {time_measure} ago when I arrived at the hospital in a {transportation}. 
The hospital is a/an {adjective1} place, there are a lot of {adjective2} {noun1} here. 
There are nurses here who have {color} {body_part}. If someone wants to come into my room I told them that they have to {verb} first. 
I’ve decorated my room with {number2} {noun2}. Today I talked to a doctor and they were wearing a {noun3} on their {body_part2}. 
I heard that all doctors {verb2} {noun4} every day for breakfast. The most {adjective3} thing about being in the hospital is the {silly_word} {noun5} !
''',
    '''
This weekend I am going camping with {person_name}. I packed my lantern, sleeping bag, and {noun1}. I am so {feeling1} to {verb1} in a tent. I am {feeling2}
we might see a(n) {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb2}. I have heard that the {color} lake is great for {action_verb}. 
Then we will {adverb} hike through the forest for {number} {time_measure}.
If I see a {color_animal} {animal2} while hiking, I am going to bring it home as a pet! At night we will tell {number3} {silly_word} stories and roast {noun2} around the campfire!!!
''',
    '''
Dear {person_name}, I am writing to you from a {adjective1} castle in an enchanted forest. I found myself here one day after going for a ride on a {color_animal} {animal} in {place}.
There are {adjective2} {magical_creature1} and {adjective3} {magical_creature2} here! In the {room} there is a pool full of {noun1}.
I fall asleep each night on a {noun2} of {noun3} and dream of {adjective4} {noun4}. It feels as though I have lived here for {number} {time_measure}.
I hope one day you can visit, although the only way to get here now is {verb_ending} on a {adjective5} {noun5}!!
'''
]

def get_int_input(prompt, error_message="Invalid input, please enter a valid number:"):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_message)

def get_non_empty_input(prompt, error_message="Input cannot be empty. Please try again: "):
    while True:
        user_input = input(prompt)
        if user_input.strip():
            return user_input
        else:
            print(error_message)


def hospital_story():
    
    number = get_int_input("Enter a number: ")
    time_measure = get_non_empty_input("Enter a measure of time (e.g., days, hours): ")
    transportation = get_non_empty_input("Enter a mode of transportation: ")
    adjective1 = get_non_empty_input("Enter an adjective: ")
    adjective2 = get_non_empty_input("Enter another adjective: ")
    noun1 = get_non_empty_input("Enter a noun: ")
    color = get_non_empty_input("Enter a color: ")
    body_part = get_non_empty_input("Enter a part of the body: ")
    verb = get_non_empty_input("Enter a verb: ")
    number2 = get_int_input("Enter another number: ")
    noun2 = get_non_empty_input("Enter a noun: ")
    noun3 = get_non_empty_input("Enter a noun: ")
    body_part2 = get_non_empty_input("Enter another part of the body: ")
    verb2 = get_non_empty_input("Enter a verb: ")
    noun4 = get_non_empty_input("Enter a noun: ")
    adjective3 = get_non_empty_input("Enter an adjective: ")
    silly_word = get_non_empty_input("Enter a silly word: ")
    noun5 = get_non_empty_input("Enter a noun: ")

  
    story = template[0].format(
        number=number, time_measure=time_measure, transportation=transportation, adjective1=adjective1,
        adjective2=adjective2, noun1=noun1, color=color, body_part=body_part, verb=verb, number2=number2,
        noun2=noun2, noun3=noun3, body_part2=body_part2, verb2=verb2, noun4=noun4, adjective3=adjective3,
        silly_word=silly_word, noun5=noun5
    )
    print(story)

def camping_story():
  
    person_name = get_non_empty_input("Enter a person's name: ")
    noun1 = get_non_empty_input("Enter a noun (e.g., stick, map): ")
    feeling1 = get_non_empty_input("Enter an adjective (feeling) for excitement: ")
    verb1 = get_non_empty_input("Enter a verb (action): ")
    feeling2 = get_non_empty_input("Enter an adjective (feeling) for concern: ")
    animal = get_non_empty_input("Enter an animal: ")
    verb2 = get_non_empty_input("Enter a verb (action): ")
    color = get_non_empty_input("Enter a color: ")
    action_verb = get_non_empty_input("Enter a verb ending in 'ing' (e.g., swimming): ")
    adverb = get_non_empty_input("Enter an adverb (ending in -ly): ")
    number = get_int_input("Enter a number: ")
    time_measure = get_non_empty_input("Enter a measure of time (e.g., days, hours): ")
    color_animal = get_non_empty_input("Enter a color: ")
    animal2 = get_non_empty_input("Enter an animal: ")
    number3 = get_int_input("Enter a number: ")
    silly_word = get_non_empty_input("Enter a silly word: ")
    noun2 = get_non_empty_input("Enter a noun (e.g., marshmallow): ")


    story = template[1].format(
        person_name=person_name, noun1=noun1, feeling1=feeling1, verb1=verb1,
        feeling2=feeling2, animal=animal, verb2=verb2, color=color,
        action_verb=action_verb, adverb=adverb, number=number, time_measure=time_measure,
        color_animal=color_animal, animal2=animal2, number3=number3,
        silly_word=silly_word, noun2=noun2
    )
    print(story)

def enchanted_castle_story():

    person_name = get_non_empty_input("Enter a person's name: ")
    adjective1 = get_non_empty_input("Enter an adjective: ")
    color_animal = get_non_empty_input("Enter a color: ")
    animal = get_non_empty_input("Enter an animal: ")
    place = get_non_empty_input("Enter a place (e.g., forest, mountain): ")
    adjective2 = get_non_empty_input("Enter an adjective: ")
    magical_creature1 = get_non_empty_input("Enter a magical creature (plural): ")
    adjective3 = get_non_empty_input("Enter another adjective: ")
    magical_creature2 = get_non_empty_input("Enter another magical creature (plural): ")
    room = get_non_empty_input("Enter a room in a house: ")
    noun1 = get_non_empty_input("Enter a noun: ")
    noun2 = get_non_empty_input("Enter a noun: ")
    noun3 = get_non_empty_input("Enter a plural noun: ")
    adjective4 = get_non_empty_input("Enter an adjective: ")
    noun4 = get_non_empty_input("Enter a plural noun: ")
    number = get_int_input("Enter a number: ")
    time_measure = get_non_empty_input("Enter a measure of time (e.g., days, weeks): ")
    verb_ending = get_non_empty_input("Enter a verb ending in 'ing': ")
    adjective5 = get_non_empty_input("Enter an adjective: ")
    noun5 = get_non_empty_input("Enter a noun: ")
    story = template[2].format(
        person_name=person_name, adjective1=adjective1, color_animal=color_animal,
        animal=animal, place=place, adjective2=adjective2, magical_creature1=magical_creature1,
        adjective3=adjective3, magical_creature2=magical_creature2, room=room, noun1=noun1,
        noun2=noun2, noun3=noun3, adjective4=adjective4, noun4=noun4,
        number=number, time_measure=time_measure, verb_ending=verb_ending,
        adjective5=adjective5, noun5=noun5
    )
    print(story)


chooseNumber = int(input("Enter a template number (1, 2, or 3): "))

if chooseNumber == 1:
    hospital_story()
elif chooseNumber == 2:
    camping_story()
elif chooseNumber == 3:
    enchanted_castle_story()
else:
    print("Invalid number. Please choose 1, 2, or 3.")
