import sys
from logging import raiseExceptions
from pywinusb import hid
from main_gui import Ui_MainWindow
# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *
from PySide2.QtWidgets import QMainWindow, QInputDialog, QMessageBox, QLineEdit, QApplication
from configobj import ConfigObj

class USB:
    def data_handler(self, data): # 数据回调
            self.rawData = data
            decData = ""
            data.pop(0)
            for i in data:
                if i != 0:
                    decData += chr(i)
            self.decData = decData
    
    def __init__(self, VID, PID):   # 初始化
        self.rawData = []
        self.decData = 0
        self.VID = VID
        self.PID = PID
        filter = hid.HidDeviceFilter(vendor_id = VID, product_id = PID)
        devices = filter.get_devices()
        if devices:
            global device
            device = devices[0]
            device.open()
            device.set_raw_data_handler(self.data_handler)
        else:
            raiseExceptions()
            
    def Setup(self):
        filter = hid.HidDeviceFilter(vendor_id = self.VID, product_id = self.PID)
        devices = filter.get_devices()
        if devices:
            global device
            device = devices[0]
            device.open()
            device.set_raw_data_handler(self.data_handler)
        else:
            raiseExceptions()
        
    def sendDecData(self, data):    # 发送字符串
        report = device.find_output_reports()
        sdata = [6]     # ReportID 6
        for i in list(data):
            sdata.append(ord(i))
        for i in range(64 - len(sdata)):
            sdata.append(0)
        # print(sdata)
        report[0].set_raw_data(bytes(sdata))
        report[0].send()
    
    def sendRawData(self, data):    # 发送数组
        report = device.find_output_reports()
        sdata = [6]     # ReportID 6
        for i in data:
            sdata.append(i)
        for i in range(64 - len(sdata)):
            sdata.append(0)
        report[0].set_raw_data(bytes(sdata))
        report[0].send()

    def receiveDecData(self):   # 接收解码数据
        if self.decData != 0:
            return self.decData
        return 0
    
    def receiveRawData(self):   # 接收原始数据
        if self.rawData != 0:
            return self.rawData
        return 0

class MainWindow(QMainWindow):
    findLock = 0
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.on_check()
        self.readConfList()
        self.readDelConfList()
        
    def emptyCheck(self):
        if self.ui.lineEdit_K1.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K1不可为空!")
            return 1
        if self.ui.lineEdit_K2.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K2不可为空!")
            return 1
        if self.ui.lineEdit_K3.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K3不可为空!")
            return 1
        if self.ui.lineEdit_K4.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K4不可为空!")
            return 1
        if self.ui.lineEdit_K5.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K5不可为空!")
            return 1
        if self.ui.lineEdit_K6.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K6不可为空!")
            return 1
        if self.ui.lineEdit_K7.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K7不可为空!")
            return 1
        if self.ui.lineEdit_K8.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K8不可为空!")
            return 1
        if self.ui.lineEdit_K9.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K9不可为空!")
            return 1
        if self.ui.lineEdit_K10.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K10不可为空!")
            return 1
        if self.ui.lineEdit_K11.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K11不可为空!")
            return 1
        if self.ui.lineEdit_K12.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K12不可为空!")
            return 1
        if self.ui.lineEdit_K13.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K13不可为空!")
            return 1
        if self.ui.lineEdit_K14.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K14不可为空!")
            return 1
        if self.ui.lineEdit_K15.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K15不可为空!")
            return 1
        if self.ui.lineEdit_K16.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K16不可为空!")
            return 1
        if self.ui.lineEdit_K17.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K17不可为空!")
            return 1
        if self.ui.lineEdit_K18.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K18不可为空!")
            return 1
        if self.ui.lineEdit_K19.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K19不可为空!")
            return 1
        if self.ui.lineEdit_K20.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K20不可为空!")
            return 1
        if self.ui.lineEdit_K21.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K21不可为空!")
            return 1
        if self.ui.lineEdit_K22.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K22不可为空!")
            return 1
        if self.ui.lineEdit_K23.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K23不可为空!")
            return 1
        if self.ui.lineEdit_K24.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K24不可为空!")
            return 1
        if self.ui.lineEdit_K25.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K25不可为空!")
            return 1
        if self.ui.lineEdit_K26.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K26不可为空!")
            return 1
        if self.ui.lineEdit_K27.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K27不可为空!")
            return 1
        if self.ui.lineEdit_K28.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K28不可为空!")
            return 1
        if self.ui.lineEdit_K29.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K29不可为空!")
            return 1
        if self.ui.lineEdit_K30.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K30不可为空!")
            return 1
        if self.ui.lineEdit_K31.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K31不可为空!")
            return 1
        if self.ui.lineEdit_K32.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("K32不可为空!")
            return 1
        if self.ui.lineEdit_ir1.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("IR1不可为空!")
            return 1
        if self.ui.lineEdit_ir2.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("IR2不可为空!")
            return 1
        if self.ui.lineEdit_ir3.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("IR3不可为空!")
            return 1
        if self.ui.lineEdit_ir4.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("IR4不可为空!")
            return 1
        if self.ui.lineEdit_ir5.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("IR5不可为空!")
            return 1
        if self.ui.lineEdit_ir6.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("IR6不可为空!")
            return 1
        if self.ui.lineEdit_threshold.text() == "":
            self.ui.plainTextEdit_log.appendPlainText("触摸阈值不可为空!")
            return 1

    def on_read(self):  # 点击读取设备
        HID.sendDecData("GetKeys%")
        while True:
            try:
                pdata = HID.receiveDecData().split("/")
                if pdata != 0:
                    break
            except:
                pass
        sdata = list(pdata[0])
        sdata.append(pdata[1])
        self.showClientData(sdata)
        self.ui.plainTextEdit_log.appendPlainText("读取下位机配置成功.")
    
    def on_write(self): # 点击写入设备
        if self.emptyCheck():
            return 0
        rdata = []
        rdata.append(ord(self.ui.lineEdit_K1.text()))
        rdata.append(ord(self.ui.lineEdit_K2.text()))
        rdata.append(ord(self.ui.lineEdit_K3.text()))
        rdata.append(ord(self.ui.lineEdit_K4.text()))
        rdata.append(ord(self.ui.lineEdit_K5.text()))
        rdata.append(ord(self.ui.lineEdit_K6.text()))
        rdata.append(ord(self.ui.lineEdit_K7.text()))
        rdata.append(ord(self.ui.lineEdit_K8.text()))
        rdata.append(ord(self.ui.lineEdit_K9.text()))
        rdata.append(ord(self.ui.lineEdit_K10.text()))
        rdata.append(ord(self.ui.lineEdit_K11.text()))
        rdata.append(ord(self.ui.lineEdit_K12.text()))
        rdata.append(ord(self.ui.lineEdit_K13.text()))
        rdata.append(ord(self.ui.lineEdit_K14.text()))
        rdata.append(ord(self.ui.lineEdit_K15.text()))
        rdata.append(ord(self.ui.lineEdit_K16.text()))
        rdata.append(ord(self.ui.lineEdit_K17.text()))
        rdata.append(ord(self.ui.lineEdit_K18.text()))
        rdata.append(ord(self.ui.lineEdit_K19.text()))
        rdata.append(ord(self.ui.lineEdit_K20.text()))
        rdata.append(ord(self.ui.lineEdit_K21.text()))
        rdata.append(ord(self.ui.lineEdit_K22.text()))
        rdata.append(ord(self.ui.lineEdit_K23.text()))
        rdata.append(ord(self.ui.lineEdit_K24.text()))
        rdata.append(ord(self.ui.lineEdit_K25.text()))
        rdata.append(ord(self.ui.lineEdit_K26.text()))
        rdata.append(ord(self.ui.lineEdit_K27.text()))
        rdata.append(ord(self.ui.lineEdit_K28.text()))
        rdata.append(ord(self.ui.lineEdit_K29.text()))
        rdata.append(ord(self.ui.lineEdit_K30.text()))
        rdata.append(ord(self.ui.lineEdit_K31.text()))
        rdata.append(ord(self.ui.lineEdit_K32.text()))
        rdata.append(ord(self.ui.lineEdit_ir1.text()))
        rdata.append(ord(self.ui.lineEdit_ir2.text()))
        rdata.append(ord(self.ui.lineEdit_ir3.text()))
        rdata.append(ord(self.ui.lineEdit_ir4.text()))
        rdata.append(ord(self.ui.lineEdit_ir5.text()))
        rdata.append(ord(self.ui.lineEdit_ir6.text()))
        if self.ui.checkBox_IR.isChecked():
            rdata.append(ord("y"))
        else:
            rdata.append(ord("n"))
        if self.ui.checkBox_Slider.isChecked():
            rdata.append(ord("y"))
        else:
            rdata.append(ord("n"))
        rdata.append(int(self.ui.lineEdit_threshold.text()))
        # print(data)
        
        head = []
        for i in list("SetKeys%"):
            head.append(ord(i))
        # print(head + rdata)
        HID.sendRawData(head + rdata)
        self.ui.plainTextEdit_log.appendPlainText("写入下位机配置成功.")
            
        
    def on_check(self): # 点击查找设备
        self.ui.plainTextEdit_log.appendPlainText("正在查找设备,请勿重复点击...")
        try:
            global HID
            HID = USB(0x303A, 0x8222)
            self.ui.plainTextEdit_log.appendPlainText("设备连接成功.")
        except:
            self.ui.plainTextEdit_log.appendPlainText("未找到设备.")
            
    def findItLog(self):
        self.findLock = 0
        if device:
            self.ui.plainTextEdit_log.appendPlainText("已找到下位机.")
        else:
            self.ui.plainTextEdit_log.appendPlainText("未找到下位机.")
        
    def on_save(self):  # 点击保存配置文件
        if self.emptyCheck():
            return 0
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
        HID.sendDecData("Gloves%")
        self.ui.plainTextEdit_log.appendPlainText("切换至手套模式.")
    
    def on_hands(self):
        HID.sendDecData("Hands%")
        self.ui.plainTextEdit_log.appendPlainText("切换至空手模式.")
        
        
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
    
if __name__ == "__main__":
    app = QApplication([])
    win = MainWindow()
    win.setWindowTitle("ChunithmController改键工具")
    win.show()
    sys.exit(app.exec_())