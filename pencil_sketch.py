#importing cv2 
import cv2

#Importing the orignal image and reading it
image = cv2.imread("Sample_image.png")
cv2.imshow("Sample", image)
cv2.waitKey(0)

#Converting the image to black & white
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("New Sample", gray_image)
cv2.waitKey(0)

inverted_image = 255 - gray_image
cv2.imshow("Inverted", inverted_image)
cv2.waitKey()

#making a little pencil sketch effect to make it look more realistic 
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

inverted_blurred = 255 - blurred

pencil_sketch = cv2.divide(gray_image, inverted_blurred)
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)

#showing the end result
cv2.imshow("orignal image", image)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)

#cprogrammed by Musa Tahawar
