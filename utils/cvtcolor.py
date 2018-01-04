import cv2
import numpy as np

enemy_spotted_icon = np.uint8([[[87, 204, 100]]])
hsv_enemy_spotted_icon = cv2.cvtColor(enemy_spotted_icon, cv2.COLOR_RGB2HSV)
print(hsv_enemy_spotted_icon)
