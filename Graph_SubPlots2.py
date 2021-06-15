import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time

import pandas as pd

def Graph_SubPlots2():
    start_time = time.time()

    # read in volcano database data
    df = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/volcano_db.csv",
        encoding="iso-8859-1",
    )

    # frequency of Country
    freq = df
    freq = freq.Country.value_counts().reset_index().rename(columns={"index": "x"})

    # read in 3d volcano surface data
    df_v = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/volcano.csv")

    # Initialize figure with subplots
    fig = make_subplots(
        rows=2, cols=2,
        column_widths=[0.6, 0.4],
        row_heights=[0.4, 0.6],
        specs=[[{"type": "scattergeo", "rowspan": 2}, {"type": "bar"}],
               [            None                    , {"type": "surface"}]])

    # Add scattergeo globe map of volcano locations
    fig.add_trace(
        go.Scattergeo(lat=df["Latitude"],
                      lon=df["Longitude"],
                      mode="markers",
                      name='Volcano Locations',
                      hoverinfo="text",
                      showlegend=True,
                      marker=dict(color="crimson", size=4, opacity=0.8)),
        row=1, col=1
    )

    # Add locations bar chart
    fig.add_trace(
        go.Bar(x=freq["x"][0:10],
               y=freq["Country"][0:10],
               name="Volcano Counts",
               marker=dict(color="crimson"),
               showlegend=True),
        row=1, col=2
    )

    # Add 3d surface of volcano
    fig.add_trace(
        go.Surface(z=df_v.values.tolist(), showscale=False),
        row=2, col=2
    )

    # Update geo subplot properties
    fig.update_geos(
        projection_type="orthographic",
        landcolor="white",
        oceancolor="MidnightBlue",
        showocean=True,
        lakecolor="LightBlue"
    )

    # Rotate x-axis labels
    fig.update_xaxes(tickangle=45)

    # Set theme, margin, and annotation in layout
    fig.update_layout(
        template="plotly_dark",
        margin=dict(r=10, t=25, b=40, l=60),
        annotations=[
            dict(
                text="Source: NOAA",
                showarrow=False,
                xref="paper",
                yref="paper",
                x=0,
                y=0)
        ]
    )

    fig.update_layout(
        title='Mixed Sub Plots')

    end_time = round(time.time() - start_time, 3)
    print(str(end_time) + ' seconds Graphing data for Graph_SubPlots2')

    fig.show()