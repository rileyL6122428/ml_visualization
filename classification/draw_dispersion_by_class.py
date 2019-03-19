from matplotlib import pyplot as plt
import numpy as np


def draw_dispersion(series, color, base_height, mean_std_offset, quantile_offset, aggregate_height):
    text_alignment = 'center'

    plt.scatter(
        x=series,
        y=np.zeros(series.size) + base_height,
        marker='d',
        alpha=0.1,
        color=color
    )

    plt.text(
        series.mean() - series.std(),
        base_height + mean_std_offset,
        '-σ',
        color=color,
        horizontalalignment=text_alignment
    )

    plt.text(
        series.mean(),
        base_height + mean_std_offset,
        'µ',
        color=color,
        horizontalalignment=text_alignment
    )

    plt.text(
        series.mean() + series.std(),
        base_height + mean_std_offset,
        '+σ',
        color=color,
        horizontalalignment=text_alignment
    )

    plt.text(
        series.quantile(.15),
        base_height + quantile_offset,
        '.15',
        color=color,
        horizontalalignment=text_alignment
    )

    plt.text(
        series.quantile(.5),
        base_height + quantile_offset,
        '.5',
        color=color,
        horizontalalignment=text_alignment
    )

    plt.text(
        series.quantile(.85),
        base_height + quantile_offset,
        '.85',
        color=color,
        horizontalalignment=text_alignment
    )

    plt.text(
        series.mean(),
        base_height + aggregate_height,
        'Total = %s' % series.size,
        color=color,
        horizontalalignment=text_alignment
    )


def draw_dispersion_by_class(series, affirmative_series, negative_series, affirmative_label='', negative_label='', title=''):
    dispersion_drawings = [
        {
            'series': series,
            'color': '#33cc33',
            'base_height': 0,
            'mean_std_offset': -0.15,
            'quantile_offset': 0.1,
            'aggregate_height': -0.3
        },
        {
            'series': negative_series,
            'color': '#007acc',
            'base_height': -1,
            'mean_std_offset': 0.1,
            'quantile_offset': 0.2,
            'aggregate_height': 0.3
        },
        {
            'series': affirmative_series,
            'color': '#ff8000',
            'base_height': 1,
            'mean_std_offset': -0.2,
            'quantile_offset': -0.3,
            'aggregate_height': -0.4
        },
    ]

    for drawing in dispersion_drawings:
        draw_dispersion(
            series=drawing['series'],
            color=drawing['color'],
            base_height=drawing['base_height'],
            mean_std_offset=drawing['mean_std_offset'],
            quantile_offset=drawing['quantile_offset'],
            aggregate_height=drawing['aggregate_height']
        )

    plt.legend(('Unclassified', negative_label, affirmative_label))
    plt.title(title)
    mng = plt.get_current_fig_manager()
    mng.resize(800, 400)
    plt.show()
