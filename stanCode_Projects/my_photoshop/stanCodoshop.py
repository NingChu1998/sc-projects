"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
"""

import os
import sys
from simpleimage import SimpleImage
import math
from math import sqrt


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    # 算出點與平均rgb最短距離
    color_distance: float = math.sqrt((red - pixel.red) ** 2 + (green - pixel.green) ** 2 + (blue - pixel.blue) ** 2)

    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    # list裡所有pixel 的RGB
    a = 0
    b = 0
    c = 0
    for p in pixels:
        a += p.red
        b += p.green
        c += p.blue
    n_avg_list = [a // len(pixels), b // len(pixels), c // len(pixels)]
    return n_avg_list


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    """avg_p = get_average(pixels)
    dist_min = 255
    v1 = pixels[0]
    red = avg_p[0]
    green = avg_p[1]
    blue = avg_p[2]
    for p in pixels:
        v2 = get_pixel_dist(p, red, green, blue)
        if v2 < dist_min:
            dist_min = v2
            v1 = p
    return v1"""
    #  先用get_average出距離要用的平均RGB值 再用變數去存
    avg_p = get_average(pixels)
    red = avg_p[0]
    green = avg_p[1]
    blue = avg_p[2]
    dist_list = []
    for p in pixels:
        # 算出每個pixel 在 list 的距離 加入到 dist_list
        v2 = get_pixel_dist(p, red, green, blue)
        dist_list.append(v2)
    # 用字典存入兩個list key = pixels （裡面位置）, value = 算出的句點
    d = dict(zip(pixels, dist_list))
    # 找出最小值 return the best pixel
    min_value = min(d.values())
    min_pixel = []
    for i, j in d.items():
        if j == min_value:
            min_pixel.append(i)
    return min_pixel[0]




def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    # for loop 去存位置 一定要x ,y
    for x in range(width):
        for y in range(height):
            # 等下要存的list
            pixel_list = []
            for img in images:
                # 讀取所有圖片的x,y 存成list
                orig_pixel = img.get_pixel(x, y)
                pixel_list.append(orig_pixel)
            # 串燒n張圖片 去找出最好點 去貼在畫布上填上RGB
            best_img = get_best_pixel(pixel_list)
            new_pixel1 = result.get_pixel(x, y)

            new_pixel1.red = best_img.red
            new_pixel1.blue = best_img.blue
            new_pixel1.green = best_img.green
            # new_img = i.get_pixel(x, y)
            # new_pixel1.red = new_img.red
            # new_pixel1.green = new_img.green
            # new_pixel1.blue = new_img.blue


    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
