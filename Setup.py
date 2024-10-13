#imports
import numpy as np
import scipy as sp
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from sklearn.decomposition import PCA

import neuscitk as ntk

#get dataset
dataset = ntk.LabChartDataset('/Users/prestonsands/Desktop/NEUSCI 302/Lab1/BWPSPA_Lab1_flipped.mat')

#organize blocks into pages
page_map = {
    'spontaneousTrials' : list(range(1,11)),
    'spine3trials' : list(range(11,16)),
    'spine4trials' : list(range(16,21)),
    'spine2trials' : list(range(21,26)),
    'spine1trials' : list(range(26,31)),
    'freqTrials' : list(range(31,36))
}

dataset.organize_by_pages(page_map)

#define new datasets
spontaneousTrials = dataset.get_page('spontaneousTrials')
spine1trials= dataset.get_page('spine1trials')
spine2trials= dataset.get_page('spine2trials')
spine3trials= dataset.get_page('spine3trials')
spine4trials= dataset.get_page('spine4trials')
freqTrials= dataset.get_page('freqTrials')

#concatonated groups
spontaneousConcat = dataset.concat_blocks(range(1,11))
spine1concat = dataset.concat_blocks(range(11,16))
spine2concat = dataset.concat_blocks(range(16,21))
spine3concat = dataset.concat_blocks(range(21,26))
spine4concat = dataset.concat_blocks(range(26,31))

#colors
colors = {
    'red': '#FF4F4F',
    'red1': '#FFBBBB',
    'red2': '#FF9B9B',
    'red3': '#FF8383',
    'red4': '#FF6969',
    'red5': '#FF4F4F',
    'red6': '#C73737',
    'red7': '#871C1C',
    'red8': '#4B0202',
    
    'gold': '#FFAE21',
    'gold1': '#FDE8C1',
    'gold2': '#FEDF94',
    'gold3': '#FED96C',
    'gold4': '#FFC044',
    'gold5': '#FFAE21',
    'gold6': '#D27D18',
    'gold7': '#A15B0E',
    'gold8': '#693703',

    'aqua': '#01CFCC',
    'aqua1': '#BFF8D0',
    'aqua2': '#96EFCF',
    'aqua3': '#6DE6CE',
    'aqua4': '#3ADBD8',
    'aqua5': '#01B0CF',
    'aqua6': '#0299AD',
    'aqua7': '#04768C',
    'aqua8': '#07435C',

    'blue': '#6480FF',
    'blue1': '#D0F2FF',
    'blue2': '#B2DBFF',
    'blue3': '#96BCFF',
    'blue4': '#7EA4FF',
    'blue5': '#647DFF',
    'blue6': '#535AD1',
    'blue7': '#3A29B8',
    'blue8': '#3F0F8D',

    'green1': '#94DD8B',
    'green2': '#0BB68C',
    'green3': '#038174',
}

#define cluster comparer
def compare_clusters(group_1, group_2, group_1_name='Group 1', group_2_name='Group 2') -> tuple[np.ndarray, np.ndarray]:

    pca = PCA().fit(group_1._waveforms)
    group_1_transformed = pca.transform(group_1._waveforms)
    group_2_transformed = pca.transform(group_2._waveforms)

    group_1_labels = group_1.labels
    group_2_labels = group_2.labels

    fig, ax = plt.subplots(figsize=(10, 8))
    counter = 0

    # Plot for group 1
    for idx, cluster in enumerate(np.unique(group_1_labels)):
        mask = group_1_labels == cluster
        ax.scatter(
            group_1_transformed[mask, 0],
            group_1_transformed[mask, 1],
            c=f'C{counter}',
            edgecolors='black',
            linewidths=0.5,
            label=f'{group_1_name} cluster {cluster}'
        )
        counter += 1

    # Plot for group 2
    for idx, cluster in enumerate(np.unique(group_2_labels)):
        mask = group_2_labels == cluster
        ax.scatter(
            group_2_transformed[mask, 0],
            group_2_transformed[mask, 1],
            c=f'C{counter}',
            edgecolors='black',
            linewidths=0.5,
            marker='X',
            label=f'{group_2_name} cluster {cluster}'
        )
        counter += 1

    ax.set_xlabel(f'{group_1_name} PC1')
    ax.set_ylabel(f'{group_2_name} PC2')

    # Place the legend outside the plot to the right
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), frameon=False)
    
    plt.tight_layout()
    plt.show()

    return group_1_transformed, group_2_transformed
