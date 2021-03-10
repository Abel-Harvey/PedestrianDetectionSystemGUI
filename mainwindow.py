from PyQt5.QtWidgets import QRadioButton, QMessageBox, QFileDialog, QLineEdit
from media import *
import os


class MainWindow:
    def __init__(self, wight, height):
        """
        :param wight: 窗体的宽
        :param height: 窗体的高
        """
        self.app = QApplication(sys.argv)  # 产生一个应用进程

        self.w = QWidget()  # 窗体
        self.w.setFixedSize(wight, height)  # 固定窗口大小
        # self.w.resize(wight, height)  # 设置其初始大小
        self.w.setWindowTitle("智能行人检测与安防系统")  # 应用程序名

        # 按钮--退出
        self.btn_exit = QPushButton(self.w)  # 将按钮放在窗体上
        self.btn_exit.setText("退出")
        self.btn_exit.move(320, 150)  # 按钮位置
        self.btn_exit.clicked.connect(self.exit_btn)  # 按钮功能绑定

        # 提示性语句
        self.tips_1 = QLabel(self.w)
        self.tips_1.setText("请选择待寻找人员的圈定方式:")
        self.tips_1.move(10, 10)

        # 选择圈人的方式--视频或者图片
        self.btn_radio_video = QRadioButton(self.w)
        self.btn_radio_video.setText("视频圈人")
        self.btn_radio_video.setChecked(True)  # 默认是按下该按钮的
        self.btn_radio_video.move(20, 30)
        self.btn_radio_image = QRadioButton(self.w)
        self.btn_radio_image.setText("图片圈人")
        self.btn_radio_image.move(20, 60)

        # 提交按钮
        self.btn_commit = QPushButton(self.w)
        self.btn_commit.setText("确认")
        self.btn_commit.move(120, 55)
        self.btn_commit.clicked.connect(self.commit_btn)  # 按钮功能绑定

        # 获取帮助按钮
        self.get_help = QPushButton(self.w)
        self.get_help.setText("帮助")
        self.get_help.move(320, 120)

        # 文件名
        self.file_name = QLineEdit(self.w)
        self.file_name.move(100, 30)
        self.file_name.close()

        # 文件选择
        self.file_choice = QFileDialog

        # 圈人按钮
        self.btn_select_person = QPushButton(self.w)
        self.btn_select_person.setText("目标人物标记")
        self.btn_select_person.move(100, 55)
        self.btn_select_person.close()  # 默认关闭

        self.video = Demo()
        self.video.setParent(self.w)
        self.video.close()

        self.w.show()  # 显示该程序
        sys.exit(self.app.exec_())  # 持续运行

    def run(self):
        pass

    def exit_btn(self):
        # 此为退出按钮所链接的函数
        msg = QMessageBox.question(self.w, '注意', '是否确认退出系统', QMessageBox.Yes | QMessageBox.No)
        if msg == QMessageBox.Yes:  # 如果选择退出，则返回正常退出值1
            self.app.exit(1)
        else:
            pass

    def commit_btn(self):
        # 此为提交圈定方式的按钮所链接的函数
        if self.btn_radio_video.isChecked():  # 如果视频圈定框被选择
            self.btn_radio_image.close()  # 图片方式被隐藏
            self.btn_commit.close()  # 提交按钮被隐藏
            self.btn_select_person.show()  # 圈人执行按钮显示
            file_name, file_type = self.file_choice.getOpenFileName(self.w,  # 得到mp4文件
                                                                    "选取文件",
                                                                    os.getcwd(),
                                                                    "All Files(*.mp4);;Text Files(*.mp4)")
            self.file_name.show()
            self.file_name.setText(os.path.split(file_name)[1])
            self.file_name.setEnabled(False)
            # print(os.path.split(file_name), file_type)

        else:
            pass

    def select_btn(self):
        # 此为文件选定后决定执行圈人操作的按钮所链接的函数
        pass


a = MainWindow(400, 200)
