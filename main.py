import schedule
import threading
from threading import Thread
import time
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import datetime
from zoom import join_zoom

def parselink(text):
    for line in text.split('\n'):
        if 'zoom.us' in line:
            link = 'https://us02web.zoom.us/wc/join/' + line[line.find('j/')+2:line.find('?')]
        if 'Код' in line or 'код' in line:
            pas = line.split()[-1]
    return link, pas

def read_tbl(df):
    l = []
    for i in range(df.shape[0]):
        l.append("schedule.every()." + df["day"][i] + 
                    ".at('" + df["time"][i] + "').do(startThread," + "'"
                    + df["link"][i]+"', '" + df["pass"][i] + "', '" + 
                    df["name"][i]  +  "', '"
                    +df["user_name"][i] + "', '" + df["msg"][i]+"')")
    return l


def startThread(link, pas, name, user_name, msg):
    tr = Thread(target=join_zoom, args=(link, pas, name, user_name, msg))
    print('Тред c именем {} инициализирован'.format(name))
    tr.start()
    print('Тред c именем {} запущен'.format(name))

if __name__ == "__main__":
    print('debug')
