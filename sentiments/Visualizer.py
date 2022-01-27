import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from wordcloud import WordCloud, STOPWORDS
from sentiments import MachineLearning

class Visualizer():
    def __init__(self):
        return

    def bar(self, x_data, y_data, title, x_label, y_label, output_file):
        fontsize = 10
        print("Generating {} Bar".format(title))
        plt.bar(x_data,y_data)
        plt.title(title)
        plt.xlabel(x_label, fontsize=fontsize, labelpad=10)
        plt.xticks(rotation=45)
        plt.ylabel(y_label, fontsize=fontsize)
        plt.tight_layout()
        plt.show()
        plt.savefig(output_file)
        return

    def multiple_bar(self, x_data, y0_data, y1_data, title, x_label, y0_label, y1_label, y_label, output_file):
        fontsize = 10
        print("Generating {} Pie".format(title))
        x_axis = np.arange(len(x_data))
        plt.bar(x_axis-0.2, y0_data, 0.4, label=y0_label)
        plt.bar(x_axis+0.2, y1_data, 0.4, label=y1_label)
        plt.xticks(x_axis, x_data)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.legend()
        plt.show()
        plt.savefig(output_file)
        return

    def pie(self):

        return

    def multiple_pie(self):
        return

    def wordCloud(self, text, color, title, output_file):
        w = 1600
        h = 800
        margin = 2
        min_font_size = 20
        figsize = (15, 10)
        text_str = ' '.join(str(e) for e in text)
        wordCloud = WordCloud(
            collocations=False, background_color=color, stopwords=set(STOPWORDS), width=w, height=h, margin=margin,
            min_font_size=min_font_size).generate(text_str)
        plt.figure(figsize= figsize)
        plt.imshow(wordCloud, interpolation='bilinear')
        plt.axis('off')
        plt.figtext(0.5, 0.8, title, fontsize = 20, ha='center')
        plt.savefig(output_file)
        plt.show()
        return

    def display_img(self):
        return