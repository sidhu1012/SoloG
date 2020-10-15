from .loginout import displayMenu, logout
from .game_rules import game_rules
from .game_over import game_over
from .body import print_body
from .menu import menu

h=3
score=0

def run():
    print_body()
    game_rules()
    displayMenu()
    menu()
    log_out()
