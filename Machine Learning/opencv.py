# import argparse
import cv2

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="Caminho da imagem")
# args = vars(ap.parse_args())

image = cv2.imread("/home/bentocarlos/Pictures/Wallpapers/0hwfsqufm3w41.jpg")
print("Altura: {} pixels".format(image.shape[0]))
print("Largura: {} pixels".format(image.shape[1]))
print("Canais: {} pixels".format(image.shape[2]))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print("Canais: {}".format(gray.shape))

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("nova_img.jpg", image)
