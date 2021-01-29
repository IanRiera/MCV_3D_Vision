import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

def line_draw(line, canv, size):
    def get_y(t):
        return -(line[0] * t + line[2]) / line[1]

    def get_x(t):
        return -(line[1] * t + line[2]) / line[0]

    w, h = size

    if line[0] != 0 and abs(get_x(0) - get_x(w)) < w:
        beg = (get_x(0), 0)
        end = (get_x(h), h)
    else:
        beg = (0, get_y(0))
        end = (w, get_y(w))
    canv.line([beg, end], width=4)


def plot_img(img, do_not_use=[0], axis=None, save=False, title=None):
    plt.figure(do_not_use[0])
    do_not_use[0] += 1
    if axis is not None:
        plt.imshow(img, extent=axis)
    else:
        plt.imshow(img)

    if save:
        if not os.path.isdir('./outputs'):
            os.mkdir('./outputs')
        plt.savefig('./outputs/' + title)
