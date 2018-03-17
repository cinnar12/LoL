#League of Legends Champion Scraper

This is a web scraping program I developed to scrape the list of champions from the multiplayer online battle arena video game [League of Legends](https://play.na.leagueoflegends.com/en_US) for their game stats. I wanted to scrape the health, health regen, attack damage, attack speed, armor, magic resistance and movement speed stats for each playable champion to create a database that would allow players and fans to compare them between champions new and old.

##Steps

First, I installed Selenium and BeautifulSoup onto a virtual environment I created for the program. I imported the libraries and modules that I was needed to use for the program and created a new .csv file for recording the data.

I had to scrape the [champions list page](https://na.leagueoflegends.com/en/game-info/champions/) for the URLs of all the available champions. I realized that all the URLs are the champion names added onto the end of the champions page URL.

Selenium was used to load the pages on the Chrome WebDriver so that the ajax can fill in the empty div with champions and their links and to extract the html with page_source for use with BeautifulSoup. I used the WebDriver Wait commands to wait for all the champion links to load before scraping.
```
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "champ-name")))
```

The program consists of two main functions that I defined:
1. One function extracts the links from the champion list page by finding all the divs containing the links and appending them to a URL list to use for the second function.
2. The second function loads each page with the URL list, scrapes them for information, appends them into a list and writes the list into a .csv file.

##Problems & Solutions

I had problems where my program would scrape before some of the information was finished loading. So I set the wait command to wait for the default backdrop to finish disappearing before getting replaced by another backdrop. I ended up switching to waiting for the skins to appear because one of the champion pages did not have a backdrop for some reason.