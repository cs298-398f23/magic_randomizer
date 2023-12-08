# magic_randomizer

Group Members:
Seth Coleman
Carl Reyes

Idea: Magic Deck Randomizer

- scryfall api
- basic oauth to save your collection of cards (and maybe decks)

Database
- mongodb
- saves passwords and decks
- hash passwords in database

Front end
- hover over different cards to show image
- importer for cards you own

our api
- GET random deck
- GET saved deck
- POST past random deck

Documentation:
https://scryfall.com/docs/api

- Basic Oauth (might want to wait for monday when coleman goes over it)

How to get Project Running on AWS

1.) Go to EC2 and start an instance
2.) select vockey for security key, put key in .ssh folder if needed
3.) Load start.sh into Advanced/User data to launch on start up
4.) click launch instance
5.) go to Instances dashboard > Security > Security Groups (go to your security group) > Edit Inbound Rules > Add Rule
6.) Fill the values: Type -> Custom TCP, Protocol -> TCP, Port range -> 5000, and save
7.) Clone the project repository.
8.) Create a file named `config.py` inside the root folder.
9.) Open the `config.py` file and enter the following:
```python
SECRET_KEY = ''
```
Placing your secret key inside the quotes.
10.) go to http://<PUBLIC IPV4 ADDRESS>:5000

Source for aws flask fix: https://stackoverflow.com/a/66688430

for friday: presentation level diagram of whole system

