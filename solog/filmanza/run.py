from solog.filmanza.loginout import displayMenu, logout
from solog.filmanza.game_rules import game_rules
from solog.filmanza.game_over import game_over
from solog.filmanza.Body import print_body
from solog.filmanza.menu import menu

h=3
score=0
users = {}

def run():
    print_body()
    displayMenu()
    game_rules()
    menu()
    log_out()
