#!/usr/bin/env python3
import base64
import os
import sys
import yaml
from PIL import Image
from io import BytesIO


def vaccine_polarity_visualisation(vaccine,path):
    with open(path+vaccine+"_timeseries_polarity_optimised_dataset.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    print(encoded_string.decode('utf-8'))
    image = Image.open(BytesIO(base64.b64decode(encoded_string)))
    return image
    image.show()
    # im = Image.open('/data/covaxin_timeseries_polarity_optimised_dataset.png')
    # im.show()

def vaccine_timeseries_visualisation(vaccine,path):
    with open(path+vaccine+"_timeseries_polarity_optimised_dataset.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    print(encoded_string.decode('utf-8'))
    image = Image.open(BytesIO(base64.b64decode(encoded_string)))
    return image
    image.show()
    # im = Image.open('/data/covaxin_timeseries_polarity_optimised_dataset.png')
    # im.show()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    
    command = sys.argv[1]
    path = sys.argv[2]
    # result=vaccine_polarity_visualisation(os.environ["INPUT"])
    vaccine_polarity_visualisation(os.environ["INPUT"],os.environ["PATH"])
    vaccine_timeseries_visualisation(os.environ["INPUT"],os.environ["PATH"])
    # Print the result with the YAML package
    print(yaml.dump({ "output": 'I am visualization' }))