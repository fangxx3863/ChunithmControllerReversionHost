import sys
import glob
import time
from main_gui import Ui_MainWindow
# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *
from PySide2.QtWidgets import QMainWindow, QInputDialog, QMessageBox, QLineEdit, QApplication
from PySide2.QtCore import QThread, QObject, Signal

import serial
from configobj import ConfigObj

class MainWindow(QMainWindow):
    findLock = 0
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.readConfList()
        self.readDelConfList()
        
        

    def on_read(self):  # 点击读取设备
        ser = serial.Serial(device, 115200)     # 初始化下位机读取
        ser.write("GetKeys".encode("utf8"))
        while True:
            count = ser.inWaiting() # 获取串口缓冲区数据
            if count !=0:
                data = ser.readline()
                recv = str(data[0:-2].decode("utf8")) # 读出串口数据，数据采用utf8编码
                if recv:
                    break
        clientData = recv.split("/")
        self.showClientData(clientData)
        self.ui.plainTextEdit_log.appendPlainText("读取下位机配置成功.")
    
    def on_write(self): # 点击写入设备
        ser = serial.Serial(device, 115200)     # 初始化下位机读取
        ser.write("SetKeys".encode("utf8"))
        while True:
            count = ser.inWaiting() # 获取串口缓冲区数据
            if count !=0:
                recv = str(ser.readline()[0:-2].decode("utf8")) # 读出串口数据，数据采用utf8编码
                if recv:
                    break
        if recv == "KeySetReady":
            time.sleep(0.5)
            writeKeys = ""
            writeKeys += self.ui.lineEdit_K1.text()
            writeKeys += self.ui.lineEdit_K2.text()
            writeKeys += self.ui.lineEdit_K3.text()
            writeKeys += self.ui.lineEdit_K4.text()
            writeKeys += self.ui.lineEdit_K5.text()
            writeKeys += self.ui.lineEdit_K6.text()
            writeKeys += self.ui.lineEdit_K7.text()
            writeKeys += self.ui.lineEdit_K8.text()
            writeKeys += self.ui.lineEdit_K9.text()
            writeKeys += self.ui.lineEdit_K10.text()
            writeKeys += self.ui.lineEdit_K11.text()
            writeKeys += self.ui.lineEdit_K12.text()
            writeKeys += self.ui.lineEdit_K13.text()
            writeKeys += self.ui.lineEdit_K14.text()
            writeKeys += self.ui.lineEdit_K15.text()
            writeKeys += self.ui.lineEdit_K16.text()
            writeKeys += self.ui.lineEdit_K17.text()
            writeKeys += self.ui.lineEdit_K18.text()
            writeKeys += self.ui.lineEdit_K19.text()
            writeKeys += self.ui.lineEdit_K20.text()
            writeKeys += self.ui.lineEdit_K21.text()
            writeKeys += self.ui.lineEdit_K22.text()
            writeKeys += self.ui.lineEdit_K23.text()
            writeKeys += self.ui.lineEdit_K24.text()
            writeKeys += self.ui.lineEdit_K25.text()
            writeKeys += self.ui.lineEdit_K26.text()
            writeKeys += self.ui.lineEdit_K27.text()
            writeKeys += self.ui.lineEdit_K28.text()
            writeKeys += self.ui.lineEdit_K29.text()
            writeKeys += self.ui.lineEdit_K30.text()
            writeKeys += self.ui.lineEdit_K31.text()
            writeKeys += self.ui.lineEdit_K32.text()
            writeKeys += self.ui.lineEdit_ir1.text()
            writeKeys += self.ui.lineEdit_ir2.text()
            writeKeys += self.ui.lineEdit_ir3.text()
            writeKeys += self.ui.lineEdit_ir4.text()
            writeKeys += self.ui.lineEdit_ir5.text()
            writeKeys += self.ui.lineEdit_ir6.text()
            if self.ui.checkBox_IR.isChecked():
                writeKeys += "y"
            else:
                writeKeys += "n"
            if self.ui.checkBox_Slider.isChecked():
                writeKeys += "y"
            else:
                writeKeys += "n"
            # writeKeys += self.ui.lineEdit_threshold.text()
            data = writeKeys.encode("utf8") + int(self.ui.lineEdit_threshold.text()).to_bytes(1, byteorder="big")
            # print(data)
            ser.write(data)
            self.ui.plainTextEdit_log.appendPlainText("写入下位机配置成功.")
            
        
    def on_check(self): # 点击查找设备
        self.ui.plainTextEdit_log.appendPlainText("正在查找设备,请勿重复点击...")
        
        if not self.findLock:
            # device = self.findDevice()       # 查找下位机设备ID
            self.thread = QThread()
            self.worker = Worker()
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.findDevice)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.worker.finished.connect(self.findItLog)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.start()
            self.findLock = 1
            # if device:
            #     self.ui.plainTextEdit_log.appendPlainText("已找到下位机.")
            
    def findItLog(self):
        self.findLock = 0
        if device:
            self.ui.plainTextEdit_log.appendPlainText("已找到下位机.")
        else:
            self.ui.plainTextEdit_log.appendPlainText("未找到下位机.")
        
    def on_save(self):  # 点击保存配置文件
        config = ConfigObj("setting.ini",encoding='UTF8')
        writeConf = []
        writeConf.append(self.ui.lineEdit_K1.text())
        writeConf.append(self.ui.lineEdit_K2.text())
        writeConf.append(self.ui.lineEdit_K3.text())
        writeConf.append(self.ui.lineEdit_K4.text())
        writeConf.append(self.ui.lineEdit_K5.text())
        writeConf.append(self.ui.lineEdit_K6.text())
        writeConf.append(self.ui.lineEdit_K7.text())
        writeConf.append(self.ui.lineEdit_K8.text())
        writeConf.append(self.ui.lineEdit_K9.text())
        writeConf.append(self.ui.lineEdit_K10.text())
        writeConf.append(self.ui.lineEdit_K11.text())
        writeConf.append(self.ui.lineEdit_K12.text())
        writeConf.append(self.ui.lineEdit_K13.text())
        writeConf.append(self.ui.lineEdit_K14.text())
        writeConf.append(self.ui.lineEdit_K15.text())
        writeConf.append(self.ui.lineEdit_K16.text())
        writeConf.append(self.ui.lineEdit_K17.text())
        writeConf.append(self.ui.lineEdit_K18.text())
        writeConf.append(self.ui.lineEdit_K19.text())
        writeConf.append(self.ui.lineEdit_K20.text())
        writeConf.append(self.ui.lineEdit_K21.text())
        writeConf.append(self.ui.lineEdit_K22.text())
        writeConf.append(self.ui.lineEdit_K23.text())
        writeConf.append(self.ui.lineEdit_K24.text())
        writeConf.append(self.ui.lineEdit_K25.text())
        writeConf.append(self.ui.lineEdit_K26.text())
        writeConf.append(self.ui.lineEdit_K27.text())
        writeConf.append(self.ui.lineEdit_K28.text())
        writeConf.append(self.ui.lineEdit_K29.text())
        writeConf.append(self.ui.lineEdit_K30.text())
        writeConf.append(self.ui.lineEdit_K31.text())
        writeConf.append(self.ui.lineEdit_K32.text())
        writeConf.append(self.ui.lineEdit_ir1.text())
        writeConf.append(self.ui.lineEdit_ir2.text())
        writeConf.append(self.ui.lineEdit_ir3.text())
        writeConf.append(self.ui.lineEdit_ir4.text())
        writeConf.append(self.ui.lineEdit_ir5.text())
        writeConf.append(self.ui.lineEdit_ir6.text())
        writeConf.append(int(self.ui.checkBox_IR.isChecked()))
        writeConf.append(int(self.ui.checkBox_Slider.isChecked()))
        writeConf.append(str(self.ui.lineEdit_threshold.text()))
        keys = config[nowConf].keys()
        i = 0
        for key in keys:
            config[nowConf][key] = writeConf[i]
            i += 1
        config.write()
        self.ui.plainTextEdit_log.appendPlainText("写入配置文件成功.")
        
    def on_gloves(self):
        ser = serial.Serial(device, 115200)     # 初始化下位机读取
        ser.write("Gloves".encode("utf8"))
        while True:
            count = ser.inWaiting() # 获取串口缓冲区数据
            if count !=0:
                recv = str(ser.readline()[0:-2].decode("utf8")) # 读出串口数据，数据采用utf8编码
                if recv:
                    break
        if recv == "Change to gloves":
            self.ui.plainTextEdit_log.appendPlainText("已切换至手套模式.")
        pass
    
    def on_hands(self):
        ser = serial.Serial(device, 115200)     # 初始化下位机读取
        ser.write("Hands".encode("utf8"))
        while True:
            count = ser.inWaiting() # 获取串口缓冲区数据
            if count !=0:
                recv = str(ser.readline()[0:-2].decode("utf8")) # 读出串口数据，数据采用utf8编码
                if recv:
                    break
        if recv == "Change to hands":
            self.ui.plainTextEdit_log.appendPlainText("已切换至空手模式.")
        pass
        
    def on_exit(self):  # 点击退出应用
        sys.exit(0)
        
    def newConf(self):
        Name, okPressed = QInputDialog.getText(self, "新建配置文件","请输入配置文件名称", QLineEdit.Normal, "")
        config = ConfigObj("setting.ini",encoding='UTF8')
        List = config.keys()
        if not Name:
            self.ui.plainTextEdit_log.appendPlainText("新建配置文件未输入名称.")
            QMessageBox.warning(self, "错误", "您未输入任何内容!", QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
        else:
            config = ConfigObj("setting.ini",encoding='UTF8')
            config[Name] = {}
            config[Name]['K1'] = '6'
            config[Name]['K2'] = '7'
            config[Name]['K3'] = '8'
            config[Name]['K4'] = '9'
            config[Name]['K5'] = 'a'
            config[Name]['K6'] = 'b'
            config[Name]['K7'] = 'c'
            config[Name]['K8'] = 'd'
            config[Name]['K9'] = 'e'
            config[Name]['K10'] = 'f'
            config[Name]['K11'] = 'g'
            config[Name]['K12'] = 'h'
            config[Name]['K13'] = 'i'
            config[Name]['K14'] = 'j'
            config[Name]['K15'] = 'k'
            config[Name]['K16'] = 'l'
            config[Name]['K17'] = 'm'
            config[Name]['K18'] = 'n'
            config[Name]['K19'] = 'o'
            config[Name]['K20'] = 'p'
            config[Name]['K21'] = 'q'
            config[Name]['K22'] = 'r'
            config[Name]['K23'] = 's'
            config[Name]['K24'] = 't'
            config[Name]['K25'] = 'u'
            config[Name]['K26'] = 'v'
            config[Name]['K27'] = 'w'
            config[Name]['K28'] = 'x'
            config[Name]['K29'] = 'y'
            config[Name]['K30'] = 'z'
            config[Name]['K31'] = ','
            config[Name]['K32'] = '.'
            config[Name]['IR1'] = '0'
            config[Name]['IR2'] = '1'
            config[Name]['IR3'] = '2'
            config[Name]['IR4'] = '3'
            config[Name]['IR5'] = '4'
            config[Name]['IR6'] = '5'
            config[Name]['IR'] = 1
            config[Name]['Slider'] = 1
            config[Name]['THRESHOLDS'] = 70
            config.write()
            self.ui.plainTextEdit_log.appendPlainText("新建配置文件成功.")
            self.ui.list_conf.clear()
            self.ui.del_conf.clear()
            self.readConfList()
            self.readDelConfList()
            self.showConf(Name)
        
    def writeConf(self, Key, Cmd, List):
        if isinstance(Key, list):
            config = ConfigObj("setting.ini",encoding='UTF8')
            for i in Key:
                for j in Cmd:
                    config[List][i] = j
                    config.write()
        if isinstance(Key, str):
            config = ConfigObj("setting.ini",encoding='UTF8')
            config[List][Key] = Cmd
            config.write()
    
    def readConfList(self):
        config = ConfigObj("setting.ini",encoding='UTF8')
        List = config.keys()
        for item in List:
            action = self.ui.list_conf.addAction(item)
            action.triggered.connect(lambda f=self.showConf,arg=item:f(arg))
        self.ui.plainTextEdit_log.appendPlainText("读取配置文件列表成功.")
    
    def readDelConfList(self):
        config = ConfigObj("setting.ini",encoding='UTF8')
        List = config.keys()
        for item in List:
            action = self.ui.del_conf.addAction(item)
            action.triggered.connect(lambda f=self.delConf,arg=item:f(arg))
    
    def delConf(self, List):
        config = ConfigObj("setting.ini",encoding='UTF8')
        del config[List]
        config.write()
        self.ui.list_conf.clear()
        self.readConfList()
        self.ui.del_conf.clear()
        self.readDelConfList()
        self.ui.plainTextEdit_log.appendPlainText("删除配置文件列表成功.")
    
    def showConf(self, item):
        global nowConf
        nowConf = item
        config = ConfigObj("setting.ini",encoding='UTF8')
        selectConf = config[item]
        keyValue = list(selectConf.values())
        self.ui.lineEdit_K1.setText(keyValue[0])
        self.ui.lineEdit_K2.setText(keyValue[1])
        self.ui.lineEdit_K3.setText(keyValue[2])
        self.ui.lineEdit_K4.setText(keyValue[3])
        self.ui.lineEdit_K5.setText(keyValue[4])
        self.ui.lineEdit_K6.setText(keyValue[5])
        self.ui.lineEdit_K7.setText(keyValue[6])
        self.ui.lineEdit_K8.setText(keyValue[7])
        self.ui.lineEdit_K9.setText(keyValue[8])
        self.ui.lineEdit_K10.setText(keyValue[9])
        self.ui.lineEdit_K11.setText(keyValue[10])
        self.ui.lineEdit_K12.setText(keyValue[11])
        self.ui.lineEdit_K13.setText(keyValue[12])
        self.ui.lineEdit_K14.setText(keyValue[13])
        self.ui.lineEdit_K15.setText(keyValue[14])
        self.ui.lineEdit_K16.setText(keyValue[15])
        self.ui.lineEdit_K17.setText(keyValue[16])
        self.ui.lineEdit_K18.setText(keyValue[17])
        self.ui.lineEdit_K19.setText(keyValue[18])
        self.ui.lineEdit_K20.setText(keyValue[19])
        self.ui.lineEdit_K21.setText(keyValue[20])
        self.ui.lineEdit_K22.setText(keyValue[21])
        self.ui.lineEdit_K23.setText(keyValue[22])
        self.ui.lineEdit_K24.setText(keyValue[23])
        self.ui.lineEdit_K25.setText(keyValue[24])
        self.ui.lineEdit_K26.setText(keyValue[25])
        self.ui.lineEdit_K27.setText(keyValue[26])
        self.ui.lineEdit_K28.setText(keyValue[27])
        self.ui.lineEdit_K29.setText(keyValue[28])
        self.ui.lineEdit_K30.setText(keyValue[29])
        self.ui.lineEdit_K31.setText(keyValue[30])
        self.ui.lineEdit_K32.setText(keyValue[31])
        self.ui.lineEdit_ir1.setText(keyValue[32])
        self.ui.lineEdit_ir2.setText(keyValue[33])
        self.ui.lineEdit_ir3.setText(keyValue[34])
        self.ui.lineEdit_ir4.setText(keyValue[35])
        self.ui.lineEdit_ir5.setText(keyValue[36])
        self.ui.lineEdit_ir6.setText(keyValue[37])
        self.ui.checkBox_IR.setChecked(int(keyValue[38]))
        self.ui.checkBox_Slider.setChecked(int(keyValue[39]))
        self.ui.lineEdit_threshold.setText(str(keyValue[40]))
        self.ui.plainTextEdit_log.appendPlainText("读取配置文件内容成功.")
        
    def showClientData(self, keyValue):
        self.ui.lineEdit_K1.setText(keyValue[0])
        self.ui.lineEdit_K2.setText(keyValue[1])
        self.ui.lineEdit_K3.setText(keyValue[2])
        self.ui.lineEdit_K4.setText(keyValue[3])
        self.ui.lineEdit_K5.setText(keyValue[4])
        self.ui.lineEdit_K6.setText(keyValue[5])
        self.ui.lineEdit_K7.setText(keyValue[6])
        self.ui.lineEdit_K8.setText(keyValue[7])
        self.ui.lineEdit_K9.setText(keyValue[8])
        self.ui.lineEdit_K10.setText(keyValue[9])
        self.ui.lineEdit_K11.setText(keyValue[10])
        self.ui.lineEdit_K12.setText(keyValue[11])
        self.ui.lineEdit_K13.setText(keyValue[12])
        self.ui.lineEdit_K14.setText(keyValue[13])
        self.ui.lineEdit_K15.setText(keyValue[14])
        self.ui.lineEdit_K16.setText(keyValue[15])
        self.ui.lineEdit_K17.setText(keyValue[16])
        self.ui.lineEdit_K18.setText(keyValue[17])
        self.ui.lineEdit_K19.setText(keyValue[18])
        self.ui.lineEdit_K20.setText(keyValue[19])
        self.ui.lineEdit_K21.setText(keyValue[20])
        self.ui.lineEdit_K22.setText(keyValue[21])
        self.ui.lineEdit_K23.setText(keyValue[22])
        self.ui.lineEdit_K24.setText(keyValue[23])
        self.ui.lineEdit_K25.setText(keyValue[24])
        self.ui.lineEdit_K26.setText(keyValue[25])
        self.ui.lineEdit_K27.setText(keyValue[26])
        self.ui.lineEdit_K28.setText(keyValue[27])
        self.ui.lineEdit_K29.setText(keyValue[28])
        self.ui.lineEdit_K30.setText(keyValue[29])
        self.ui.lineEdit_K31.setText(keyValue[30])
        self.ui.lineEdit_K32.setText(keyValue[31])
        self.ui.lineEdit_ir1.setText(keyValue[32])
        self.ui.lineEdit_ir2.setText(keyValue[33])
        self.ui.lineEdit_ir3.setText(keyValue[34])
        self.ui.lineEdit_ir4.setText(keyValue[35])
        self.ui.lineEdit_ir5.setText(keyValue[36])
        self.ui.lineEdit_ir6.setText(keyValue[37])
        if keyValue[38] == "y":
            self.ui.checkBox_IR.setChecked(1)
        else:
            self.ui.checkBox_IR.setChecked(0)
        if keyValue[39] == "y":
            self.ui.checkBox_Slider.setChecked(1)
        else:
            self.ui.checkBox_Slider.setChecked(0)
        self.ui.lineEdit_threshold.setText(keyValue[40])
    
    def serial_ports(self):
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # 这不包括当前的终端"/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        if len(result) == 0:
            raise Exception     # 结果为空抛出异常
        return result
    
    def findDevice(self):
        tty = self.serial_ports()
        for devId in tty:
            ser = serial.Serial(devId, 115200, timeout=5)
            count = 0
            ser.write('check'.encode("utf8"))       # 发送Check命令
            t1 = int(time.time())
            while not count:
                count = ser.inWaiting() # 获取串口缓冲区数据
                if int(time.time()) - t1 > 1:
                    break
            if count !=0:
                recv = str(ser.readline()[0:-2].decode("utf8")) # 读出串口数据，数据采用utf8编码
                if recv == "this":      # 检测下位机是否返回数据
                    ser.close()
                    return devId
        
class Worker(QObject):
    deviceID = 0
    finished = Signal(int)
    findIt = Signal(int)
    
    
    def serial_ports(self):
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # 这不包括当前的终端"/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        if len(result) == 0:
            raise Exception     # 结果为空抛出异常
        if not result:
            return 0
        return result
    
    def findDevice(self):
        # print("Finding...")
        global device
        device = 0
        try: 
            tty = self.serial_ports()
        except:
            # print("No TTY")
            self.finished.emit(1)
        if not tty:
            # print("No TTY")
            self.finished.emit(1)
        for devId in tty:
            print("DevID: " + devId)
            ser = serial.Serial(devId, 115200, timeout=5)
            count = 0
            ser.write('check'.encode("utf8"))       # 发送Check命令
            t1 = int(time.time())
            while not count:
                count = ser.inWaiting() # 获取串口缓冲区数据
                if int(time.time()) - t1 > 1:
                    break
            if count !=0:
                recv = str(ser.readline()[0:-2].decode("utf8")) # 读出串口数据，数据采用utf8编码
                if recv == "this":      # 检测下位机是否返回数据
                    ser.close()
                    self.deviceID = devId
                    device = devId
                    self.findIt.emit(1)
        self.finished.emit(1)

if __name__ == "__main__":
    app = QApplication([])
    win = MainWindow()
    win.setWindowTitle("ChunithmController改键工具")
    win.show()
    sys.exit(app.exec_())