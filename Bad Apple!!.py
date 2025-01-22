from PIL import Image
import numpy as np
import time
import shutil

file_path="Bad Appele!!/Bad Apple!!.csv"
max = 2191

input("name?")

a=int(0/3)

for i in range(max):
    b = a*3
    # 画像のファイルパス
    file_path2 = f'Bad Appele!!/movs/frame_{b:04d}.jpg'

    #画像を読み込んでグレースケール（Lモード）に変換し、サイズ変更
    image = Image.open(file_path2).convert('L')
    del file_path2

    #サイズ変更
    new_size = (256,128)
    resized_image = image.resize(new_size, resample=Image.BICUBIC)
    del image
    del new_size

    #NumPy配列に変換
    im_gray = np.array(resized_image)
    del resized_image


    with open("Bad Appele!!/test.txt",'w') as file:
        file.write("")

    with open("Bad Appele!!/test.txt","a") as file:
        for i in im_gray:
            for j in i:
                if (j == 255):
                    file.write(" ")
                else:
                    file.write("@")
            file.write("\n")
    time.sleep(0.1)
    shutil.copy("Bad Appele!!/test.txt", file_path)
    print("next")
    print("frame is "+str(b))
    del im_gray
    a+=1