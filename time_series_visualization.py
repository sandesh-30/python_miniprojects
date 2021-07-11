## time series data visualization
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv" , parse_dates=True , index_col= "date")

# Clean data
df = df.drop(df[ (df["value"] <= df["value"].quantile(0.025)) | (df["value"] >= df["value"].quantile(0.975))].index)


def draw_line_plot():
    # Draw line plot
    fig = plt.figure()
    plt.plot(df["value"] , color='r')
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.strftime('%B')
    #months = list(set(df_bar["month"]))
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December'] 
    df_bar= df_bar.groupby(['year' , 'month'])['value'].mean()
    df_bar = df_bar.unstack()
   
    # Draw bar plot
    ax = df_bar.plot(kind= 'bar',figsize=(14,6) , legend=True)
    fig = ax.get_figure()
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title= 'Months',fontsize = 7,  labels = months)
    #plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box.sort_values(by=['year','date'], ascending=[False, True], inplace=True)
    # Draw box plots (using Seaborn)
    fig = plt.figure(figsize=(14,6))
    ax1 = fig.add_subplot(121)
    ax1 = sns.boxplot(x = "year", y = "value", data = df_box)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax2 = fig.add_subplot(122)
    ax2=sns.boxplot(x='month',y='value',data=df_box)
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')






    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
