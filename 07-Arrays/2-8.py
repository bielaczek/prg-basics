computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

game = 0
while game < len(computer_games):
    print(computer_games[game])
    game += 1

game = 0
computer_games.sort()

while game < len(computer_games):
    print(f'{game + 1}. {computer_games[game]}')
    game += 1