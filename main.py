import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

image_path = 'FreeasBird.png'

render = easyocr.Reader(['en'], gpu=True)
result = render.readtext(image_path)
result
