import requests
from bs4 import BeautifulSoup
import pandas as pd


def batting_card(innings):
    batsmen_df = pd.DataFrame(columns=["Name", "Description", "Runs", "Balls", "4s", "6s", "SR"])
    board = []
    for texts in innings:
        board.append(texts.get_text())

    for element in board:
        element = element.strip()
        element = element.replace("  ", "\t")
        element = element.replace("\t\t", "\t")
        player_stats = element.split("\t")
        player_name = player_stats[0]
        if player_name == "Extras" or player_name == "Total" or player_name == "Yet to Bat" or player_name == "Did not Bat":
            continue

        player_desc = player_stats[1]
        player_boundary = player_stats[2].split(" ")
        batsmen_df = batsmen_df.append(
            {"Name": player_name, "Description": player_desc, "Runs": player_boundary[0], "Balls": player_boundary[1],
             "4s": player_boundary[2], "6s": player_boundary[3], "SR": player_boundary[4]}, ignore_index=True)

    return batsmen_df


def bowling_card(innings):
    bowler_df = pd.DataFrame(columns=["Bowler", "Over", "Maiden", "Runs", "Wickets", "NB", "WD", "ECO"])
    board = []
    for texts in innings:
        board.append(texts.get_text())

    for element in board:
        element = element.strip()
        player_name = element.split("  ")[0]
        player_stats = element.split("  ")[1]
        player_stat = player_stats.strip().split(" ")
        bowler_df = bowler_df.append(
            {"Bowler": player_name, "Over": player_stat[0], "Maiden": player_stat[1], "Runs": player_stat[2],
             "Wickets": player_stat[3], "NB": player_stat[4], "WD": player_stat[5], "ECO": player_stat[6]},
            ignore_index=True)

    return bowler_df

with open('cricLink.txt', 'r') as f:
    URL = f.readline()

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

page = requests.get(URL)

soup = BeautifulSoup(page.text, 'lxml')

matchResult = soup.select('.cb-scrcrd-status')

# for texts in matchResult:
#   print(texts.text)

inningsHighlight = soup.select('.cb-scrd-hdr-rw')

# scorecard = soup.select('.cb-ltst-wgt-hdr')
for texts in matchResult:
    print(texts.text)

Inning_score = []
for texts in inningsHighlight:
    Inning_score.append(texts.text)

Innings1 = soup.find('div', id="innings_1")

if Innings1:
    Inning1 = soup.find_all('div', id="innings_1")[0]

    Inning1_batting = Inning1.find_all('div', class_="cb-col cb-col-100 cb-ltst-wgt-hdr")[0]
    Inning1_bowling = Inning1.find_all('div', class_="cb-col cb-col-100 cb-ltst-wgt-hdr")[1]
    Inning1_batting = Inning1_batting.find_all('div', class_="cb-col cb-col-100 cb-scrd-itms")
    Inning1_bowling = Inning1_bowling.find_all('div', class_="cb-col cb-col-100 cb-scrd-itms")

    batting_df = batting_card(Inning1_batting)
    bowling_df = bowling_card(Inning1_bowling)
    print(Inning_score[0])
    print(batting_df)
    print(bowling_df)

Innings2 = soup.find('div', id="innings_2")
if Innings2:
    Inning2 = soup.find_all('div', id="innings_2")[0]
    Inning2_batting = Inning2.find_all('div', class_="cb-col cb-col-100 cb-ltst-wgt-hdr")[0]
    Inning2_bowling = Inning2.find_all('div', class_="cb-col cb-col-100 cb-ltst-wgt-hdr")[1]
    Inning2_batting = Inning2_batting.find_all('div', class_="cb-col cb-col-100 cb-scrd-itms")
    Inning2_bowling = Inning2_bowling.find_all('div', class_="cb-col cb-col-100 cb-scrd-itms")
    batting_df = batting_card(Inning2_batting)
    bowling_df = bowling_card(Inning2_bowling)
    print(Inning_score[1])
    print(batting_df)
    print(bowling_df)

Innings3 = soup.find('div', id="innings_3")
if Innings3:
    Inning3 = soup.find_all('div', id="innings_3")[0]
    Inning3_batting = Inning3.find_all('div', class_="cb-col cb-col-100 cb-ltst-wgt-hdr")[0]
    Inning3_bowling = Inning3.find_all('div', class_="cb-col cb-col-100 cb-ltst-wgt-hdr")[1]
    Inning3_batting = Inning3_batting.find_all('div', class_="cb-col cb-col-100 cb-scrd-itms")
    Inning3_bowling = Inning3_bowling.find_all('div', class_="cb-col cb-col-100 cb-scrd-itms")
    batting_df = batting_card(Inning3_batting)
    bowling_df = bowling_card(Inning3_bowling)
    print(Inning_score[2])
    print(batting_df)
    print(bowling_df)

Innings4 = soup.find('div', id="innings_4")
if Innings4:
    Inning4 = soup.find_all('div', id="innings_4")[0]
    Inning4_batting = Inning4.find_all('div', class_="cb-col cb-col-100 cb-ltst-wgt-hdr")[0]
    Inning4_bowling = Inning4.find_all('div', class_="cb-col cb-col-100 cb-ltst-wgt-hdr")[1]
    Inning4_batting = Inning4_batting.find_all('div', class_="cb-col cb-col-100 cb-scrd-itms")
    Inning4_bowling = Inning4_bowling.find_all('div', class_="cb-col cb-col-100 cb-scrd-itms")
    batting_df = batting_card(Inning4_batting)
    bowling_df = bowling_card(Inning4_bowling)
    print(Inning_score[3])
    print(batting_df)
    print(bowling_df)

scorecard = soup.select('.cb-scrd-itms')
