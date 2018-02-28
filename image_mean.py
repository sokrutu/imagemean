# -*- coding: utf-8 -*-
from k_means import k_means
from PIL import Image

def main():
    # test = k_means([[250,250],[1,1],[1,2],[2,1],[10,10],[240,240]], 2)
    # print(test)

    image = Image.open("a.jpg")
    data = __decompose(image)
    res = k_means(data,4)
    __compose(res[0], res[1], image)
    image.save("b.jpg")
    return 0

def __decompose(image):
    # TODO: ignores Alpha channel
    width, height = image.size
    N = width*height
    pixels = image.load()
    data = [None]*N
    for y in range(0,height):
        for x in range(0,width):
            data[width*y+x] = pixels[x,y][:3] # only RGB (last is Alpha)

    return data

def __compose(means, assignments, image):
    width, height = image.size
    N = width * height

    # Re-create "data"
    data = [means[x] for i,x in enumerate(assignments)]

    # Make sure its only integers
    for e in data:
        for i in range(0,3): # TODO only for Dim = 3
            e[i] = int(round(e[i]))

    pixels = image.load()
    for y in range(0,height):
        for x in range(0,width):
            pixels[x, y] = tuple(data[width*y+x])
    return

if __name__ == "__main__":
    main()