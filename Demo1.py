from os import stat
import pandas as pd 
import csv 
import statistics
import plotly.figure_factory as ff 
import plotly.graph_objects as go
import random 
df=pd.read_csv("Data.csv")
data=df["temp"].tolist()
populationMean=statistics.mean(data)
standarddeviation=statistics.stdev(data)
print(populationMean)
print(standarddeviation)

def randomsetofmean(counter):
    datasets=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(data))
        value=data[randomindex]
        datasets.append(value)
    mean=statistics.mean(datasets)
    return mean
def showfigure(meanlist):
    df=meanlist
    mean=statistics.mean(meanlist)
    print(mean)
    figure=ff.create_distplot([df],["temprature"],show_hist=False)
    figure.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    figure.show()
def setup():
    mean_list=[]    
    for i in  range(0,1000):
        setofmeans=randomsetofmean(100)
        mean_list.append(setofmeans)
    
    showfigure(mean_list)
setup()
def standarddeviation():
    mean_list=[]    
    for i in  range(0,1000):
        setofmeans=randomsetofmean(100)
        mean_list.append(setofmeans)
    standarddeviation1=statistics.stdev(mean_list)
    print(standarddeviation1)
standarddeviation()


