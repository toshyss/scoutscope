import cv2

def addImages(f1, f2, out, top, left):
    img1 = cv2.imread(f1)
    img2 = cv2.imread(f2)

    img1 = cv2.resize(img1, (600, 600))

    height, width = img1.shape[:2]
    img2[top:height + top, left:width + left] = img1

    cv2.imshow('out', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite(out, img2)


addImages('./images/mark_camera_satsuei_ok.png', './images/sample.png', 'output.png', 30, 60)