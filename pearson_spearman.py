from scipy.stats import pearsonr
from scipy.stats import spearmanr
import numpy as np
import plotly.graph_objects as go

# Generate non-normally distributed linear data and use Spearman correlation
spearman_p = 1
while spearman_p > 0.05:
    # Generate y-values with some variation
    y1 = [i*np.random.randint(15,100)/100 for i in np.arange(0, 100, 1)]
    x1 = [i*np.random.randint(15,100)/100 for i in np.arange(0, 100, 1)]
    # Calculate Spearman correlation and p-value
    spearman_rho, spearman_p = spearmanr(x1, y1)
    title = 'Spearman rho={}, p={}'.format(round(spearman_rho, 2), round(spearman_p, 3))
    # Create a scatter plot
    fig = go.Figure()
    # Calculate the coefficients for the linear regression line
    slope, intercept = np.polyfit(x1, y1, 1)
    # Generate predicted y-values based on the linear regression line
    trend_line_y = [slope * x + intercept for x in x1]
    # Add a trace for the trend line
    fig.add_trace(go.Scatter(x=x1, y=trend_line_y, mode='lines', line=dict(color='grey', width=2), name='Trend Line'))
    # Add data points
    fig.add_trace(go.Scatter(x=x1, y=y1, mode='markers', marker_color='black'))
    # Customize the plot layout
    fig.update_layout(template='simple_white', showlegend=False, width=500, height=500, title=title)
    fig.update_xaxes(showticklabels=False, title='latitude')
    fig.update_yaxes(showticklabels=False, title='# migrating species')
    # Save the plot as a PDF file
    fig.write_image('/Users/tillmacher/Desktop/Paper/metabarcoding101/5_stuff/pearson_spearman_1.pdf')

# Generate normally distributed linear data and use Pearson correlation
pearson_r = 0
while pearson_r >= -0.3:
    # Generate x-values with some variation
    x1 = sorted([i/100*np.random.randint(80,100)/100 for i in range(15,100,1)])  # Adjust the range and number of points as needed
    # Define the mean and standard deviation for the normal distribution
    # Generate random y-values following a normal distribution
    y1 = np.random.normal(loc=0.001, scale=0.001, size=len(x1))
    # Calculate Pearson correlation and p-value
    pearson_r, pearson_p = pearsonr(x1, y1)
    title = 'Pearson r={}, p={}'.format(round(pearson_r, 2), round(pearson_p, 3))
    # Create a scatter plot
    fig = go.Figure()
    # Calculate the coefficients for the linear regression line
    slope, intercept = np.polyfit(x1, y1, 1)
    # Generate predicted y-values based on the linear regression line
    trend_line_y = [slope * x + intercept for x in x1]
    # Add a trace for the trend line
    fig.add_trace(go.Scatter(x=x1, y=trend_line_y, mode='lines', line=dict(color='grey', width=2), name='Trend Line'))
    # Add data points
    fig.add_trace(go.Scatter(x=x1, y=y1, mode='markers', marker_color='black'))
    # Customize the plot layout
    fig.update_layout(template='simple_white', showlegend=False, width=500, height=500, title=title)
    fig.update_xaxes(showticklabels=False, title='pesticide concentration')
    fig.update_yaxes(showticklabels=False, title='# observed species')
    # Save the plot as a PDF file
    fig.write_image('/Users/tillmacher/Desktop/Paper/metabarcoding101/5_stuff/pearson_spearman_2.pdf')

# Generate non-normally distributed linear data and use Spearman and Pearson correlations
spearman_p = 1
while spearman_p > 0.05:
    # Generate y-values and x-values with some variation
    y1 = [i+np.random.randint(-10,15) for i in np.arange(10, 90, 1)]
    x1 = [i+np.random.randint(-10,15) for i in np.arange(10, 90, 1)]
    # Calculate Spearman and Pearson correlations and p-values
    spearman_rho, spearman_p = spearmanr(x1, y1)
    pearson_r, pearson_p = pearsonr(x1, y1)
    title = 'Spearman rho={}, p={}'.format(round(spearman_rho, 2), round(spearman_p, 3))
    # Create a scatter plot
    fig = go.Figure()
    # Calculate the coefficients for the linear regression line
    slope, intercept = np.polyfit(x1, y1, 1)
    # Generate predicted y-values based on the linear regression line
    trend_line_y = [slope * x + intercept for x in x1]
    # Add a trace for the trend line
    fig.add_trace(go.Scatter(x=x1, y=trend_line_y, mode='lines', line=dict(color='grey', width=2), name='Trend Line'))
    # Add data points
    fig.add_trace(go.Scatter(x=x1, y=y1, mode='markers', marker_color='black'))
    # Customize the plot layout
    fig.update_layout(template='simple_white', showlegend=False, width=500, height=500, title=title)
    fig.update_xaxes(showticklabels=False, range=(-0.5, 100.5), title='# species primer A')
    fig.update_yaxes(showticklabels=False, range=(-0.5, 100.5), title='# species primer B')
    # Save the plot as a PDF file
    fig.write_image('/Users/tillmacher/Desktop/Paper/metabarcoding101/5_stuff/pearson_spearman_3.pdf')
