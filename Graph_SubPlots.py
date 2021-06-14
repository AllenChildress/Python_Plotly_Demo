import plotly.graph_objects as graph
from plotly.subplots import make_subplots
import time
from Parallel_Coordinates_Plot import Parallel_Coordinates_Plot
import plotly.express as px

def Graph_SubPlots():
    start_time = time.time()
    df = px.data.iris()
    # ---------------------------------------------------------------------
    # Define 3 graphs in 1 column
    # ---------------------------------------------------------------------
    fig = make_subplots(rows=2, shared_xaxes=True, vertical_spacing=0.03,
                        row_width=[0.15, 0.15]
                        )
    fig.add_scatter(y=[4, 2, 1, 3, 5, 9, 14], mode="lines", name="Scatter Graph", row=1, col=1)
    fig.add_bar(y=[2, 1, 3, 4, 7, 12, 4], name="Bar Graph", row=2, col=1)
    fig.update_layout(
        title='Sub Plots')
    fig.show()