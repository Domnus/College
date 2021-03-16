import cv2

imagem = cv2.imread('/home/bentocarlos/Pictures/Wallpapers/0hwfsqufm3w41.jpg')

novaImagem = cv2.GaussianBlur(imagem, (35, 35), 0)

cv2.imshow("Original", imagem)
cv2.imshow("GaussianBlur", novaImagem)

cv2.waitKey(0)
