import threading
import time
teams=['BSN', 'CHN', 'CN2', 'PT1', 'SL4', 'NY1', 'PHI', 'BR3', 'PIT', 'BRO', 'CIN', 'SLN', 'BLA', 'BOS', 'CHA', 'CLE', 'DET', 'MLA', 'PHA', 'WS1', 'SLA', 'NYA', 'ML1', 'BAL', 'KC1', 'LAN', 'SFN', 'LAA', 'MIN', 'WS2', 'HOU', 'NYN', 'CAL', 'ATL', 'OAK', 'KCA', 'SE1', 'MON', 'SDN', 'ML4', 'TEX', 'SEA', 'TOR', 'COL', 'FLO', 'ANA', 'TBA', 'ARI', 'MIL', 'WAS', 'MIA']
#teams=['BSN', 'CHN', 'CN2']
#data = pd.read_csv("D:\Python\DE_Path\Data\ecommerce5000.csv", encoding="Latin-1")
#query=data.loc[0:4999,"query"]
#duplicates = []

def task(team):
    time.sleep(3)
    print(team)
    #print('Completed thread 2')

threads = []
for i, team in enumerate(teams):
    thread= threading.Thread(target=task, args=(team,))
    print("Started task {}".format(i))
    thread.start()
    threads.append(thread)


for thread in threads:
    thread.join()


#print(type(teams))
print(teams)