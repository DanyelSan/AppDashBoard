#================= importacion packeges ====================#
import dash 
from dash import html, dcc
import dash_bootstrap_components as dbc

import plotly_express as px
import plotly.graph_objects as go

import pandas as pd

from components.rca_application.vlayout import *
#===========================================================#


#============ Tratamento de Dados ==============#
file_representante = pd.read_excel("database/Representante/representante.xlsx")
#file_representante = pd.read_excel("../database/Representante/representante.xlsx")
pd_representante = pd.DataFrame(file_representante, columns=["FORNECEDOR",
"CLI.BASE", "CLI.POS.", "%POS", "QT.MIX.CAD", "QT.MIX", "PR.MÉIDO", "PESO (KG)"
"QT","VL.FATURADO", "%"
])
#===============================================#


#================================ LAYOUT =====================================#
def representante_dash_application(flask_app):
    app_dash = dash.Dash(server=flask_app, name="Representante", url_base_pathname='/Representante/')
    app_dash.config["suppress_callback_exceptions"] = True
    app_dash.scripts.config.serve_locally = True
    server = app_dash.server



    # ------------------------------ Titulo Da Página & Favivon -------------------------------- #
    app_dash.title = "Representante"
    app_dash._favicon = ("../assets/favicon/dash.ico")
    # ------------------------------------------------------------------------------------------ #

    app_dash.layout = html.Div(
        html.H1(
            "Tela Representante em Desenvolvimento"
        )
    )
    
#=============================================================================#