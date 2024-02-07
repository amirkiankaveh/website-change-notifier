# Website Change Notifire on Telegram

this is for when you whant to be notified, as soon as some part of a website changes.
you will give this app a URL to listen and a CSS selector to check for changes.
and if anything happend it will notify all members of your telegram bot, channel or group.


- before all this, you should make a Telegram bot with @BotFather in telegram. get your API token and then...

## install:

1. first install python 3.11.
2. clone this repo
```
git clone https://github.com/Lord-A2K/website-change-notifier.git
```
3. install poetry and then installing project.
```
pip install poetry

poetry install
```

## setup and configuration:

check **.env.example** for the environment variables that you can set.
just make a **.env** file with your data or set variables manualy.

or just simply change **src/config.py** file.

## run:

enter this command:
```
poetry run start
```
