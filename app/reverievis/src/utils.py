from math import pi
import pandas as pd
import numpy as np

colors_pallate = ['#FF6D60', '#6DA9E4', '#F7D060', '#BE6DB7']

def create_data_structure(data, category, values):
    data_radar = {}
    data_category = data[category].unique()
    data_values = data[values].to_numpy()
    for idx,val in enumerate(data_values):
        result = val
        result = np.append(result, val[:1])
        data_radar[data_category[idx]] = result
    
    return data_radar


def normalize_minmax(data, category, data_minmax, vmin=0, vmax=1):
    value = data.copy()
    data_scaled = data.copy()
    data_scaled = data_scaled[[category]]
    value_scaled = value.drop(category, axis=1)
    if vmin != 0 or vmax != 1:
        for column in value_scaled.columns:
            value_scaled[column] = (value_scaled[column] - vmin) / (vmax - vmin)
    elif data_minmax is not None:
        for column in value_scaled.columns:
            value_scaled[column] = (value_scaled[column] - data_minmax[column]['min']) / (data_minmax[column]['max'] - data_minmax[column]['min']) 
    else:
        for column in value_scaled.columns:
            value_scaled[column] = (value_scaled[column] - value_scaled[column].min()) / (value_scaled[column].max() - value_scaled[column].min())   

    data_full = pd.concat([data_scaled, value_scaled], axis=1)
    return data_full 


def create_angles(length):
    angles = [n / float(length) * 2 * pi for n in range(length)]
    angles += angles[:1]

    return angles


def draw_radar(ax, data_radar, angles, colors_alpha, marker, marker_size, colors):
    count = 0

    if colors is not None:
        for key in data_radar.keys():
            ax.plot(angles, data_radar[key], linewidth=1, 
                    linestyle='solid', marker=marker, 
                    markersize=marker_size,
                    color=colors[count], label=f"{key}")
            ax.fill(angles, data_radar[key], color=colors[count], alpha=colors_alpha)
            count += 1
    else:
        for key in data_radar.keys():
            ax.plot(angles, data_radar[key], linewidth=1, 
                    linestyle='solid', marker=marker, 
                    markersize=marker_size,
                    color=colors_pallate[count], label=f"{key}")
            ax.fill(angles, data_radar[key], color=colors_pallate[count], alpha=colors_alpha)
            count += 1


def legend_styling(ax, style, col):
    if style == 'bottom':
        ax.legend(loc='lower center',
            bbox_to_anchor=(0.5, -0.17),
            ncol=col,
            borderpad=1,
            frameon=False,
            fontsize=8
            )
    elif style == 'top':
        ax.legend(loc='upper center',
            bbox_to_anchor=(0.5, 1.17),
            ncol=col,
            borderpad=1,
            frameon=False,
            fontsize=8
            )


def get_ymax_lim(data):
    ymax = 0

    for key in data.keys():
        temp = data[key].max()
        if ymax < temp:
            ymax = temp
    
    if ymax < 1:
        ymax = 1
    return ymax


def get_yticks(ylim_max, circle):
    yticks_label = np.linspace(0,ylim_max, circle).astype(int)
    yticks_label = yticks_label.astype(str)
    return np.linspace(0,ylim_max, circle), yticks_label


def put_title(ax, title, y=1.08):
    ax.set_title(title, y=y, fontsize=12, fontweight='bold', color='black')