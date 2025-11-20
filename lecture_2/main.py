from datetime import date

print('Hello, newbie 🤙🏽')
user_name = input('Enter your full name: ')
birth_year_str = input('Enter your birth year: ')
birth_year = int(birth_year_str)
current_age = date.today().year - birth_year


def generate_profile(age: int):
    if 0 <= age < 13:
        return 'Child'
    elif 13 <= age < 20:
        return 'Teenager'
    else:
        return 'Adult'


hobbies = list()
while True:
    user_input = input('Enter a favorite hobby or type \'stop\' to finish: ')
    if user_input.lower() == 'stop':
        break
    hobbies.append(user_input)

life_stage = generate_profile(current_age)
user_profile = {
    "name": user_name,
    "age": current_age,
    "stage": life_stage,
    "hobbies": hobbies
}

print('\n---\nProfile Summary:')
print(f"Name:  {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['stage']}")
if len(user_profile['hobbies']) > 0:
    print(f"Favorite Hobbies ({len(hobbies)}):")
    for hobby in user_profile['hobbies']:
        print(f'- {hobby}')
else:
    print('You didn\'t mention any hobbies.')
print('---')