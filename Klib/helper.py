"""
    # Copyright © 2022 By Nguyễn Phú Khương
    # ZALO : 0363561629
    # Email : dev.phukhuong0709@hotmail.com
    # Github : npk-0709
"""
import os
import ctypes
import requests
from datetime import datetime
import string
import random
import subprocess


def random_string(string_length, addstring: str = ''):
    letters = string.ascii_letters + string.digits + addstring
    return ''.join(random.choice(letters) for _ in range(string_length))


def get_chrome_version():
    try:
        result = subprocess.run(
            args=[
                'reg',
                'query',
                'HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon',
                '/v',
                'version'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.split(' ')[-1].strip()
    except:
        return None


def getNewFullName():
    """male | female"""
    try:
        r = requests.get(
            'https://story-shack-cdn-v2.glitch.me/generators/vietnamese-name-generator/?count=10')
        return r.json()['data']
    except:
        pass


def startFile(path: str):
    os.system(f"start {path}")


def processPersent(dataMax: list, dataCurrent: list, typeReturn=int, ndigits=2):
    return typeReturn(round(float(len(dataCurrent)/len(dataMax))*100, ndigits))


def getNowTime(formatx="%d-%m-%Y %H:%M:%S", typeReturn=str):
    return typeReturn(datetime.now().strftime(formatx))


def getMyIP(proxies={}):
    try:
        return str(requests.request('GET', 'https://api.ipify.org/', proxies=proxies).text.strip())
    except:
        return None


def notVar(var: object):
    return not var


def processPassword(password: str, char: str):
    newPass = ''
    for i in password:
        if i == char:
            newPass += random_string(1, '#$%&@')
        else:
            newPass += i
    return newPass


