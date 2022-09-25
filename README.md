# imageLibrary-TelegramBot

This is a telegram bot I wrote to use in our friend group chat. Its intended function is to save images as requested by the users and send them back later.

It stores the images using the telegram image_id on a csv file. 

The bot has 3 basic commands

- Meme: Sends a random image from the database. Can be used either with an id to send a specific image or with a hashtag and it picks a random image from the images that have that hashtag.

- Save: Saves the last image sent to the database. May be used with hashtags.

- Hashtag: Adds hashtags to the last image sent.


# Setting up

## 1. installing dependencies
Make sure to have Python 3 with pandas and the [python-telegram-bot library](https://github.com/python-telegram-bot/python-telegram-bot).
```
$ pip install python-telegram-bot pandas --upgrade
```
## 2. Create a telegram bot with bot father and get your bot token
[Follow the instructions here to create your own bot and get your bot token](https://core.telegram.org/bots#6-botfather)

Paste your token in the token.txt file.

## 3. Starting up
Start up the bot with
```
$ pithon3 telegramBot.py
```
The bot should be now up and running.
