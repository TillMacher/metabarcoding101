# Import necessary libraries
from scipy.stats import wilcoxon
from scipy.stats import ttest_ind
from scipy.stats import ttest_rel
import numpy as np
from scipy.stats import skewnorm
import plotly.graph_objects as go

## two independent forests
p_value = 1
# Continue looping until p-value is less than 0.05
while p_value >= 0.05:
    # Generate random data for Forest A and Forest B using skewnorm distribution
    y1 = skewnorm.rvs(a=0, loc=20, size=50)
    y2 = skewnorm.rvs(a=0, loc=15, size=50)
    # Perform independent t-test to compare the means of two samples
    tt_stat, p_value = ttest_ind(y1, y2)
    # Create a title for the plot
    title = 'statistic={}, p-value={}'.format(round(tt_stat,2), round(p_value,3))
    # Create a box plot for Forest A and Forest B
    fig = go.Figure()
    fig.add_trace(go.Box(y=y1, boxpoints='all', jitter=0.6, pointpos=-1.8, name='Forest A', marker_color='black'))
    fig.add_trace(go.Box(y=y2, boxpoints='all', jitter=0.6, pointpos=-1.8,  name='Forest B', marker_color='black'))
    # Customize plot layout
    fig.update_yaxes(title='# invasive species', rangemode='tozero')
    fig.update_layout(template='simple_white', height=500, width=500, showlegend=False, title=title)
    # Save the plot as an image
    fig.show()

## two dependent sample types
p_value = 0
# Continue looping until p-value is greater than 0.05
while p_value <= 0.05:
    # Generate random data for Method A and Method B using skewnorm distribution
    y1 = skewnorm.rvs(a=0, loc=10, size=50)
    y2 = skewnorm.rvs(a=0, loc=10, size=50)
    # Perform paired t-test to compare the means of two dependent samples
    tt_stat, p_value = ttest_rel(y1, y2)
    # Create a title for the plot
    title = 'statistic={}, p-value={}'.format(round(tt_stat,2), round(p_value,3))
    # Create a box plot for Method A and Method B
    fig = go.Figure()
    fig.add_trace(go.Box(y=y1, boxpoints='all', jitter=0.6, pointpos=-1.8, name='Method A', marker_color='black'))
    fig.add_trace(go.Box(y=y2, boxpoints='all', jitter=0.6, pointpos=-1.8,  name='Method B', marker_color='black'))
    # Customize plot layout
    fig.update_yaxes(title='# indicator species', rangemode='tozero')
    fig.update_layout(template='simple_white', height=500, width=500, showlegend=False, title=title)
    # Save the plot as an image
    fig.show()

## two dependent sample types
p_value = 1
# Continue looping until p-value is less than 0.05
while p_value >= 0.05:
    # Generate random data for Year 1 and Year 2 using integer values
    y1 = [np.random.randint(40,200) for i in range(1,50)]
    y2 = [np.random.randint(30,250) for i in range(1,50)]
    # Perform Wilcoxon signed-rank test to compare two dependent samples
    tt_stat, p_value = wilcoxon(y1, y2)
    # Create a title for the plot
    title = 'statistic={}, p-value={}'.format(round(tt_stat,2), round(p_value,3))
    # Create a box plot for Year 1 and Year 2
    fig = go.Figure()
    fig.add_trace(go.Box(y=y1, boxpoints='all', jitter=0.6, pointpos=-1.8, name='Year 1', marker_color='black'))
    fig.add_trace(go.Box(y=y2, boxpoints='all', jitter=0.6, pointpos=-1.8,  name='Year 2', marker_color='black'))
    # Customize plot layout
    fig.update_yaxes(title='# invasive species', rangemode='tozero')
    fig.update_layout(template='simple_white', height=500, width=500, showlegend=False, title=title)
    # Save the plot as an image
    fig.show()
