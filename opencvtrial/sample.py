import cv2

img = cv2.imread("./images/sample.png")
img2 = cv2.imread("./images/sample.png", 0)

overlay = cv2.imread("./images/mark_camera_satsuei_ok.png")

print(img.shape)
print(img2.shape)

print(overlay.shape)

overlay = cv2.resize(overlay,(600, 600))


cv2.imshow('overlay', overlay)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imshow('img2', img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.imwrite("./output_images/sample_copy.jpg", img)
# cv2.imwrite("./output_images/sample_copy_gray.jpg", img2)