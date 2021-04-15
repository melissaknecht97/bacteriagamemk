from test import create_players

number_players = {
	"Human": 2,
	"Bacteria": 4,
	"Immune System": 3,
	"Antibody": 0,
	"Doesn't Matter": 7}

players = {}

# making the player names
for role in number_players:
	if not role in players:
		players[role] = []
	for i in range(1, number_players[role] + 1):
		players[role].append(role[0].lower() + str(i))

create_players(players, url="mafiaalex.herokuapp.com")
