#================= importacion packeges ====================#
import dash 
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State 

from components.diretoria_application.dlayout import *
from components.diretoria_application import dlayout
#===========================================================#


# ----------------- Estilos e Fontes ------------------- #
estilos = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css", "https://fonts.googleapis.com/icon?family=Material+Icons", dbc.themes.COSMO]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
# ------------------------------------------------------ #


#================================ LAYOUT =====================================#
def diretoria_dash_application(flask_app):
    app_dash_diretoria = dash.Dash(server=flask_app, name="Diretoria", url_base_pathname='/Diretoria/', external_scripts=estilos + [dbc_css] + [FONT_AWESOME])
    app_dash_diretoria.config["suppress_callback_exceptions"] = True
    app_dash_diretoria.scripts.config.serve_locally = True
    server = app_dash_diretoria.server

    # ----------- Titulo Da Página & Favivon -------------- #
    app_dash_diretoria.title = "Diretoria"
    app_dash_diretoria._favicon = ("../assets/favicon/dash.ico")
    # ----------------------------------------------------- # 


    # -------------------------- Page CONTENT ------------------------- #
    content = html.Div(id="page-content")
    # ----------------------------------------------------------------- #


    app_dash_diretoria.layout = dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Store(id="side_click"),
                            dcc.Location(id="url"),
                            dlayout.barra_superior,
                            dlayout.sidebar
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