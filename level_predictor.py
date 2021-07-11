### sea level predictor

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    fig, ax= plt.subplots()
    ax.scatter(x = df["Year"] , y = df["CSIRO Adjusted Sea Level"])


    # Create first line of best fit
    results = linregress(x = df["Year"].values , y = df["CSIRO Adjusted Sea Level"].values)
    m = results.slope
    c = results.intercept

    #using y=m*X+c to draw line

    X = range(1880 , 2051) #extending x-axis till 2050

    ax.plot(X ,m*X + c)


    # Create second line of best fit
    #filtering dataset
    new_df = df[df["Year"] >= 2000]
    year_new = new_df["Year"].values
    CSIRO_new = new_df["CSIRO Adjusted Sea Level"].values
    new_results = linregress(x = year_new , y = CSIRO_new)
    m_new = new_results.slope
    c_new = new_results.intercept
    X_new = range(2000 , 2051 ,1)
    
    #second line of best fit
    ax.plot(X_new , m_new*X_new + c_new)


    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
