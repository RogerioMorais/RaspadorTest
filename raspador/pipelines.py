# -*- coding: utf-8 -*-
from urllib.request import urlretrieve
from os import path, makedirs
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class RaspadorPipeline(object):
    
    def __init__(self):
        self.image_dir = path.dirname(path.abspath(__file__)) + "/../images"
        if not path.exists(self.image_dir):
            makedirs(self.image_dir)

    def process_item(self, item, spider):
        try:
            image_url = item["img"]
            filename = image_url.split("/")[-1]
            filepath = self.image_dir + "/" + filename
            print("path:"+filepath)
            urlretrieve(image_url, filepath)
            print("download")
            item["picture"] = filename
            print("FileName:"+filename)
            return item
        except Exception as e:
            return item
