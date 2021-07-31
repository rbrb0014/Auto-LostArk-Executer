import pyautogui
import time
from skimage.metrics import structural_similarity
import pytesseract as tesseract
import re
import cv2

import pyzbar.pyzbar as pyzbar  # pip install pyzbar
import cv2  # pip install opencv-python
import webbrowser


pyautogui.click(x=200, y=210)
pyautogui.click(x=200, y=210)

imgBack = cv2.imread('background.jpg')
imgQrCheck = cv2.imread('qrCheck.jpg')
imgZbarCheck = cv2.imread('zbarCheck.jpg')

while True:
    time.sleep(1)
    pyautogui.screenshot('./loginPage.jpg', region=(960, 600, 50, 50))
    imgLogin = cv2.imread('loginPage.jpg')

    grayBack = cv2.cvtColor(imgBack, cv2.COLOR_BGR2GRAY)
    grayLogin = cv2.cvtColor(imgLogin, cv2.COLOR_BGR2GRAY)

    (score1, diff) = structural_similarity(grayBack, grayLogin, full=True)
    diff = (diff * 255).astype("uint8")

    print(score1)
    if score1 > 0.99:
        print("로그인창 발견")
        pyautogui.click(x=980, y=630)
        break

while True:
    time.sleep(1)
    pyautogui.screenshot('./qrLogin.jpg', region=(740, 725, 200, 50))
    imgQrLogin = cv2.imread('qrLogin.jpg')

    grayQrCheck = cv2.cvtColor(imgQrCheck, cv2.COLOR_BGR2GRAY)
    grayQrLogin = cv2.cvtColor(imgQrLogin, cv2.COLOR_BGR2GRAY)

    (score2, diff) = structural_similarity(grayQrCheck, grayQrLogin, full=True)
    diff = (diff * 255).astype("uint8")
    
    print(score2)
    if score2 > 0.99:
        print("qr로그인창 발견")
        pyautogui.click(x=900, y=770)
        break


while True:
    time.sleep(1)
    pyautogui.screenshot('./zbarCmp.jpg', region=(895, 587, 25, 25))
    imgZbarCmp  = cv2.imread('zbarCmp.jpg')

    grayZbarCheck = cv2.cvtColor(imgZbarCheck, cv2.COLOR_BGR2GRAY)
    grayZbarCmp = cv2.cvtColor(imgZbarCmp, cv2.COLOR_BGR2GRAY)

    (score2, diff) = structural_similarity(grayZbarCheck, grayZbarCmp, full=True)
    diff = (diff * 255).astype("uint8")
    
    print(score2)
    if score2 > 0.99:
        print("qr코드 발견")
        pyautogui.screenshot('./zbar.jpg', region=(870, 530, 160, 200))
        pyautogui.screenshot('./loginNum.jpg', region=(962, 484, 37, 30))
        break


im = cv2.imread('zbar.jpg')
# Find barcodes and QR codes
decodedObjects = pyzbar.decode(im)

# Print results
for obj in decodedObjects:
    print(obj.data)
    webbrowser.open(obj.data)
    # 화면 최대화
    pyautogui.keyDown('altleft')
    pyautogui.keyDown('space')
    pyautogui.keyUp('altleft')
    pyautogui.keyUp('space')
    pyautogui.keyDown('x')
    pyautogui.keyUp('x')



tesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract'
img1 = cv2.imread("loginNum.jpg", cv2.IMREAD_COLOR)
hsv1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
text1 = tesseract.image_to_string(hsv1, config='--psm 6')
split1 = re.split('\s', text1)
print(split1)

time.sleep(2)
pyautogui.screenshot('./choice.jpg', region=(300, 640, 1320, 40))

img2 = cv2.imread("choice.jpg", cv2.IMREAD_COLOR)
hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
text2 = tesseract.image_to_string(hsv2, config='--psm 6')
split2 = re.split('\s', text2)
print(split2)

for i in range(3):
    if(split1[0] in split2[i]):
        pyautogui.click(x=300+660*i, y=660)
        print(i+1)
        pyautogui.keyDown('ctrlleft')
        pyautogui.keyDown('w')
        pyautogui.keyUp('ctrlleft')
        pyautogui.keyUp('w')
        time.sleep(3)
        pyautogui.click(x=1400, y=500)
        print('로아 실행 완료')