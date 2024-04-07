from PIL import Image
import numpy as np
import string

import click

@click.command()
@click.option('--data', default='0', help='data u want to decode')
def dec(data):
    #generate conversion keys
    conversion_keys = {}
    keys = string.ascii_letters + string.digits + string.punctuation + string.whitespace 
    values = [x for x in range(0,len(keys))]

    for key in keys:
        conversion_keys[values[keys.index(key)]] = key

    #read im
    im = np.array(Image.open('hello.bmp').convert('L'))
    #decode
    dec = ''
    for char in im:
        dec += conversion_keys[int(str(char).strip('[]'))]

    print(conversion_keys)
    print(im)
    print(dec)

if __name__ == "__main__":
    dec()