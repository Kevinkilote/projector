#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#˅
import cv2

class MainDisplay:
    
    def __init__(self):
        self.__result_image = None

    def loadImages(self, image_path):
        image = cv2.imread(image_path)
        return image
    
    def initializeImage(self, image):
        self.__result_image = image.copy()
        return self.__result_image
    
    def saveImage(self, image, image_name):
        cv2.imshow(f'result_{image_name}.jpg', self.__result_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    
        
