import cv2
import numpy as np

jeans = cv2.imread("41094.jpg")


jeans = cv2.resize(jeans,(0,0),fx=0.5,fy=0.5)
# cv2.imshow("jeans",jeans)

gray = cv2.cvtColor(jeans, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray",gray)
canny = cv2.Canny(gray,50,100)
cv2.imshow("canny",canny)

# img = np.empty((300,300,3),np.uint8)

# for row in range(300):
#     for col in range(300):
#         img[row][col] = [150,150,150]

# cv2.imshow("img",img)
cv2.waitKey(0)

# te = np.ones((2,4,4),np.uint8)
# te[0][0][2:4]=[3,4]


# print(te)