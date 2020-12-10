from selenium import webdriver
from PIL import Image
from io import BytesIO



def capturar(site, ximagemAnuncio, ordem):
    location = ximagemAnuncio.location
    size = ximagemAnuncio.size
    png = site.get_screenshot_as_png() # saves screenshot of entire page

    im = Image.open(BytesIO(png)) # uses PIL library to open image in memory

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']


    im = im.crop((left, top, right, bottom)) # defines crop points
    indice = str(ordem)
    indices2 = 'screenshot' + indice + '.png'
    im.save(indices2) # saves new cropped image