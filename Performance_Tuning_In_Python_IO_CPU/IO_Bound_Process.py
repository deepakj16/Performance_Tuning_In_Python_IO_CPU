import pandas as pd
import threading
import time
import multiprocessing

def task(teams):
    time.sleep(3)
    for team in teams:
        print(team)

def task2(teams):
    time.sleep(3)
    for team in teams:
        print('Task 2 Printing' + team)

if __name__ == '__main__':
    import pandas as pd
    import threading
    import time
    import multiprocessing
    teams=['BSN', 'CHN', 'CN2', 'PT1', 'SL4', 'NY1', 'PHI', 'BR3', 'PIT', 'BRO', 'CIN', 'SLN', 'BLA', 'BOS', 'CHA', 'CLE', 'DET', 'MLA', 'PHA', 'WS1', 'SLA', 'NYA', 'ML1', 'BAL', 'KC1', 'LAN', 'SFN', 'LAA', 'MIN', 'WS2', 'HOU', 'NYN', 'CAL', 'ATL', 'OAK', 'KCA', 'SE1', 'MON', 'SDN', 'ML4', 'TEX', 'SEA', 'TOR', 'COL', 'FLO', 'ANA', 'TBA', 'ARI', 'MIL', 'WAS', 'MIA']
    #teams=['BSN', 'CHN', 'CN2']
    data = pd.read_csv("D:\Python\DE_Path\Data\ecommerce5000.csv", encoding="Latin-1")
    query=data.loc[0:4999,"query"]
    duplicates = []


        #print('Completed thread 2')
    '''
    threads = []
    for i, team in enumerate(teams):
        thread= threading.Thread(target=task, args=(team,))
        print("Started task {}".format(i))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    '''

    #print(type(teams))
    #print(teams)

    start = time.time()
    p1 = multiprocessing.Process(target=task, args=(teams,))
    p2 = multiprocessing.Process(target=task2, args=(teams,))
    p1.start()
    p2.start()

    for process in [p1, p2]:
        process.join()

    total = time.time() - start