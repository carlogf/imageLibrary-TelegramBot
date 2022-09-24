# imageLibrary-TelegramBot

This is a telegram bot I wrote to use in our friend group chat. Its intended function is to save images as requested by the users and send them back later.

It stores the images using the telegram image_id on a csv file. It has 3 basic commands

- Meme: Sends a random meme from the database. Can be used either with an id to send a specific image or with a hashtang and it sends a random image from the images that have that hashtag

- Save: Save the last image sent to the database. May be used with hashtags

- Hashtag: Adds hashtags to the last image sent.


To use the bot you need to create your own telegram bot using the telegram Bot Father and copy and paste your token in the token.txt file.
