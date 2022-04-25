import pandas as pd
import numpy as np

from holoviews import opts, dim

import holoviews as hv
#ext = hv.extension('bokeh')
#ot = hv.output(size=200)

def chord_diagram(df):
    hv.extension('bokeh')
    hv.output(size=200)
    trips = df[['Team In','Team Left']].value_counts()
    

    links=pd.DataFrame.from_records(
        list(trips.index),
        columns=['start','end']
        ) 

    links['trips']=trips.values


    chord=hv.Chord(links).select(value=(0.25, None))

    chord.opts(
        node_color='index',
        edge_color='start',
        label_index='index',
        cmap='Category10',
        edge_cmap='Category10')

    return chord