
if __name__ == '__main__':
    from multiprocessing import Pool
    from Python_Classics import Pandas as pd
    import time
    import MultiProcess_Utils as MU

    emails = pd.read_csv("D:\Python\DE_Path\Data\Emails.csv")
    emails.info()

    p= Pool(2)
    start = time.time()
    capital_letters = p.map(MU.count_capital_letters, emails["RawText"])
    total = time.time() - start
    print(total)

    print(capital_letters)
