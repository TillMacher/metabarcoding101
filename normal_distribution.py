import scipy.stats as stats
from scipy.stats import skewnorm
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import scipy.stats as stats

## This script will test y values on their normal distribution

def normal_dist_test(y_values):
    # Perform Shapiro-Wilk test
    shapiro_stat, shapiro_p_value = stats.shapiro(y_values)

    # Check the Shapiro-Wilk test result
    if shapiro_p_value <= 0.05:
        print('Shapiro-Wilk Test: NOT normally distributed data! - Statistic: {}, p-value: {}'.format(shapiro_stat, shapiro_p_value))
    else:
        print('Shapiro-Wilk Test: Normally distributed data! - Statistic: {}, p-value: {}'.format(shapiro_stat, shapiro_p_value))

    # Perform Kolmogorov-Smirnov test
    ks_stat, ks_p_value = stats.kstest(y_values, 'norm')

    # Check the Kolmogorov-Smirnov test result
    if ks_p_value <= 0.05:
        print('Kolmogorov-Smirnov Test: NOT normally distributed data! - Statistic: {}, p-value: {}'.format(ks_stat, ks_p_value))
    else:
        print('Kolmogorov-Smirnov Test: Normally distributed data! - Statistic: {}, p-value: {}'.format(ks_stat, ks_p_value))

    # Determine the overall result based on both tests
    if shapiro_p_value <= 0.05 and ks_p_value <= 0.05:
        result = False  # Data is not normally distributed
    elif shapiro_p_value <= 0.05 or ks_p_value <= 0.05:
        result = 'Investigate'  # Data may not be normally distributed, further investigation needed
    else:
        result = True  # Data is normally distributed

    # Return the result
    return result


def normal_dist_plot(y_values):
    # Create subplots
    fig = make_subplots(rows=1, cols=2, horizontal_spacing=.15, subplot_titles=['Histogram', 'Q-Q plot'])

    # Calculate mean of the dataset
    y_mean = np.mean(y_values)

    # Calculate values for the histogram
    histogram_y = sorted([round(i - y_mean, 1) for i in y_values])
    histogram_y_set = list(set(histogram_y))
    histogram_x = [histogram_y.count(i) for i in histogram_y_set]

    # Add the histogram to the first subplot
    fig.add_trace(go.Bar(x=histogram_y_set, y=histogram_x, marker_color='black'), col=1, row=1)
    fig.update_xaxes(dtick=1, title='Variable', col=1, row=1)
    fig.update_yaxes(title='Count', col=1, row=1)

    # Sort the data for the Q-Q plot
    sorted_data = np.sort(y_values)

    # Calculate expected quantiles for a normal distribution
    expected_quantiles = stats.norm.ppf(np.linspace(0.01, 0.99, len(y_values)))

    # Add the Q-Q plot to the second subplot
    fig.add_trace(go.Scatter(x=expected_quantiles, y=sorted_data, mode='markers', marker_color='black'), col=2, row=1)
    fig.update_xaxes(title='Theoretical Quantiles', col=2, row=1)
    fig.update_yaxes(title='Sample Quantiles', col=2, row=1)

    # Update layout and display the plot
    fig.update_layout(template='simple_white', showlegend=False)
    fig.show()


# create example data
y1 = skewnorm.rvs(a=0,   loc=1,   size=150)
y2 = skewnorm.rvs(a=-100, loc=1,   size=150)
y3 = skewnorm.rvs(a=100,   loc=1,   size=150)

# run example data

# normal distributed
a = normal_dist_test(y1)
normal_dist_plot(y1)

# left skewed
b = normal_dist_test(y3)
normal_dist_plot(y2)

# right skewed
c = normal_dist_test(y3)
normal_dist_plot(y3)

