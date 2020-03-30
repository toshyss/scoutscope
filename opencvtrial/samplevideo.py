import cv2

capture = cv2.VideoCapture('data/samplevideo.mp4')

while True:
    ret, frame = capture.read()
    if ret:
        cv2.imshow('sample', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

# cv2.destroyAllWindows()
cv2.destroyWindow('sample')