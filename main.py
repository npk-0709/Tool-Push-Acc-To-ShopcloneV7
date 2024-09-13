import requests
import time
from Klib.files import *
from Klib.helper import *


while True:
    print(getNowTime(), f" [*] Đang Thống Kê Dữ Liệu...")
    config = openFileJson("config.json")
    time_delay = config['time_delay']
    domain = config['domain']
    code = config['code']
    api_key = config['api_key']
    path_to_file_data = config['path_to_file_data']
    row_count = config['row_count']
    try:
        File = openFile(path_to_file_data, True)
    except:
        print("ĐƯỜNG DẪN SAI HOẶC FILE BỊ LỖI ! ")
        exit()
    indexx = 0
    print(
        getNowTime(),
        f" [*] Tiến Hành Tải Lên {str(len(File)-row_count)} Tài Khoản Mới...")
    for count in range(row_count, len(File)):
        data = File[count].strip()
        if data != "":
            pushx = data.split("|", 5)[
                0]+"|"+data.split("|", 5)[1]+"|"+data.split("|", 5)[2]
            url = f'{domain}/api/importAccount.php?code={code}&api_key={api_key}&account={pushx}'
            for i in range(50):
                try:
                    requests.get(url, timeout=10)
                    break
                except:
                    time.sleep(0.5)
            indexx += 1
    if indexx != 0:
        print(
            getNowTime(),
            f" [*] Tải Lên Thành Công {str(indexx)} Tài Khoản Mới...")
    else:
        print(getNowTime(), ' [*] Không Tìm Thấy Tài Khoản Mới')
    replaceJsonFiles('config.json', ['row_count'], [len(File)])
    start_time = time.time()
    print(f"[*] Đang Chờ #{str(time_delay)} Giây Cho Lần Up Tiếp Theo...")
    for _ in range(99999):
        if time.time()-start_time >= config['time_delay']:
            break
        time.sleep(0.5)
    print("*"*20)
