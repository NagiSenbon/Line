import cv2
import numpy as np
import matplotlib.pyplot as plt

def LineDetection():
      img_1 = input('Your image: ')
      print('OK')
      img_2 = cv2.imread(img_1, cv2.IMREAD_GRAYSCALE)
      img = cv2.Canny(img_2, 50, 200)
      lines = cv2.HoughLinesP(img, rho=1,
                              theta=np.deg2rad(0.1),
                              threshold=80, 
                              minLineLength=250,
                              maxLineGap=30)
      
      fig, ax = plt.subplots(dpi=300)
      plt.imshow(img_2, cmap='gray')
      
      from matplotlib.collections import LineCollection
      lc = LineCollection(lines.reshape(-1, 2, 2))
      ax.add_collection(lc)
      ax.axis('off')
      plt.show()
      return 0

if __name__ == '__main__':
      LineDetection()
