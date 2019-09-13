#!/home/mdo/.pyenv/versions/anaconda3-5.3.1/bin/python3
# -*- coding: utf-8 -*-

import requests
import csv
import numpy as np


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


def getValList(tableText):
    sp = text.split("table")
    # sp[2]が正しい
    valLL = sp[5].split("style_td\">")
    val = [v.split("</td")[0] for v in valLL]

    lst = []
    for i in range(7, len(val), 4):
        if "gt" in val[i]:
            lst.append(int(val[i].split(";")[1]))
        else:
            lst.append(int(val[i]))
    return lst


if __name__ == "__main__":

    url, id, pas = readCSV()
    text = getURLText(url, (id, pas))
    val = getValList(text)

    print("Content-Type: text/plain")
    print()
    print(np.sum(val))
