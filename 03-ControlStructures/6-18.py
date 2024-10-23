interesed = input('SURVEY Are you interested in computer science? (y/n): ')
games = input('Do you like playing computer games? (y/n): ')
instagram = input('Do you have an Instagram account? (y/n): ')

if interesed == 'y':
    print(f'SURVEY RESULTS Interesed in computer science: Yes')
elif interesed == 'n':
    print(f'SURVEY RESULTS Interesed in computer science: No')

if games == 'y':
    print(f'Playing computer games: Yes')
elif games == 'n':
    print(f'Playing computer games: No')

if instagram == 'y':
    print(f'Has an Instagram account: Yes')
elif instagram == 'n':
    print(f'Has an Instagram account: No')