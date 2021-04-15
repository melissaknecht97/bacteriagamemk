# Mafia (or Werewolf)

Home screen:

<img src="https://raw.githubusercontent.com/aok1425/mafia-werewolf/master/static/images/start.png" width="200">

From player's point-of-view:

<img src="https://raw.githubusercontent.com/aok1425/mafia-werewolf/master/static/images/user-00.png" width="200">
<img src="https://raw.githubusercontent.com/aok1425/mafia-werewolf/master/static/images/user-1.png" width="200">
<img src="https://raw.githubusercontent.com/aok1425/mafia-werewolf/master/static/images/user-2.png" width="200">
<img src="https://raw.githubusercontent.com/aok1425/mafia-werewolf/master/static/images/user-3.png" width="200">

From narrator's point-of-view:

<img src="https://raw.githubusercontent.com/aok1425/mafia-werewolf/master/static/images/host-00.png" width="200">
<img src="https://raw.githubusercontent.com/aok1425/mafia-werewolf/master/static/images/host-1.png" width="200">
<img src="https://raw.githubusercontent.com/aok1425/mafia-werewolf/master/static/images/host-2.png" width="200">

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/aok1425/mafia-werewolf)

This webapp facilitates player sign-up and role distribution. An added benefit is that players can secretly choose the role they want.

## How to use:
With one player per device, have each player and the narrator visit [mafiaalex.herokuapp.com](http://mafiaalex.herokuapp.com). The narrator creates a game, then waits for all players to sign up.

The player chooses the game, inputs his or her name, then waits for everyone else to sign up. 

The narrator chooses the number of mafia, sheriffs, and angels, then presses Assign Roles.

The player presses View Role, and sees his or her identity.

## More details:

* When the narrator views players, those who have signed up in the past 1.5 hours are shown.

## Next steps:
* If narrator says player is not playing, have that player removed from player waiting screen as well.
* Set smart defaults for number of special characters, not just the left choice.
* Make the preferred role form box on the sign in page conform to Bootstrap specifications.
* Allow voting via the webapp? Have a timer on the webapp for each round?
* Write formal tests in Flask. Possible tests are: many players signing up for the same role; what happens after a round; multiple players with same name.