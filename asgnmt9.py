from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

csvFile = open("lol_champs.csv", "w")
c = csv.writer(csvFile)
c.writerow(["Name", "Health", "Health Regeneration", "Attack Damage", "Attack Speed", "Armor", "Magic Resistance", "Movement Speed"])

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://na.leagueoflegends.com/en/game-info/champions/")
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "champ-name")))
html = driver.page_source
bsObj = BeautifulSoup(html, "html.parser")
champion_list = []

def get_champion_pages(bsObj):
    champion_links = bsObj.findAll("div", {"class":"champ-name"})
    for link in champion_links:
        champ = link.find("a")["href"]
        champion_list.append(champ)

def get_champion_details(champion_list):
    for i in champion_list:
        champ_url = "https://na.leagueoflegends.com/en/game-info/champions/" + i
        driver.get(champ_url)
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[class='skins']")))
        html = driver.page_source
        bsObj = BeautifulSoup(html, "html.parser")
        name = bsObj.find("h1", {"class":"dd-auto-set"}).get_text() + " " + bsObj.find("h3").get_text()
        hp = bsObj.find("span", {"class":"stat-hp"}).find_next_sibling("span", {"class":"stat-value"}).get_text()
        hp_rgn = bsObj.find("span", {"class":"stat-hp-regen"}).find_next_sibling("span", {"class":"stat-value"}).get_text()
        atk_dmg = bsObj.find("span", {"class":"stat-ad"}).find_next_sibling("span", {"class":"stat-value"}).get_text()
        atk_spd = bsObj.find("span", {"class":"stat-as"}).find_next_sibling("span", {"class":"stat-value"}).get_text()
        armor = bsObj.find("span", {"class":"stat-armor"}).find_next_sibling("span", {"class":"stat-value"}).get_text()
        mg_resist = bsObj.find("span", {"class":"stat-mr"}).find_next_sibling("span", {"class":"stat-value"}).get_text()
        mvmnt_spd = bsObj.find("span", {"class":"stat-ms"}).find_next_sibling("span", {"class":"stat-value"}).get_text()
        champ_info = [name, hp, hp_rgn, atk_dmg, atk_spd, armor, mg_resist, mvmnt_spd]
        champion = []
        for info in champ_info:
            try:
                champion.append(info)
            except:
                champion.append("None")
        c.writerow(champion)
        time.sleep(1)

get_champion_pages(bsObj)
get_champion_details(champion_list)
csvfile.close()
driver.quit()
