#================= importacion packeges ====================#
import dash 
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State

import plotly_express as px
import plotly.graph_objects as go

import pandas as pd

from components.supervisor_application.supervisor_dash import *
#============================================================#


# ----------------------------------- LAYOUT ----------------------------------- #
layout = dbc.Col(
    [
        html.H1("Tela Performance Em Desenvolvimento"),
        html.Hr()
    ]
)
# ------------------------------------------------------------------------------ #
