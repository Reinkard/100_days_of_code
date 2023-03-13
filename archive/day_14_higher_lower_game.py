from random import randint
from os import system

instagram_followers = [
    {
        'name': 'Instagram',
        'follower_count': 1537579119,
        'description': 'соціальна мережа',
        'country': 'США'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 336109601,
        'description': 'футболіст',
        'country': 'Португалія'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 270840227,
        'description': 'актор, культурист',
        'country': 'США'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 238679073,
        'description': 'підприємниця, телеведуча',
        'country': 'США'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 221638953,
        'description': 'телеведуча, підприємниця',
        'country': 'США'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 197829011,
        'description': 'футболіст',
        'country': 'Аргентина'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 176401126,
        'description': 'співачка, актриса',
        'country': 'США'
    },
    {
        'name': 'National Geographic',
        'follower_count': 157558617,
        'description': 'журнал про природу та науку',
        'country': 'США'
    },
    {
        'name': 'Neymar Jr.',
        'follower_count': 148941072,
        'description': 'футболіст',
        'country': 'Бразилія'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 140983904,
        'description': 'співак',
        'country': 'Канада'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 136962873,
        'description': 'співачка, актриса',
        'country': 'США'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 132160841,
        'description': 'співачка',
        'country': 'США'
    },
    {
        'name': 'Kylie Cosmetics',
        'follower_count': 127325874,
        'description': 'бренд косметики',
        'country': 'США'
    },
    {   'name': 'Kendall Jenner',
        'follower_count': 117508008,
        'description': 'модель, телеведуча',
        'country': 'США'
    },
    {
        'name': 'Jennifer Lopez',
        'follower_count': 114258833,
        'description': 'співачка, актриса',
        'country': 'США'
    },
    {
        'name': 'Khloé Kardashian',
        'follower_count': 103896667,
        'description': 'телеведуча, підприємниця',
        'country': 'США'
    },
    {
        'name': 'Miley Cyrus',
        'follower_count': 102968444,
        'description': 'співачка, актриса',
        'country': 'США'
    },
    {
        'name': 'Virat Kohli',
        'follower_count': 100636328,
        'description': 'капітан збірної Індії з крикету',
        'country': 'Індія'
    },

    {
        'name': 'Jennifer Aniston',
        'follower_count': 96915928,
        'description': 'актриса',
        'country': 'США'
    },
]

def higher_lower():
    input('Вітаю в грі більше-менше! Натисни Enter, щоб розпочати...')
    system('clear')
    count = 0
    instagram_account_1 = randint(0, len(instagram_followers) - 1)
    play_again = ''
    while True:
        instagram_account_2 = randint(0, len(instagram_followers) - 1)

        while instagram_account_1 == instagram_account_2: # якщо раптом аккаунти будуть одинакові
            instagram_account_2 = randint(0, len(instagram_followers))
        
        a = f"{instagram_followers[instagram_account_1]['name']}, {instagram_followers[instagram_account_1]['description']}, з країни: {instagram_followers[instagram_account_1]['country']}\n"
        b = f"{instagram_followers[instagram_account_2]['name']}, {instagram_followers[instagram_account_2]['description']}, з країни: {instagram_followers[instagram_account_2]['country']}\n"

        player_choice = ''
        while player_choice not in ['A', 'B']:
            player_choice = input(f"{a} vs\n{b}\nУ кого більше підписників? Введи 'А' або 'В': ").upper()
        
        if instagram_followers[instagram_account_1]['follower_count'] > instagram_followers[instagram_account_2]['follower_count'] and player_choice == 'A':
            count += 1
            system('clear')
            print(f"Супер! Рахунок правильних відповідей: {count}")
        elif instagram_followers[instagram_account_1]['follower_count'] < instagram_followers[instagram_account_2]['follower_count'] and player_choice == 'B':
            instagram_account_1 = instagram_account_2
            count += 1
            system('clear')
            print(f"Супер! Рахунок правильних відповідей: {count}")
        else:
            print(f"Ти програв з рахуном {count} балів(")
            while play_again not in ['y', 'n']:
                play_again = input("Зіграємо ще раз? Введи 'y' або 'n': ")
            if play_again == 'y':
                system('clear')
                higher_lower()
            else:
                exit()
        
higher_lower()
