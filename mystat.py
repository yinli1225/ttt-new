#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%
folder="./static/"

def update_pic():

    stats = pd.read_csv("./game_stats.csv")
    winner = stats["Winner"]
    stats[["Winner","Winner Type"]]
    #%%
    stats["Winner"] != "Draw"
    #%%
    stats[stats["Winner"]!= "Draw"]

    #%%

    stats[stats["Winner Name"] == "Mary"]

    #%%

    # totoal num of games
    stats["Game ID"].count()

    #%%

    # winning count
    stats["Winner Name"].value_counts()

    #%%

    rankings = pd. DataFrame(columns=[
        "Player Name",
        "Games",
        "Wins",
        "Draws",
        "Winning Rate"
    ])
    rankings

    #%%

    stats

    #%%

    stats[["Winner Name","Winner Type"]].groupby("Winner Type").count()

    #%%

    # games count by player， winning rate
    all_names = pd.concat([stats["Player 1"], stats["Player 2"]], ignore_index=True).unique().tolist()
    rankings["Player Name"] = all_names
    rankings["Games"] = [((stats["Player 1"] == name) | (stats["Player 2"] == name)).sum() for name in all_names]
    rankings["Wins"] = [(stats["Winner Name"] == name).sum() for name in all_names]
    draw_games = stats[stats["Winner"] == "Draw"]
    rankings["Draws"] = [((draw_games["Player 1"] == name) | (draw_games["Player 2"] == name)).sum() for name in all_names]
    rankings["Winning Rate"] = rankings["Wins"] / rankings["Games"]
    rankings

    #%%

    # Pie chart:
    labels = 'Bot', 'Human'
    botwin=rankings[rankings["Player Name"]=="Bot"]["Wins"].to_list()[0]
    humanwin=rankings[rankings["Player Name"]=="Bot"]["Games"]-rankings[rankings["Player Name"]=="Bot"]["Wins"]-rankings[rankings["Player Name"]=="Bot"]["Draws"]
    humanwin=humanwin.to_list()[0]
    sizes = [botwin, humanwin]
    explode = (0, 0)  # no"explode"

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title('Human vs. Bot Wins')
    plt.savefig(folder+"img1.png")
    plt.show()

    #%%

    plt.rcdefaults()
    fig, ax = plt.subplots()
    player=rankings["Player Name"].to_list()
    #player = ('Bot', 'Bot 2', 'Mary', 'David')
    wins=rankings["Wins"].to_list()
    #wins = (8,4,3,2)

    ax.barh(y_pos, wins, align='center')
    ax.set_yticks(y_pos, labels=player)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Wins')
    ax.set_title('Winner Ranking')

    plt.show()

    #%%

    stats.plot.scatter(x = "Game ID", y = "Moves")


if __name__ == "__main__":
    update_pic()


