import webbrowser
from random import randrange

link_root = 'https://deepdreamgenerator.com/u/349718/account?page='

random_page = str(randrange(1, 92, 1))

link = link_root + random_page

webbrowser.open_new_tab(link)
