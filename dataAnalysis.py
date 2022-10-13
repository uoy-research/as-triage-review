"""
Data analysis for the paper. Performed by Billy Lyons

Original was lost in file corruption, issues upgrading to Ubuntu 22.04.

As such reperformed and committed to website and document.
"""
import os
from matplotlib.cbook import boxplot_stats
import numpy as np
import pandas as pd
from pip import main
import seaborn as sns
import matplotlib.pyplot as plt

# Permanently changes the pandas settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

current_directory = os.path.abspath(os.getcwd())

def dataPointAnalysis():
    # Load respective .csv file
    df = pd.read_csv(current_directory + "/csvFiles/dataPointsAndTypes.csv")
    # Delete all unncessary coiumns
    df.drop(['Author', 'Title', 'Year', 'S or V', 'Patient Facing', 'Regular Use', 'Age', 'Notes', 'Illness', 'Unnamed: 11', 'Unnamed: 13'], axis=1, inplace=True)
    # Create Seaborn multi-axis boxplot
    f, axes = plt.subplots(1,3)
    # Remove 0s from data
    retrospective = df['Retrospective'].loc[~(df['Retrospective'] == 0)]
    outliersRetrospective = [y for stat in boxplot_stats(retrospective) for y in stat['fliers']]
    evp = df['EV&P Data'] = df['EV&P Data'].loc[~(df['EV&P Data'] == 0)]
    outliersevp = [y for stat in boxplot_stats(evp) for y in stat['fliers']]
    lTrials = df['Live Trials'] = df['Live Trials'].loc[~(df['Live Trials'] == 0)]
    outlierslTrials = [y for stat in boxplot_stats(lTrials) for y in stat['fliers']]
    sns.boxplot(y = retrospective, orient='v', ax=axes[0], showfliers=False, color="#9b59b6").set(xlabel='Retrospective', ylabel='Number of data points')
    sns.boxplot(y = evp, orient='v', ax=axes[1], showfliers=False, color = '#3498db').set(xlabel='EV&P', ylabel='Number of data points')
    sns.boxplot(y = lTrials, orient='v', ax=axes[2], showfliers=False, color='#2ecc71').set(xlabel='Live Trials', ylabel='Number of data points')
    plt.show()

    print(f"Outliers for Retrospective: {outliersRetrospective}")
    print(f"Outliers for Retrospective: {outliersevp}")
    print(f"Outliers for Retrospective: {outlierslTrials}")   
    exit()
    
def stage5Analaysis():
    # Load respective .csv file
    df = pd.read_csv(current_directory + "/csvFiles/stage5Data.csv")
    
    pass
def stagesAnalysis():
    # Load respective .csv file
    df = pd.read_csv(current_directory + "csvFiles/stagesData.csv")
    
    pass
def technologiesAnalysis():
    # Load respective .csv file
    df = pd.read_csv(current_directory + "csvFiles/technologiesData.csv")
    pass

def main():
    dataPointAnalysis()
    

if __name__ == "__main__":
    main()
    exit()