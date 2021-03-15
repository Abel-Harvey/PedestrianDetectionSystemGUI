import cv2
# import msvcrt
global frame
global point1, point2
global whether_continue


# 截取需要查找的行人图片
def on_mouse(event, x, y, flags, param):
    global frame, point1, point2
    global whether_continue
    img2 = frame.copy()
    if event == cv2.EVENT_LBUTTONDOWN:  # 左键点击
        point1 = (x, y)
        cv2.circle(img2, point1, 10, (0, 255, 0), 5)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):  # 按住左键拖曳
        cv2.rectangle(img2, point1, (x, y), (255, 0, 0), 5)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_LBUTTONUP:  # 左键释放
        point2 = (x, y)
        cv2.rectangle(img2, point1, point2, (0, 0, 255), 5)
        cv2.imshow('image', img2)
        min_x = min(point1[0], point2[0])
        min_y = min(point1[1], point2[1])
        width = abs(point1[0] - point2[0])
        height = abs(point1[1] - point2[1])
        cut_img = frame[min_y:min_y + height, min_x:min_x + width]
        cv2.imwrite('query/0001_c1s1_0_%s.jpg' % min_x, cut_img)
    elif event == cv2.EVENT_FLAG_RBUTTON:  # 右键释放
         whether_continue = False


def get_query():
    global whether_continue
    global frame
    whether_continue = True
    videoCapture = cv2.VideoCapture('center.mp4')  # VideoCapture()中参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
    # Read image
    success, frame = videoCapture.read()
    while success and whether_continue:
        cv2.namedWindow('image',0)  # 得到的图像框就可以自己调整大小，按住四个角会出来小箭头可以拉伸调整
        cv2.setMouseCallback('image', on_mouse)  # 根据编写的函数进行相应
        cv2.imshow('image', frame)  # 显示图像
        cv2.waitKey(0)  # 代表按任意键继续，按住其中任意一个键，实现视频的持续播放
        # if ord(msvcrt.getch()) in [68, 100]:
        #     break
        success, frame = videoCapture.read()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# if __name__ == '__main__':
#     get_query()
# # if __name__ == '__main__':
# #     global whether_continue,frame
# #     whether_continue = True
# #     videoCapture = cv2.VideoCapture('center.mp4')  # VideoCapture()中参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
# #     # Read image
# #     success, frame = videoCapture.read()
# #     while success and whether_continue:
# #         cv2.namedWindow('image',0)  # 得到的图像框就可以自己调整大小，按住四个角会出来小箭头可以拉伸调整
# #         cv2.setMouseCallback('image', on_mouse)  # 根据编写的函数进行相应
# #         cv2.imshow('image', frame)  # 显示图像
# #         cv2.waitKey(0)  # 代表按任意键继续，按住其中任意一个键，实现视频的持续播放
# #         # if ord(msvcrt.getch()) in [68, 100]:
# #         #     break
# #         success, frame = videoCapture.read()
# #     cv2.waitKey(0)
# #     cv2.destroyAllWindows()
