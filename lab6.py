from PIL import Image, ImageFilter
def z1():
    file = "fishing.jpg"
    with Image.open(file) as img:
        img.load()
    img.show()
    width, height = img.size
    format = img.format
    mode = img.mode
    print('Ширина: ', width)
    print('Высота: ', height)
    print('Формат: ', format)
    print('Цветовая модель: ', mode)

def z2():
    file = "fishing.jpg"
    with Image.open(file) as img:
        img.load()
    resize_img = img.resize((img.width // 3, img.height // 3))
    resize_img.save("resize_fishing.jpg")
    vertical_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    vertical_img.save('vertical_fishing.jpg')
    horizontal_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    horizontal_img.save('horizontal_fishing.jpg')

def z3():
    pics = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
    for f in pics:
        with Image.open(f) as pic:
            pic.load()
        new_pic = pic.filter(ImageFilter.FIND_EDGES)
        new_pic.show()
        new_pic.save('new_' + f)

def z4():
    mark = 'watermark.png'
    with Image.open(mark) as pic:
        pic.load()
    image = 'city.jpeg'
    with Image.open(image) as pic1:
        pic1.load()
    pic1.paste(pic, (100,100), pic)
    pic1.save('watermark_city.jpeg')
    pic1.show()

