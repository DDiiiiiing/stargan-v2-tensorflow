import os
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import getpass
from fontTools.ttLib import TTFont

username = getpass.getuser()
font_root = os.path.join("C:\\Users", username, "AppData\\Local\\Microsoft\\Windows\\Fonts")
del username

# create 8bit RGB image
def draw_single_char(ch: str, font: str, canvas_size=64, x_offset=4, y_offset=4):
    img = Image.new('RGB', (canvas_size, canvas_size), 'white')
    draw = ImageDraw.Draw(img)
    draw.text((x_offset, y_offset), ch, fill='black', font=ImageFont.truetype(os.path.join(font_root, font), size=canvas_size-max(x_offset,y_offset)*3))

    return img


def char_in_font(unicode_char, font):
    ''' check whether unicode missing in font '''
    for cmap in font['cmap'].tables:
        if cmap.isUnicode():
            if ord(unicode_char) in cmap.cmap:
                return True

    return False


def save_dataset(source_path: str, unicode_list: tuple, font: str="NanumMyeongjo-YetHangul.ttf", canvas_size: int=64, x_offset: int=4, y_offset: int=4):
    ''' 폰트의 모든 이미지에 대한 데이터. 각 폰트가 하나의 도메인 jpg 로 저장 '''
    file_num = 0
    for i in unicode_list: #list from text.txt
        #check is font missing     

        # not korean
        if not char_in_font(chr(i), TTFont(os.path.join(font_root, font))): 
            continue
        char_img = draw_single_char(ch=chr(i), font=font, canvas_size=canvas_size, x_offset=x_offset, y_offset=y_offset)

        # korean, but font not compatible
        if np.sum(np.asarray(char_img))>255*3*canvas_size*canvas_size*0.99:
            continue
        
        #line feed
        if i == '0xa':   
            continue

        img = centering_img(char_img)
        img.save(os.path.join(source_path, str(file_num).zfill(5) + ".jpg"), 'jpeg')
        file_num+=1
    
    print("generate source image finished!")


def padding_img(img: np.ndarray, pad_l, pad_t, pad_r, pad_b):
    height, width, depth = img.shape
    #Adding padding to the left side.
    pad_left = np.full(shape=(height, pad_l, 3), fill_value=255, dtype=np.uint8)
    img = np.concatenate((pad_left, img), axis = 1)

    #Adding padding to the top.
    pad_up = np.full(shape=(pad_t, pad_l + width, 3), fill_value=255, dtype=np.uint8)
    img = np.concatenate((pad_up, img), axis = 0)

    #Adding padding to the right.
    pad_right = np.full(shape=(height + pad_t, pad_r, 3), fill_value=255, dtype=np.uint8)
    img = np.concatenate((img, pad_right), axis = 1)

    #Adding padding to the bottom
    pad_bottom = np.full(shape=(pad_b, pad_l + width + pad_r, 3), fill_value=255, dtype=np.uint8)
    img = np.concatenate((img, pad_bottom), axis = 0)

    return img


def centering_img(img: Image.Image):
    img_arr = np.asarray(img)
    height, width, depth= img_arr.shape
    # cutting
    col_sum = np.where(np.sum(img_arr, axis = 0)<255*3*width*0.999)
    row_sum = np.where(np.sum(img_arr, axis = 1)<255*3*height*0.999)

    y1, y2 = row_sum[0][0], row_sum[0][-1]
    x1, x2 = col_sum[0][0], col_sum[0][-1]
    img_cut = img_arr[y1:y2, x1:x2]

    # padding
    pad_l = int((width-img_cut.shape[1])/2)
    pad_r = width-pad_l-img_cut.shape[1]
    pad_t = int((height-img_cut.shape[0])/2)
    pad_b = height-pad_t-img_cut.shape[0]

    img_pad = padding_img(img_cut, pad_l=pad_l, pad_t=pad_t, pad_r=pad_r, pad_b=pad_b)
    img_ret = Image.fromarray(img_pad, 'RGB')

    return img_ret
