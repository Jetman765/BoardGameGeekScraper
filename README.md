# BoardGameGeekScraper
This is my first project in python3 after reading Automate the Boring Stuff.

This project will pull the individual URL's from Boardgamegeek's Card Sleeve Sizes for Games geeklist. After scraping all 12 pages of content, it creates a dictionary with the key being the game's title, and the value the game's url. Next you can call findNumSleeves(url) and pass in the url found in the dictionary to pull up that game's entry on your web browser. 

I plan to edit the script so that instead of scraping the content everytime it's run, it will store the information locally. I also would like to have instead of the web browser being opened to the game's page, have the actual number of cards be sent to be stored in a Google sheets document.
