import pandas as pd   
#import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from chart_studio import plotly
from plotly import tools
import plotly.offline as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly.offline import init_notebook_mode, iplot
#init_notebook_mode(connected=True) 

plt.style.use('bmh')

plt.rcParams['figure.dpi'] = 100

def radar_chart(df, eq1, eq2):
    AVT = df[df["Name"] == eq1]
    APT = df[df["Name"] == eq2]
    Moyenne2022 = df[df["Name"] == "Moyenne_2022"]
    data = [
        go.Scatterpolar(
             name = Moyenne2022.Name.values[0],
            r = [Moyenne2022['Attaque'].values[0],Moyenne2022['Passe'].values[0],Moyenne2022['Defense'].values[0]],
            theta = ['Attaque','Passe','Defense'],
            fill = 'toself',
            line =  dict(
                    color = 'red'
                )
            ),
        go.Scatterpolar(
             name = AVT.Name.values[0],
            r = [AVT['Attaque'].values[0],AVT['Passe'].values[0],AVT['Defense'].values[0]],
            theta = ['Attaque','Passe','Defense'],
            fill = 'toself',
            line =  dict(
                    color = 'cyan'
                )
            ),
        go.Scatterpolar(
            name = APT.Name.values[0],
            r = [APT['Attaque'].values[0],APT['Passe'].values[0],APT['Defense'].values[0]],
            theta = ['Attaque','Passe','Defense'],
            #fill = 'toself',
            line =  dict(
                color = 'orange'
            )
        )]
    layout = go.Layout(
        polar = dict(
            radialaxis = dict(
                visible = True,
                range = [0, 1]
            )
        ),
        showlegend =True,
        title = "{} vs {} Stats Comparison".format(AVT.Name.values[0], APT.Name.values[0])
    )

    fig = go.Figure(data=data, layout=layout)
    
    return fig
    

def radar_det(df, eq1, eq2):
    AVT = df[df["Name"] == eq1]
    APT = df[df["Name"] == eq2]
    AVTDetail = df[df["Name"] == eq1]
    APTDetail = df[df["Name"] == eq2]
    Moyenne2022Detail = df[df["Name"] == "Moyenne_2022"]
    data2 = [
        go.Scatterpolar(
            name = Moyenne2022Detail.Name.values[0],
             r = [Moyenne2022Detail['Buts'].values[0],Moyenne2022Detail['Assists'].values[0],
             Moyenne2022Detail['Tirs_cadrés'].values[0],Moyenne2022Detail['Tirs'].values[0],
             Moyenne2022Detail['Passes_complétées'].values[0],Moyenne2022Detail['Passes'].values[0],
             Moyenne2022Detail['Tacles'].values[0],Moyenne2022Detail['Tacles_gagnés'].values[0],
             Moyenne2022Detail['Pression'].values[0],Moyenne2022Detail['Interception'].values[0],
             Moyenne2022Detail['Duels_aeriens_remportés'].values[0]],
             theta = ['Buts','Assists','Tirs_cadrés','Tirs','Passes_complétées','Passes','Tacles','Tacles_gagnés',
                 'Pression','Interception','Duels_aeriens_remportés'],
            fill = 'toself',
            line =  dict(
                color = 'red'
            )
        ),
        go.Scatterpolar(
             name = AVTDetail.Name.values[0],
             r = [AVTDetail['Buts'].values[0],AVTDetail['Assists'].values[0],
             AVTDetail['Tirs_cadrés'].values[0],AVTDetail['Tirs'].values[0],
             AVTDetail['Passes_complétées'].values[0],AVTDetail['Passes'].values[0],
             AVTDetail['Tacles'].values[0],AVTDetail['Tacles_gagnés'].values[0],
             AVTDetail['Pression'].values[0],AVTDetail['Interception'].values[0],
             AVTDetail['Duels_aeriens_remportés'].values[0]],
            theta = ['Buts','Assists','Tirs_cadrés','Tirs','Passes_complétées','Passes','Tacles','Tacles_gagnés',
                 'Pression','Interception','Duels_aeriens_remportés'],
        #fill = 'toself',
            line =  dict(
                color = 'cyan'
            )
        ),
        go.Scatterpolar(
            name = APTDetail.Name.values[0],
            r = [APTDetail['Buts'].values[0],APTDetail['Assists'].values[0],
             APTDetail['Tirs_cadrés'].values[0],APTDetail['Tirs'].values[0],
             APTDetail['Passes_complétées'].values[0],APTDetail['Passes'].values[0],
             APTDetail['Tacles'].values[0],APTDetail['Tacles_gagnés'].values[0],
             APTDetail['Pression'].values[0],APTDetail['Interception'].values[0],
             APTDetail['Duels_aeriens_remportés'].values[0]],
            theta = ['Buts','Assists','Tirs_cadrés','Tirs','Passes_complétées','Passes','Tacles','Tacles_gagnés',
                 'Pression','Interception','Duels_aeriens_remportés'],
            #fill = 'toself',
            line =  dict(
                color = 'orange'
            )
        )]
    layout = go.Layout(
        polar = dict(
        radialaxis = dict(
        visible = True,
        range = [0, 1]
    )
    ),
    showlegend = True,
    title = "{} vs {} Stats Comparison Details".format(AVT.Name.values[0], APT.Name.values[0])
    )

    fig = go.Figure(data=data2, layout=layout)
    return fig

    