'''Script to add logo to all photos in the folder.

'''

# There is a problem: a quality of photo decrease as soon as you open it with Image class
# Im working on it.


import os, sys
from PIL import Image, ImageEnhance
from tqdm import tqdm
from tkinter.filedialog import askdirectory, askopenfilename


image_formats = ['JPG', 'JPEG', ]
res_dir_name = '_res'
size = 1024, 1024
logo_size = (int(s/8) for s in size)
# xy_offset = 100, 100

if __name__ == '__main__':
    # Preparing
    # DIR = askdirectory()
    DIR = r'C:\Users\Stanislav\Desktop\photo'
    RES_DIR = os.path.join(DIR, res_dir_name)
    # LOGO_PATH = askopenfilename()
    LOGO_PATH = r'C:\Users\Stanislav\PycharmProjects\lesia_pronko\logo.png'

    # Preparing logo
    logo = Image.open(LOGO_PATH)
    logo.resize(logo_size, Image.ANTIALIAS)
    # logo_bright = 0.3
    # logo = ImageEnhance.Brightness(logo).enhance(logo_bright)

    # Making directory
    if not os.path.exists(RES_DIR):
        os.mkdir(RES_DIR)

    # List of images
    files = os.listdir(DIR)
    images = []
    for f in files:
        if f.split('.')[-1].upper() in image_formats:
            images.append(f)

    # Looping over images
    for img in tqdm(images):
        img_file = os.path.splitext(img)
        img_name = os.path.join(RES_DIR, ''.join(img_file))

        # Changing size of image
        im = Image.open(os.path.join(DIR, img))
        im.resize(size, Image.ANTIALIAS)
        p = im.size[0]/im.size[1]
        xy_offset = im.size[0] - logo.size
        im.paste(logo, xy_offset)
        im.save(img_name)
