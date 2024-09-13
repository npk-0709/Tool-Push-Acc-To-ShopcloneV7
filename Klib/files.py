"""
    # Copyright © 2022 By Nguyễn Phú Khương
    # ZALO : 0363561629
    # Email : dev.phukhuong0709@hotmail.com
    # Github : npk-0709
"""
import json
import datetime


def openFile(pathFile: str, toLines: bool = False):
    try:
        with open(pathFile, 'r', encoding='utf-8') as f:
            if toLines:
                return [str(i).strip() for i in f.readlines()]
            return f.read().strip()
    except Exception as e:
        return None


def openFileJson(pathFile: str):
    try:
        with open(pathFile, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        return None


def saveFile(pathFile: str, data: str, mode='a+', end: str = '\n'):
    try:
        with open(pathFile, mode, encoding='utf-8') as f:
            return f.write(data+end)
    except Exception as e:
        return None


def saveFileAsLog(data: str):
    try:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        data = data.replace('\n', '=-=-=')
        with open('log.data', 'a+', encoding='utf-8') as f:
            return f.write(f'{now}|{data}\n')
    except Exception as e:
        return None


def saveFilejson(pathFile: str, data: object, mode='w'):
    try:
        with open(pathFile, mode, encoding='utf-8') as f:
            return json.dump(data, f, indent=4)
    except Exception as e:
        return None


def replaceJsonFiles(pathFile: str, keys: list, newValues: list):
    try:
        with open(pathFile, 'r', encoding='utf-8') as f:
            x = json.load(f)
        error = 0
        for i in range(len(keys)):
            try:
                x[keys[i]] = newValues[i]
            except:
                error += 1

        with open(pathFile, 'w', encoding='utf-8') as f:
            json.dump(x, f, indent=4)

        return True, error

    except Exception as e:
        return None, None


def saveLogger(typelog='account.log', log: str = '', dir: str = ''):
    """
    debug.log
    accounts.log
    app.log
    error.log
    run.log
    """
    try:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open(f'{dir}/{typelog}', 'a+', encoding='utf-8') as f:
            return f.write(f'{now} | {log} \n')
    except:
        pass
