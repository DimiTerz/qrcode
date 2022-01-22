import cv2
import qrcode

mode = input("To create a QrCode enter 1 to decode enter 2: ")
if mode == "1":
    userInput = input("Type something to test this out: ")
    filename = input("Type in the filename to use for the image: ")
    img = qrcode.make(userInput)
    img.save("%s.png" % filename)
elif mode == "2":
    filenameIn = input("Type in the full filename to decode: ")
    d = cv2.QRCodeDetector()
    retval, points, straight_qrcode = d.detectAndDecode(cv2.imread(filenameIn))
    print(retval)
