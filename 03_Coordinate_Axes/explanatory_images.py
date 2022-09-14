import os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd

"""Helper module that creates images for explanation purposes."""

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

    fig.suptitle('A Square that looks different based on the Aspect Ratio')
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
    fig.tight_layout()
    return fig


def plot_temps(ax, xArr, yArr, aspect_ratio, x_label, y_label, title):

    ax.plot(xArr, yArr)
    # Adding Text
    for i, txt in zip([0, 3, 6, 9], ['Jan 1st', 'Apr 1st', 'Jul 1st', 'Oct 1st']):
        ax.text(xArr[i], yArr[i] + 1 , txt, verticalalignment='bottom', horizontalalignment='center')
        ax.scatter(xArr[i], yArr[i], s = 15, marker = 'o', c = 'black' )
        
    # Plotting Reference Line
    ax.plot(np.arange(50,85+1,1), np.arange(50,85+1,1), 
            linestyle = '--', color = 'firebrick', label='Slope = 1:1')
      
    # Adding Testing Square
    square_props = dict(edgecolor = 'red', alpha = 0.3, fill = True, lw = 2,
                        facecolor ='red')
    square = Rectangle((55, 70), width = 5, height = 5, **square_props)
    ax.add_patch(square)
    ax.text(57.5, 72.5 , 'Test', verticalalignment='center', horizontalalignment='center', 
            **dict(fontname="Arial", fontsize='large', fontweight = 'bold', color = 'black'))
    
    # Aesthetics
    ax.grid()
    ax.set_axisbelow(True)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_aspect(aspect_ratio)
    ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
    ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
    ax.set_title(title)  
        
    return ax