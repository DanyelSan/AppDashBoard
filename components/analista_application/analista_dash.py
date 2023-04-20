#================= importacion packeges ====================#
import dash 
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State

from components.analista_application.alayout import *
from components.analista_application import alayout
#===========================================================#


# ----------------- Estilos e Fontes ------------------- #
estilos = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css", "https://fonts.googleapis.com/icon?family=Material+Icons", dbc.themes.COSMO]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
# ------------------------------------------------------ #


#================================ LAYOUT =====================================#
def analista_dash_application(flask_app):
    app_dash_analista = dash.Dash(server=flask_app, name="Analista", url_base_pathname='/Analista/', external_scripts=estilos + [dbc_css] + [FONT_AWESOME])
    app_dash_analista.config["suppress_callback_exceptions"] = True
    app_dash_analista.scripts.config.serve_locally = True
    server = app_dash_analista.server
    
    # ----------- Titulo Da Página & Favivon -------------- #
    app_dash_analista.title = "Analista"
    app_dash_analista._favicon = ("../assets/favicon/dash.ico")
    # ----------------------------------------------------- # 


    # -------------------------- Page CONTENT ------------------------- #
    content = html.Div(id="page-content")
    # ----------------------------------------------------------------- #


    app_dash_analista.layout = dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Store(id="side_click"),
                            dcc.Location(id="url"),
                            alayout.barra_superior,
                            alayout.sidebar
                        ], md=2
                    ),
                    
                    dbc.Col(
                        [
                            html.Div([content], style={"display": "flex", "position": "flex"})
                        ], md=10
                    )
                ]
            )
        ], fluid=True, style={"padding": "0px"}, className="dbc"
    )
#=============================================================================#