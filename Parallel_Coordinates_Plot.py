import plotly.express as px
import time

def Parallel_Coordinates_Plot():
    start_time = time.time()

    df = px.data.iris()
    fig = px.parallel_coordinates(df, color="species_id", labels={"species_id": "Species",
                    "sepal_width": "Sepal Width", "sepal_length": "Sepal Length",
                    "petal_width": "Petal Width", "petal_length": "Petal Length", },
                                 color_continuous_scale=px.colors.diverging.Tealrose,
                                 color_continuous_midpoint=2)
    fig.update_layout(
        title='Parallel Coodinates Plot')

    end_time = round(time.time() - start_time, 3)
    print(str(end_time) + ' seconds Graphing data for Parallel_Coordinates_Plot')

    fig.show()