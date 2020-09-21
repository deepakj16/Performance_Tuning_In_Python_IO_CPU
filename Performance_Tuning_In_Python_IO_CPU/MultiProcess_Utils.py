from Python_Classics import Pandas as pd

emails = pd.read_csv("D:\Python\DE_Path\Data\Emails.csv")
#emails.info()


def count_capital_letters(email):
    return len([letter for letter in email if letter.isupper()])


def count_capitals_in_emails(start, finish, capital_letters):
    for email in emails["RawText"][start:finish]:
        capital_letters.append(count_capital_letters(email))