import seaborn as sns
from matplotlib import pylab as plt
from statsmodels.graphics.gofplots import qqplot

# checking and visualizing the type of distribution of a feature column
def univariate_analysis(process_data, color, title1, title2):
    '''
             Univariate Data Analysis
    '''

    fig, (ax1, ax2) = plt.subplots(  # subplots
        ncols=2,  # num of cols
        nrows=1,  # num of rows
        figsize=(20, 6)  # set the width and high
    )

    # TO CREATE 2 PLOTS BELOW : Distplot & ggplot
    sns.distplot(  # create a distplot visualization
        process_data,  # data
        ax=ax1,  # axes 1
        kde=True,  # kde
        color=color  # color
    )

    ax1.set_title(  # set the title 1
        title1,
        weight="bold",  # weight
        fontname="monospace",  # font-name
        fontsize=25,  # font-size
        pad=30  # padding
    )

    qqplot(  # qqplot (quantile plot)
        process_data,  # data
        ax=ax2,  # axes 2
        line='s'  # line
    )

    ax2.set_title(  # set the title 2
        title2,
        weight="bold",  # weight
        fontname="monospace",  # font-name
        fontsize=25,  # font-size
        pad=30  # padding
    )

    return plt.show()  # returning the figure
