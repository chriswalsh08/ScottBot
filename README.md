![ScottBot](https://sites.psu.edu/littlepassion/files/2018/11/6357600113572837231773916132_michael-scott-s-top-tantrums-25dfult.jpg)
# ScottBot
A Discord bot created using discord.py rewrite. This bot was created simply as a side project for my resume, to familiarize myself with the discord.py package and object-oriented programming in Python, and to create a cool 'toy' for my Discord server. There are 'responses' that the bot says to certain things that my friends and I say a lot in Discord. These are
## Commands
* **.help**: shows the custom help command with a list of all of Scottbot's commands.
### Moderation
* **.ban**: takes in user and reason arguments and bans the mentioned guild member from the server indefinitely.
* **.kick**: takes in user and reason arguments and kicks the mentioned guild member from the server, thus allowing them to rejoin with a new invite.
* **.changepreset**: takes in a command preset argument. Changes the command preset for Scottbot from the default value of '.'
### Fun
* **.compliment**: takes in user argument and sends the mentioned user a nice compliment :)
* **.insult**: takes in user argument and sends the mentioned user a mean insult :(
* **.animalfact**: takes in animal argument from a preset list (dog, cat, bird, koala, fox, panda) and sends a random fact and image of the animal.
* **.conch**: ask the Almighty Conch a question! Takes in a question argument.
### Gambling
* **.coinflip**: flip a coin!
* **.roll**: takes in a dice argument. This command needs work. It works with 1d4, 1d6, 1d8, 1d10, 1d20, and 1d100. Need to implement NdN format in the future.
## Importance of Files
* **Cogs** folder: holds the __pycache__ and cog.py files for each of the fun, gambling, and moderation cogs.
* **gifs** folder: holds the gifs that Scottbot responds to certain user messages with.
* **Procfile**: Used for deploying bot to Heroku
* **bot.py**: Main bot file
* **prefixes.json**: Necessary for holding a list of the bot's custom prefixes throughout servers
* **requirements.txt**: used by Heroku to download Python packages necessary to run the bot
## To-do List
* **Music**: In the future given more time, I would like to implement features that allow Scottbot to enter a voice channel and play linked YouTube videos or Spotify playlists so users could listen to music with it.
* **Level System**: Additionally, I'd like to add levels per user based on the amount of messages they send in the server.
* **Steam Price Scraper**: Finally, I want to add an API call that allows the bot to pull prices of Steam games and post it in chat when commanded.
