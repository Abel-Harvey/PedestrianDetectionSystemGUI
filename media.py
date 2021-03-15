import os
from PyQt5.Qt import QUrl, QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QApplication, QWidget


class Demo(QWidget):
    def __init__(self, url):
        super(Demo, self).__init__()
        self.playlist = QMediaPlaylist(self)
        self.video_widget = QVideoWidget(self)  # 1
        self.video_widget.resize(self.width(), self.height())

        self.player = QMediaPlayer(self)
        self.player.setPlaylist(self.playlist)
        self.player.setVideoOutput(self.video_widget)  # 2

        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(url)))  # 3
        # self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemOnce)
        self.playlist.setCurrentIndex(2)

        self.player.setVolume(50)
        self.player.play()


def get_url():
    url_father = os.path.dirname(os.path.abspath(__file__))
    url = ""
    for i in url_father:
        if i == "\\":
            url = url + "/"
        else:
            url = url + i
    return url


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     url = get_url()
#     print(url)
#     demo = Demo(url)
#     demo.show()
#     sys.exit(app.exec_())
