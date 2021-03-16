import cv2

imagem = cv2.imread('/home/bentocarlos/Pictures/Wallpapers/0hwfsqufm3w41.jpg')

gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

gaussian = cv2.GaussianBlur(gray, (5, 5), 0)

thresh = cv2.threshold(gaussian, 100, 150, cv2.THRESH_BINARY)[1]

thresh_INV = cv2.threshold(gaussian, 155, 255, cv2.THRESH_BINARY_INV)[1]

cv2.imshow("Original", imagem)
cv2.imshow("Dilate", thresh)

cv2.waitKey(0)
