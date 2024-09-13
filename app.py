"""
    # Copyright © 2022 By Nguyễn Phú Khương
    # TELEGRAM : @khuongdev0709
    # Email : dev.phukhuong0709@hotmail.com
    # Github : npk-0709
"""
from PyQt5 import QtGui, QtWidgets
import requests
import time
from Klib.files import *
from Klib.helper import *
from ui import *
import sys
import threading


class App(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        self.ACTIVATION = False
        super().__init__()
        self.setupUi(self)
        self.loadconfig()
        self.url.textChanged.connect(self.updateconfig)
        self.apikey.textChanged.connect(self.updateconfig)
        self.delay.valueChanged.connect(self.updateconfig)
        self.getprefix.valueChanged.connect(self.updateconfig)
        self.RUNNING = False
        self.btnChooseFile.clicked.connect(self.btnChooseFile_clicked)
        self.btnEvent.clicked.connect(self.btnEvent_clicked)

    def btnChooseFile_clicked(self):
        try:
            self.path_to_file_data = QtWidgets.QFileDialog.getOpenFileName(
                self, 'Chọn File', '', 'Text Files (*.txt)')[0]
            self.btnChooseFile.setText(
                str(self.path_to_file_data).split('/')[-1])
            if not os.path.exists("count/"+str(self.path_to_file_data).split('/')[-1]):
                with open("count/"+str(self.path_to_file_data).split('/')[-1], "w") as f:
                    f.write(str(0))
        except:
            pass

    def loadconfig(self):
        self.config = openFileJson("config.json")
        self.url.setText(self.config['domain'])
        self.apikey.setText(self.config['api_key'])
        self.delay.setValue(int(self.config['time_delay']))
        self.getprefix.setValue(int(self.config['prefix']))
        rr = openFile("code.txt", True)
        for i in range(len(rr)):
            _translate = QtCore.QCoreApplication.translate
            self.code.addItem("")
            self.code.setItemText(i, _translate("MainWindow", rr[i]))

    def updateconfig(self):
        conf = {
            "domain": self.url.text(),
            "api_key": self.apikey.text(),
            "time_delay": self.delay.value(),
            "prefix": self.getprefix.value()
        }
        replaceJsonFiles("config.json", list(conf.keys()), list(conf.values()))

    def btnEvent_clicked(self):
        if self.RUNNING:
            self.RUNNING = False
            self.btnEvent.setText("Start")
        else:
            self.RUNNING = True
            self.btnEvent.setText("Stop")
            threading.Thread(target=self.run).start()

    def run(self):
        while True:
            if not self.RUNNING:
                break
            print(getNowTime(), f" [*] Đang Thống Kê Dữ Liệu...")
            time_delay = self.delay.value()
            domain = self.url.text()
            code = self.code.currentText().split("-")[0]
            api_key = self.apikey.text()
            path_to_file_data = self.path_to_file_data
            if not os.path.exists("count/"+path_to_file_data.split("/")[-1]):
                try:
                    with open("count/"+path_to_file_data.split("/")[-1], "w") as f:
                        f.write(str(0))
                except:
                    print("ĐƯỜNG DẪN SAI HOẶC FILE BỊ LỖI ! ")
                    exit()
            else:
                row_count = int(
                    openFile("count/"+path_to_file_data.split("/")[-1]).strip())

            try:
                File = openFile(path_to_file_data, True)
                if File == None:
                    print("ĐƯỜNG DẪN SAI HOẶC FILE BỊ LỖI ! ")
                    exit()
                print(File)
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
                    pushx = ""
                    for index_range in range(self.getprefix.value()):
                        pushx = pushx+data.split("|", 10)[index_range]+"|"
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
            with open("count/"+path_to_file_data.split("/")[-1], "w") as f:
                f.write(str(len(File)))
            start_time = time.time()
            print(
                f"[*] Đang Chờ #{str(time_delay)} Giây Cho Lần Up Tiếp Theo...")
            for _ in range(99999):
                if time.time()-start_time >= self.delay.value():
                    break
                time.sleep(0.5)
            print("*"*20)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    __mainWindow = App()
    __mainWindow.show()
    sys.exit(app.exec_())
