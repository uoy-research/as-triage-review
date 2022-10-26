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
from upsetplot import plot
sns.set(rc={'savefig.dpi':200})

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

def illnessComparison():
    # Load respective .csv file
    df = pd.read_csv(current_directory + "/csvFiles/dataPointsAndTypes.csv")
    # Delete all unncessary coiumns
    df.drop(['Author', 'Title', 'Year', 'S or V', 'Patient Facing', 'Regular Use', 'Age', 'Notes', 'EV&P Data', 'Live Trials', 'Retrospective', 'Unnamed: 11', 'Unnamed: 13'], axis=1, inplace=True)
    to_groupby = list(df.columns.values)
    # Groupby and count data
    grouped = df.groupby(to_groupby).size().sort_values(ascending=False).reset_index(name='Counts')
    sns.barplot(data=grouped, x="Illness", y="Counts")
    plt.xticks(rotation=45, horizontalalignment='right')
    plt.xlabel('Illness considered', fontweight='bold')
    plt.ylabel('Counts', fontweight='bold')
    plt.tight_layout()
    plt.show()

def dataCombinationsAnalysis():
    # Load respective .csv file
    df = pd.read_csv(current_directory + "/csvFiles/dataPointsAndTypes.csv")
    # Delete all unncessary coiumns
    df.drop(['Author', 'Title', 'Year', 'Patient Facing', 'Regular Use', 'Age', 'Notes', 'Illness', 'Unnamed: 11', 'Unnamed: 13'], axis=1, inplace=True)
    df = df.mask(df>0,1)
    to_groupby = list(df.columns.values)
    # Groupby and count data
    grouped = df.groupby(to_groupby).size().sort_values(ascending=False)
    # Plot upset plot
    plot(grouped, show_counts=True)
    plt.show()

def stage5Analysis():
    # Load respective .csv file
    df = pd.read_csv(current_directory + "/csvFiles/stage5Data.csv")
    # Delete unnecessary columns
    df.drop(['Author','Title', 'Unnamed: 26'], axis=1, inplace=True)
    to_groupby = list(df.columns.values)
    # Set NaN to 0
    df = df.fillna(0)
    # Groupby and count data
    grouped = df.groupby(to_groupby).size().sort_values(ascending=False)
    # Plot upset plot
    plot(grouped, show_counts=True)
    plt.show()   
    pass

def stagesAnalysis():
    # Load respective .csv file
    df = pd.read_csv(current_directory + "/csvFiles/stagesData.csv", skipfooter=2)
    # Delete unnecessary columns
    df.drop(['Analysis - Stages', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 18'], axis=1, inplace=True)
    # Skip first two rows
    df = df.iloc[1:]
    # Reset column headers
    new_header = df.iloc[0] #grab the first row for the header
    df = df[1:] #take the data less the header row
    df.columns = new_header #set the header row as the df header
    # Drop extraneous columns
    df.drop(['Author', 'Title', 'Year','which system'], axis=1, inplace=True)
    # Set occupied to 1
    df = df.notna().astype(int)
    # Set NaN to 0
    df = df.fillna(0)
    # Groupby and count data
    grouped = df.groupby(['0','1','2','3','4','5']).size().sort_values(ascending=False)
    # Plot upset plot
    plot(grouped, show_counts=True)
    plt.show()
    pass

def technologiesAnalysis():
    # Load respective .csv file
    df = pd.read_csv(current_directory + "/csvFiles/technologiesData.csv")
    total_tech = df[["Technology", "Count"]]
    # Plot top 10 largest techs
    sns.barplot(data=total_tech.nlargest(10, 'Count'), x="Technology", y = "Count")
    plt.xticks(rotation=45, horizontalalignment='right')
    plt.xlabel('Technology', fontweight='bold')
    plt.ylabel('Counts', fontweight='bold')
    plt.tight_layout()
    pass

def technologiesComboAnalysis():
    # Load respective .csv file
    df = pd.read_csv(current_directory + "/csvFiles/technologiesData.csv")
    total_tech = df[["Technology", "Count"]]
    # Plot top 10 largest techs
    sns.barplot(data=total_tech.nlargest(10, 'Count'), x="Technology", y = "Count")
    plt.xticks(rotation=45, horizontalalignment='right')
    plt.xlabel('Technology', fontweight='bold')
    plt.ylabel('Counts', fontweight='bold')
    plt.tight_layout()
    plt.show()
    pass

def mostSuccessfulResults():
    # Load respective .csv file
    df = pd.read_csv(current_directory + "/csvFiles/hardwareAndMostSuccessful.csv", skipfooter=9)
    # Delete unnecessary columns
    df.drop(['Technology', 'Count', 'Unnamed: 2', 'Hardware', 'Hardware Count', 'Unnamed: 5', 'Author', 'Title', 'Unnamed: 8'], axis=1, inplace=True) 
    to_groupby = list(df.columns.values)
    # Groupby and count data
    grouped = df.groupby(to_groupby).size().sort_values(ascending=False).reset_index(name='Counts')
    print(grouped)
    sns.barplot(data=grouped, x="Best", y="Counts")
    plt.xticks(rotation=45, horizontalalignment='right')
    plt.xlabel('Reportedly most successful algorithm or combination', fontweight='bold')
    plt.ylabel('Counts', fontweight='bold')
    plt.tight_layout()
    plt.show()

def main():
    # illnessComparison()
    # dataPointAnalysis()
    dataCombinationsAnalysis()
    stagesAnalysis()
    stage5Analysis()
    # technologiesAnalysis()
    # technologiesComboAnalysis()
    # mostSuccessfulResults()

if __name__ == "__main__":
    main()
    exit()