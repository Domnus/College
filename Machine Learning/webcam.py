import cv2

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if cv2.waitKey(1) == ord('q'):
        break

    cv2.imshow("webcam", frame)

video.release()
cv2.destroyAllWindows()