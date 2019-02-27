<<<<<<< HEAD
Parse project created to parse games from Google play store


You will have to install requests, BeautifulSoup (and django, django rest framework to use in web) in order to use in
Project uses python 3

You can user parse.py on its own, the data will be printed to the terminal
you can also use in browser

standalone use:
Create parses instance with desirable url('https://play.google.com/store/apps/category/GAME')
use parser instance to parse and print results
parser_instance.parse()
parser_instance.print_games()

for web usrls are:
test/html/ for html representation

to use search add a query parameter to the url in this format:
 
test/html/?search={one or more keywords separated by space}
=======
