import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')

class Dataset:
    def __init__(self):
        self.df = pd.read_csv('dataset\weatherHistory.csv')
    def plotBar(self,col_name):
        return sns.countplot(x=col_name,data=self.df)
    def plotHist(self,col_name):
        return sns.distplot(self.df[col_name])
    def plotScatter(self,col_name1,col_name2):
        return sns.scatterplot(x=col_name1,y=col_name2,data=self.df)
    def plotBox(self,col_name1,col_name2):
        return sns.boxplot(x=col_name1,y=col_name2,data=self.df)
    