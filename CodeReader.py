from pyzbar import pyzbar
import cv2

def barcodeDetector(imgPath):
    image = cv2.imread(imgPath)

    barcodes = pyzbar.decode(image)
    coords = []
    barcodeData = []
    for barcode in barcodes:
        (x,y,w,h) = barcode.rect
        coords.append([[x,y],[x+w,y+h]])
        barcodeData.append(barcode.data)

    return coords, barcodeData


print(barcodeDetector("DotMatrix.png"))
