from PIL import Image
import numpy as np
import string
import click

@click.command()
@click.option('--data', default='0', help='data u want to encode')
def enc(data):
    #initialize data
    data = data

    #alphabet
    conversion_keys = {}
    values = string.ascii_letters + string.digits + string.punctuation + string.whitespace 
    keys = [x for x in range(0,len(values))]

    for key in keys:
        conversion_keys[values[keys.index(key)]] = key

    #encode to nums, pixel = [char,0,0] (resp diff colour)
    enc = []
    for char in data:
        enc.append(conversion_keys[char])

    #encode to nums, version 2; pixel = [char1,char2,char3]

    #save to image
    pil_img = Image.fromarray(np.array(enc)).convert('L')
    print(pil_img.mode)
    # RGB

    pil_img.save('hello.bmp')
    print(np.array(enc))

if __name__ == "__main__":
    enc()