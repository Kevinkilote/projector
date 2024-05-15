#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#˅
from MaskCreator import MaskCreator
from ConfigReader import ConfigReader
from MainDisplay import MainDisplay


# creating object for MainDisplay, ConfigReader classes
#reader = ConfigReader("config_right.ini")
reader = ConfigReader("config_left.ini")
display = MainDisplay()

# initializing variables
mask_width = reader.getProjectedOverlapWidth()
image_width = reader.getProjectedImageWidth()
gamma = reader.getGamma()
image_side = reader.getSide()
image_path = reader.getImageName()

if image_side == 0:
    image_name = 'left'
elif image_side == 1:
    image_name = 'right'
else:
    print("Invalid ImageSide value in config.ini. Use 0 for left image, 1 for right image.")

# loading image
image = display.loadImages(image_path)
result_image = display.initializeImage(image)


if image is not None:
    # creating object for MaskCreator class
    processor = MaskCreator(image)
    
    # image modification
    processor.createMask(image_side, mask_width, image_width)
    processor.gammaCorrection(gamma)
    processor.result_image = result_image
    processor.alphaBlending(image_side)
    processor.modifyIntensity(image_side)
    
    # saving image
    display.saveImage(processor.result_image, image_name)
else:
    print(f"Failed to read the image (ImageSide={image_side}).")
