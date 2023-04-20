#================= importacion packeges ====================#
from importlib.resources import contents
import dash 
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State

import plotly_express as px
import plotly.graph_objects as go

import pandas as pd
#============================================================#



layout = dbc.Col(
    [
        html.H1(
            "Tela Campanha Em Desenvolvimento"
        )
    ]
)