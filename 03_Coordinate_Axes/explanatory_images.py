import os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import pandas as pd


def plot_squares(figsize = (16,8)):

    fig, ax = plt.subplots(nrows=1, ncols=3, figsize = figsize)
    x = np.arange(0,11,1)
    y = x
    square_props = dict(edgecolor = 'red', alpha = 0.3, fill = True, lw = 2,
                        facecolor ='red')
    ratios = ['equal', 2, 0.5]
    ratios_label = ['1:1', '1:2', '2:1']

    for axes, asp_ratio, asp_ratio_str in zip(ax, ratios, ratios_label):
        axes.grid()
        axes.set_axisbelow(True)
        axes.set_xlim(0,10)
        axes.set_ylim(0,10)
        axes.set_aspect(asp_ratio)
        axes.set_title('Aspect Ratio (w:h) ' + asp_ratio_str)
        square = Rectangle((4, 4), width = 2, height = 2, **square_props)
        axes.add_patch(square)

    fig.suptitle('A Square that looks different based on Aspect Ratio')
    return fig


def plot_squares_longer_xaxis(figsize = (16,8)):

    fig, ax = plt.subplots(nrows=1, ncols=3, figsize = figsize)
    x = np.arange(0,11,1)
    y = x
    square_props = dict(edgecolor = 'red', alpha = 0.3, fill = True, lw = 2,
                        facecolor ='red')
    ratios = ['equal', 2, 0.5]
    ratios_label = ['1:1', '1:2', '2:1']

    for axes, asp_ratio, asp_ratio_str in zip(ax, ratios, ratios_label):
        axes.grid()
        axes.set_axisbelow(True)
        axes.set_xlim(0,20)
        axes.set_ylim(0,10)
        axes.set_aspect(asp_ratio)
        axes.set_title('Aspect Ratio (w:h) ' + asp_ratio_str)
        square = Rectangle((4, 4), width = 2, height = 2, **square_props)
        axes.add_patch(square)
    
    fig.suptitle("X-axis 0-20 and Y-axis 0-10.")
    return fig