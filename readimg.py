from PIL import Image

#img = Image.open("pic.png")
img = Image.open("map.png")

print()

for i in range(580):
    for j in range(592):

        r, g, b = img.getpixel((i, j))
        if (b > g and b > r):  # 对蓝色进行判断
            b = 0
            g = 0
            r = 0
        else:
            b=255
            g=255
            r=255

        img.putpixel((i, j), (r, g, b))
print(type(img))
img.save('mapresult.png')



