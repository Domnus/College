import cv2

video = cv2.VideoCapture(0)

background = None
restart = 0

while True:
    ret, frame = video.read()

    frame_resize = cv2.resize(frame, (1280, 720))

    gray = cv2.cvtColor(frame_resize, cv2.COLOR_BGR2GRAY)

    frame_gaussian = cv2.GaussianBlur(gray, (35, 35), 0)

    if background is None:
        background = frame_gaussian

    difference = cv2.absdiff(frame_gaussian, background)

    thresh = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]

    dilate = cv2.dilate(thresh, None, iterations=6)

    contours = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]  

    for c in contours:
        if cv2.contourArea(c) < 500:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print("Detectou")

    if restart >= 5:
        restart = 0
        background = None

    if cv2.waitKey(1) == ord('q'):
        break

    restart += 1

    cv2.imshow("webcam", frame)
    # cv2.imshow("Escala de cinza", gray)
    # cv2.imshow("Gaussian", frame_gaussian)
    # cv2.imshow("diff", difference)

video.release()
cv2.destroyAllWindows()
