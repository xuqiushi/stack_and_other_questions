import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from urllib.request import urlopen, Request

url = "http://goldpricez.com/gold/history/lkr/years-3"

req = Request(url=url)
html_content = urlopen(req).read().decode("utf-8")
df = pd.read_html(url)  # this will give you a list of dataframes from html

df1 = df[3]

first_val = df1.iloc[0][0]


date = df1[0]
price = df1[1]

data = [df1[0], df1[1]]

headers = ["Date", "Price"]

df3 = pd.concat(data, axis=1, keys=headers)


from datetime import datetime

df3["Date"] = df3["Date"].apply(lambda x: datetime.strptime(x, "%d-%m-%Y"))


df3["Year"] = pd.DatetimeIndex(df3["Date"]).year
df3["Month"] = pd.DatetimeIndex(df3["Date"]).month
df3["Day"] = pd.DatetimeIndex(df3["Date"]).day

df3["WDay"] = df3["Date"].dt.dayofweek

df3["WeekDayName"] = pd.DatetimeIndex(df3["Date"]).day_name()


print(df3["WDay"])


writer = pd.ExcelWriter("data/dash_exceptions.xlsx", engine="xlsxwriter")

# Convert the dataframe to an XlsxWriter Excel object.
df3.to_excel(writer, sheet_name="Sheet1")

# Close the Pandas Excel writer and output the Excel file.
writer.save()


app = dash.Dash(__name__)


app.layout = html.Div(
    [
        html.H1("Gold Price Analyst", style={"text-align": "center"}),
        html.Div(["Output: ", dcc.Graph(figure={})], id="this_year_graph"),
    ]
)


@app.callback(
    [Output(component_id="this_year_graph", component_property="figure")],
    [Input("none", "children")],
)
def update_graph():

    dff = df3.copy()
    dff = [df4["Date"], df4["Price"]]

    this_year_graph = px.line(dff, x=dff["Date"], y=dff["Price"])

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
