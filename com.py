import cv2
import os

#パス
file_path = 'Bad Appele!!/Bad_Apple!!.mp4'
#何秒ごとか
time = 0.1

#読み込み
cap_file = cv2.VideoCapture(file_path)
#動画が正しく開けたか確認
if not cap_file.isOpened():
    print("動画の読み込みに失敗しました")
    exit()

#fps
fps = cap_file.get(cv2.CAP_PROP_FPS)
print(fps)

#保存
num = int(fps * time)

#今のframe数
frame_num = 0
count =0
#loop
while(1):
    ret,frame = cap_file.read()  #フレームを読み込む
    if not ret:  #フレームが読み込めなければ終了
        break

    if (frame_num % num == 0):

        #保存するファイル名
        frame_filename = os.path.join("Bad Appele!!/movs", f"frame_{frame_num:04d}.jpg")

        #画像として保存
        cv2.imwrite(frame_filename, frame)
        count += 1


    frame_num += 1

#閉じる
cap_file.release()
print(count)