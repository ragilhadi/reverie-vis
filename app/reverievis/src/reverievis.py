import matplotlib.pyplot as plt
from .utils import create_data_structure, normalize_minmax\
                    ,create_angles, draw_radar\
                    ,legend_styling, put_title\
                    ,get_ymax_lim, get_yticks
from math import pi


def radar(data, category, values, 
              data_minmax = None,
              scaled=None, colors=None, colors_alpha=0.2,
              show_legend=True,
              legend_style='bottom', legend_col=2,
              title=None, title_position=1.08,
              circle=5,
              marker=None, marker_size=3, 
              show_label=False, show_circle = False,
              **kwargs):
    """
    A function to create radar visualization
    """
    if scaled is not None:
        data_norm = normalize_minmax(data=data, category=category, 
                                     data_minmax=data_minmax,
                                     vmin=scaled[0], vmax=scaled[1])
    elif data_minmax is not None:
        data_norm = normalize_minmax(data=data, category=category,
                                     data_minmax=data_minmax)
    else:
        data_norm = data
    data_radar = create_data_structure(data_norm, category, values)
    angles = create_angles(len(values))
    ylim_max = get_ymax_lim(data_radar)
    yticks, yticks_label = get_yticks(ylim_max, circle)

    if show_circle == False:
        yticks = []

    plt.figure(figsize=(16,6))
    ax = plt.subplot(111, polar=True)
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angles[:-1], values)
    ax.set_rlabel_position(0)
    if show_label == True:
        ax.set_yticks(yticks, yticks_label, color="grey", size=7)
    elif show_label == False:
        ax.set_yticks(yticks, [], color="grey", size=7)
    ax.set_ylim(0,ylim_max)

    if colors is not None:
        draw_radar(ax=ax, data_radar=data_radar, 
                   angles=angles, colors=colors,
                   marker=marker, marker_size=marker_size,
                   colors_alpha=colors_alpha)
    else:
        draw_radar(ax=ax, data_radar=data_radar, 
                   colors=colors,
                   marker=marker, marker_size=marker_size,
                   angles=angles, colors_alpha=colors_alpha)
    
    if title is not None:
        put_title(ax,title, title_position)

    if show_legend:
        legend_styling(ax, legend_style, legend_col)


def get_minmax(data, columns) -> dict:
    """
    Function to get min value and max value of the column data
    """
    data = data[columns]
    data_minmax = {}
    for column in data.columns:
        data_minmax[column] = {'max': data[column].max(),
                               'min': data[column].min()}
    return data_minmax