import requests
import csv


def readCSV():
    lst = []
    with open("url.csv") as f:
        reader = csv.reader(f)
        for r in reader:
            lst.append(r[0])
    return (lst[0], lst[1], lst[2])


def getURLText(URL, auth):
    get_url_info = requests.get(URL, auth=("mpcman", "1958"))
    return get_url_info.text


if __name__ == "__main__":

    url, id, pas = readCSV()
    text = getURLText(url, (id, pas))

    sp = text.split("table")

    # sp[2]が正しい
    print(sp[5])
