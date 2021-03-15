import sys
from PyQt5.QtWidgets import QRadioButton, QMessageBox, QFileDialog, QLineEdit, QPushButton, QLabel, QDesktopWidget
from media import *
from query_get import *
from detect import *


class MainWindow:
    def __init__(self, width, height):
        """
        :param width: 窗体的宽
        :param height: 窗体的高
        """
        self.app = QApplication(sys.argv)  # 产生一个应用进程
        self.width = width
        self.height = height

        self.w = QWidget()  # 窗体
        self.w.setFixedSize(width, height)  # 固定窗口大小
        # self.w.resize(wight, height)  # 设置其初始大小
        self.w.setWindowTitle("智能行人检测与安防系统")  # 应用程序名

        # 查看结果时所需要的变量
        self.video = Demo(get_url() + '/output/00014.mp4')  # 视频播放
        self.video.close()
        self.btn_restart = QPushButton(self.w)  # 重新进行
        self.btn_restart.close()
        self.btn_close = QPushButton(self.w)  # 停止播放
        self.btn_close.close()
        self.btn_pause = QPushButton(self.w)  # 暂停播放
        self.btn_pause.close()
        self.btn_goon = QPushButton(self.w)  # 继续播放
        self.btn_goon.close()
        self.btn_again = QPushButton(self.w)  # 再次播放
        self.btn_again.close()
        self.btn_output = QPushButton(self.w)  # 检测成果后结果视频文件路径

        # 打开目标文件所在路径
        self.btn_output.setText("打开文件所在路径")
        self.btn_output.move(self.width * 2 - 150, self.height * 2 - 280)
        self.btn_output.close()
        self.btn_output.clicked.connect(self.get_file)

        # 按钮--退出
        self.btn_exit = QPushButton(self.w)  # 将按钮放在窗体上
        self.btn_exit.setText("退出")
        self.btn_exit.move(320, 150)  # 按钮位置
        self.btn_exit.clicked.connect(self.exit_btn)  # 按钮功能绑定

        # 提示性语句
        self.tips_1 = QLabel(self.w)
        self.tips_1.setText("请选择待寻找人员的圈定方式:")
        self.tips_1.move(10, 10)
        self.tips_1.show()

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
        self.get_help.clicked.connect(self.help_btn)
        self.get_help.setText("帮助")
        self.get_help.move(320, 120)
        self.get_help.show()

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
        self.btn_select_person.clicked.connect(self.select_btn)

        # 执行检索的按钮
        self.btn_detect = QPushButton(self.w)
        self.btn_detect.setText("开始检索")
        self.btn_detect.move(115, 55)
        self.btn_detect.close()
        self.btn_detect.clicked.connect(self.run)

        self.w.show()  # 显示该程序
        sys.exit(self.app.exec_())  # 持续运行

    def run(self):
        # 开始执行检测的函数
        msg = QMessageBox.question(self.w, '注意', '检测将消耗一定时间，请耐心等待', QMessageBox.Ok)
        if msg == QMessageBox.Ok:
            run()
            self.btn_detect.close()
            msg = QMessageBox.information(self.w, '注意', '检测完成，点击预览目标视频', QMessageBox.Ok)
            if msg == QMessageBox.Ok:
                self.play_result()  # 调用播放视频函数
        else:
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
                                                                    get_url(),
                                                                    "All Files(*.mp4);;Text Files(*.mp4)")
            file_name = os.path.split(file_name)[1]
            if file_name == '':  # 避免用户不选择文件
                QMessageBox.question(self.w, '注意', '请至少选择一个文件', QMessageBox.Ok)
                self.commit_btn()
            else:
                self.file_name.show()
                self.file_name.setText(file_name)
                self.file_name.setEnabled(False)
            # print(os.path.split(file_name), file_type)
        else:  # 图片圈人
            QMessageBox.question(self.w, '注意', '开发中...\n请继续使用视频圈人模式', QMessageBox.Ok)
            pass

    def select_btn(self):
        # 此为文件选定后决定执行圈人操作的按钮所链接的函数
        self.btn_select_person.close()  # 按后则关闭
        self.btn_detect.show()
        get_query()

    def help_btn(self):
        # 此为帮助按钮的函数
        msg = QMessageBox.information(self.w, "帮助",
                                      '1.如果是视频，则命名为center.mp4放入项目根目录\n'
                                      '2.如果是图片，则放入query路径下\n'
                                      '3.选择视频或图像圈人\n'
                                      '4.按照提示圈定所希望寻找的人\n'
                                      '5.等候训练完毕，选择查看检索后的视频\n'
                                      '6.为保护隐私，本软件不保存文件，所需要留存，请自行保存相关文件', QMessageBox.Ok)
        if msg == QMessageBox.Ok:
            pass
        pass

    def play_result(self):
        # 播放检索视频
        # 各种按钮清除
        self.btn_radio_image.close()
        self.btn_radio_video.close()
        self.file_name.clear()
        self.file_name.close()
        self.tips_1.close()

        # 视频播放单次循环
        # print(get_url())
        self.video.setParent(self.w)
        self.video.show()
        self.video.move(1, 1)
        self.video.player.play()

        # 窗口和位置变化
        self.w.setFixedSize(self.width * 2, self.height * 2.2)
        self.w.move(270, 200)
        # 退出按钮和帮助按钮变化
        self.btn_exit.move(self.width * 2 - 100, self.height * 2 - 20)
        self.get_help.move(self.width * 2 - 100, self.height * 2 - 50)

        # 再次播放按钮
        self.btn_again.setText("再看一次")
        self.btn_again.move(self.width * 2 - 125, self.height * 2 - 370)
        # self.btn_again.clicked.connect(self.play_result)
        self.btn_again.clicked.connect(lambda: self.set_play(4))
        self.btn_again.show()

        self.btn_goon.setText("继续播放")
        self.btn_goon.move(self.width * 2 - 125, self.height * 2 - 340)
        self.btn_goon.close()
        self.btn_goon.clicked.connect(lambda: self.set_play(1))

        self.btn_pause.setText("暂停播放")
        self.btn_pause.move(self.width * 2 - 125, self.height * 2 - 340)
        self.btn_pause.show()
        self.btn_pause.clicked.connect(lambda: self.set_play(2))

        self.btn_close.setText("停止播放")
        self.btn_close.move(self.width * 2 - 125, self.height * 2 - 310)
        self.btn_close.show()
        self.btn_close.clicked.connect(lambda: self.set_play(3))

        # 重新开始
        self.btn_restart.setText("重新开始")
        self.btn_restart.move(self.width * 2 - 125, self.height * 2 - 340)
        self.btn_restart.close()
        self.btn_restart.clicked.connect(self.restart)

        self.btn_output.show()

    def get_file(self):
        _, _ = QFileDialog.getOpenFileName(self.w,  # 得到mp4文件
                                           "目标路径",
                                           get_url() + '/output/',
                                           "All Files(*.mp4);;Text Files(*.mp4)")
        pass

    def set_play(self, state):
        if state == 1:  # 如果是继续播放
            self.video.player.play()
            # print(self.video.player.state())
            self.btn_goon.close()
            self.btn_pause.show()
        if state == 2:  # 如果是暂停播放
            self.video.player.pause()
            # print(self.video.player.state())
            self.btn_pause.close()
            self.btn_goon.show()
        if state == 3:  # 如果是停止播放
            self.video.player.pause()
            self.video.close()
            self.btn_goon.close()
            self.btn_pause.close()
            self.btn_close.setEnabled(False)
            self.btn_restart.show()
        if state == 4:
            self.btn_close.setEnabled(True)
            self.btn_restart.close()
            self.video.player.pause()
            self.play_result()

    def restart(self):
        self.w.setFixedSize(self.width, self.height)
        self.btn_exit.move(320, 150)
        self.get_help.move(320, 120)
        self.video.close()

        self.tips_1.show()
        self.btn_radio_video.show()
        self.btn_radio_image.show()

        self.btn_commit.show()
        self.btn_output.close()


if __name__ == "__main__":
    a = MainWindow(400, 200)
