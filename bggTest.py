import requests, bs4, re, webbrowser, sys, pyperclip
"""
# Fetch the site.
bggReq = requests.get('https://boardgamegeek.com/geeklist/164572/card-sleeve-sizes-games?titlesonly=1')
bggReq.raise_for_status()

print('Site fetched')

# Make the soup.
bggSoup = bs4.BeautifulSoup(bggReq.text, "html.parser")

print('Made the soup')
"""

gameList = []
urlList = []

def searchPage(page):
    """
    searchPage() takes in an integer (page number) and searches that page and
    appends the information to the global lists, gameList and urlList.
    """
    # Fetch the site.
    bggReq = requests.get('https://boardgamegeek.com/geeklist/164572/card-sleeve-sizes-games/page/'+str(page)+'?titlesonly=1')
    bggReq.raise_for_status()

    print('Site fetched')

    # Make the soup.
    bggSoup = bs4.BeautifulSoup(bggReq.text, "html.parser")

    print('Made the soup for page ' + str(page))

    # Find all game names
    rawGameList = bggSoup.findAll('a', {'href': re.compile('^/boardgame/')})

    for game in range(50, len(rawGameList)):
        gameList.append(rawGameList[game].getText())
        tmp = rawGameList[game].previousSibling.previousSibling.attrs
        tmp1 = list(tmp.values())
        urlList.append(str(tmp1).strip("'[]"))

def findNumSleeves(url):
    """
    findNumSleeves() takes in a url (found by calling gameDict[<gameName>])
    and returns the sleeving info (sizes and number of sleeves).
    """
    # Open the url for game's page.
    gameReq = requests.get('https://boardgamegeek.com' + str(url))
    gameReq.raise_for_status()

    # Make game page soup
    gameSoup = bs4.BeautifulSoup(gameReq.text, "html.parser")

    print('Made soup for game.')
    
    webbrowser.open('https://boardgamegeek.com'+str(url))
    """
    itemNum = url[-11:]

    div = gameSoup.find('dl', {'id': 'body_list'+itemNum})
    dblRight = gameSoup.findChild('dd', {'class': 'doubleright'})
    div.findChild

    # TODO: A child of dblRight should be a <b></b> tag with the number of cards
    """
    
# Call searchPage for all (12) pages:
for pageNum in range(1,13):
    searchPage(pageNum)

#searchPage(1)

# Create a dictionary, mapping the game titles to their sleeving page url.
gameDict = dict(zip(gameList, urlList))

# Read in sysargv or paste from clipboard for the search.
if len(sys.argv) > 1:
    # Get address from command line.
    gameSearch = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    gameSearch = pyperclip.paste()

findNumSleeves(gameDict[gameSearch])
