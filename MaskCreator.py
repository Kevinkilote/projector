#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#˅
import cv2
import numpy as np

class MaskCreator:

    def __init__(self, image):
        self.__image = image
        self.__alpha_gradient = None
        self.__gamma_corrected = None
        self.result_image = None
        self.__mask = None
        
    def createMask(self, image_side, mask_width, image_width):
        self.__mask = self.__image.shape[1] * mask_width // image_width
        if image_side == 1:
            self.__alpha_gradient = np.linspace(1, 0, self.__mask)
        elif image_side == 0:
            self.__alpha_gradient = np.linspace(0, 1, self.__mask)

    def gammaCorrection(self, gamma):
            self.__gamma_corrected = np.uint8(cv2.pow(self.__image / 255.0, gamma) * 255)
        

    def alphaBlending(self, image_side):
        if image_side == 1:
            for col in range(self.__mask):
                alpha = self.__alpha_gradient[-self.__mask + col]
                self.result_image[:, col] = alpha * self.__gamma_corrected[:, col] + (1 - alpha) * self.result_image[:, col]
        elif image_side == 0:
            for col in range(self.__mask):
                alpha = self.__alpha_gradient[-self.__mask + col]
                self.result_image[:, -self.__mask + col] = alpha * self.__gamma_corrected[:, -self.__mask + col] + (1 - alpha) * self.result_image[:, -self.__mask + col]
        
    def modifyIntensity(self, image_side):
        if image_side == 1:
            for col in range(self.__mask):
                intensity_factor = 1.0 - (self.__mask - col) / self.__mask
                self.result_image[:, col] = (self.result_image[:, col] * intensity_factor).astype(np.uint8)
        elif image_side == 0:
            for col in range(self.__mask):
                intensity_factor = 1.0 - col / self.__mask
                self.result_image[:, -self.__mask + col] = (self.result_image[:, -self.__mask + col] * intensity_factor).astype(np.uint8)
