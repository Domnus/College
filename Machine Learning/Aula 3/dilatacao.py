import cv2 

imagem = cv2.imread("/home/bentocarlos/Pictures/Wallpapers/0hwfsqufm3w41.jpg")

dilate = cv2.dilate(imagem, None, iterations=10)

cv2.imshow("Original", imagem)
cv2.imshow("Dilate", dilate)

cv2.waitKey(0)
