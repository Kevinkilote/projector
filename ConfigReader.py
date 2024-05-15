#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#˅
import configparser

class ConfigReader:

    def __init__(self,config_path): 
        self.__config = configparser.ConfigParser()
        self.__config.read(config_path)
        
    def getImageName(self):
        return self.__config['DEFAULT']['image_name']

    def getProjectedImageWidth(self):
        return int(self.__config['DEFAULT']['projected_image_width'])

    def getProjectedOverlapWidth(self):
        return int(self.__config['DEFAULT']['projected_overlap_width'])

    def getGamma(self):
        return float(self.__config['DEFAULT']['gamma'])

    def getSide(self):
        return int(self.__config['DEFAULT']['image_side'])
