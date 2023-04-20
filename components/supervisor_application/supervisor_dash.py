# ================= importacion packeges ==================== #
import dash 
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify
from dash_bootstrap_templates import ThemeChangerAIO
from dash.dependencies import Output, Input, State

import plotly_express as px
import plotly.graph_objects as go

import pandas as pd

from components.supervisor_application.slayout import *
from components.supervisor_application import sbase, scampanha, scomitiva, sconfiguração, sfee, sperfil, sperformance, spremissas, sranking, slayout
# =========================================================== #   


# ================= Estilos e Fontes =================== #
estilos = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css", "https://fonts.googleapis.com/icon?family=Material+Icons", dbc.themes.COSMO]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
# ==================================================== #


 # ================================ LAYOUT ===================================== #
def supervisor_dash_application(flask_app):
    app_dash_sup = dash.Dash(
        server=flask_app, name="Supervisor", url_base_pathname='/Supervisor/', external_scripts=estilos + [dbc_css] + [FONT_AWESOME],
        external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css], use_pages=True, pages_folder="", meta_tags=[
            {"name": "viewport", "content": "width=device-width, initial-scale=1, maximum-scale=1.2, minimum-scale=0.5"}
        ]
    )
    app_dash_sup.config["suppress_callback_exceptions"] = True
    app_dash_sup.scripts.config.serve_locally = True
    server = app_dash_sup.server


    # ------------------------ Titulo Da Página & Favicon ---------------------- #
    app_dash_sup.title = "Supervisor"
    app_dash_sup._favicon = ("../assets/favicon/dash.ico")
    # -------------------------------------------------------------------------- #

    page_content = html.Div(id="page-supervisor")


    app_dash_sup.layout = dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Store(id="side_click"),
                            dcc.Location(id="url"),
                            slayout.barra_superior,
                            slayout.sidebar
                        ], md=2
                    ),

                    dbc.Col(
                        [
                            html.Div([page_content], style={"display": "flex", "positon": "flex"})
                        ], md=10
                    )
                ]
            )
        ], fluid=True, style={"padding": "0px"}, className="dbc-1"
    )

 # ================================================================================== #


 # ======================== Callback Page Content =============================== #
 
    @app_dash_sup.callback(
        Output("page-supervisor", "children"),
        [Input("url", "pathname")]
    )
    def render_page_content(pathname):
        if pathname == "/Supervisor/" or pathname == "/Performance/":
            return sperformance.layout

        if pathname == "/Premissas/":
            return spremissas.layout

        if pathname == "/Fee/":
            return sfee.layout
        
        if pathname == "/Campanha/":
            return scampanha.layout

        if pathname == "/Ranking/":
            return sranking.layout

        if pathname == "/Base/":
            return sbase.layout

        if pathname == "/Comitiva/":
            return scomitiva.layout

        if pathname == "/Configuracao/":
            return sconfiguração.layout

        if pathname == "/Perfil/":
            return sperfil.layout

 # ============================================================================== #

 
 # ===================== CallBack Fechamento e Aberturada Menu Lateral ================== #

    @app_dash_sup.callback(
        [
            Output("sidebar", "style"), # Construção Sidebar
            Output("page-supervisor", "style"), # Pagina Content "md-12"
            Output("side_click", "data"), # Side Click
            Output("bottom_sidebar", "style"), # Botão Do Menu Lateral
            Output("avata_img", "style"), # Foto Avatar - Perfil
            Output("nome_usuario", "style"), # H2 Do Nome Do Usuario
            Output("navlink_perf", "style"), # NavLink Performance
            Output("navlink_premiss", "style"), # NavLick Premissas
            Output("navlink_fee", "style"), # NavLink Fee
            Output("navlink_camp", "style"), # NavLink Campanha
            Output("navlink_rank", "style"), # NavLink Ranking
            Output("navlink_bas", "style"), # NavLink Base
            Output("navlink_comit", "style"), # NavLink Comitiva
            Output("navlink_conf", "style"), # Navlink Configuração
            Output("navlink_perfil", "style"), # NavLink Perfil
            Output("bottom-perf", "style"), # Botão Performance
            Output("bottom-prem", "style"), # Botão Premissas
            Output("bottom-fee", "style"), # Botão Fee
            Output("bottom-camp", "style"), # Botão Campanha
            Output("bottom-rank", "style"), # Botão Ranking
            Output("bottom-bass", "style"), # Botão Base
            Output("bottom-comit", "style"), # Botão Comitiva
            Output("bottom-conf", "style"), # Botão Configuração
            Output("bottom-perfil", "style") # Botão Perfil
        ],

        [
            Input("btn_sidebar", "n_clicks") # Botão Do Menu Lateral
        ],

        [
            State("side_click", "data") # Side Click
        ]
    )

    def toggle_sidebar(n, nclick):
        if nclick == "HIDDEN":
            menulateral = MENULATERAL_STYLE # Função Menu Lateral
            content = CONTENT_STYLE # Função Com Content - Page-Content
            botaomenu = BOTÃO_MENU # Função Botão Abrir e Fecha Menu lateral
            avatar_style = IMAGEM_ESTILO # Função Foto Perfil
            nameuser = NAME_USER # Função Nome do Usuario
            nl_perf = BOTTOM_MENUS # Função Move o Nome NavLink
            nl_premiss = BOTTOM_MENUS # Função Move Nome NavLink
            nl_fee = BOTTOM_MENUS # Função Move Nome NavLink
            nl_camp = BOTTOM_MENUS # Função Move Nome NavLink
            nl_rank = BOTTOM_MENUS # Função Move Nome NavLink
            nl_bas = BOTTOM_MENUS # Função Move Nome NavLink
            nl_comit = BOTTOM_MENUS # Função Move Nome NavLink
            nl_conf = BOTTOM_MENUS # Função Move Nome NavLink
            nl_perfi = BOTTOM_MENUS # Função Move Nome NavLink
            bt_perf = ICON_STYLE # Botão Move Performance
            bt_prem = ICON_STYLE # Botão Move Premissas
            bt_fee = ICON_STYLE # Botão Move Fee
            bt_camp = ICON_STYLE # Botão Move Campanha
            bt_rank = ICON_STYLE # Botão Move Ranking
            bt_bass = ICON_STYLE # Botão Move Base
            bt_comit = ICON_STYLE # Botão Move Comitiva
            bt_conf = ICON_STYLE # Botão Move Configuração
            bt_perfil = ICON_STYLE # Botão Move Perfil   
            cur_click = "SHOW" # Função Click
        else:
            menulateral = MENULATERAL_OCULTA # Função Menu Lateral
            content =  CONTENT_STYLE_OCULTO # Função Com Content - Page-Content
            botaomenu = BOTÃO_MENU2 # Função Botão Abrir e Fecha Menu lateral
            avatar_style = IMAGEM_ESTILO_OCULTO # Função Foto Perfil
            nameuser = NAME_USER_OCULTO # Função Nome do Usuario
            nl_perf = BOTTOM_MENUS_OCULTO # Função Move Nome NavLink
            nl_premiss = BOTTOM_MENUS_OCULTO # Função Move Nome NavLink
            nl_fee = BOTTOM_MENUS_OCULTO # Função Move Nome NavLink
            nl_camp = BOTTOM_MENUS_OCULTO # Função Move Nome NavLink
            nl_rank = BOTTOM_MENUS_OCULTO # Função Move Nome NavLink
            nl_bas = BOTTOM_MENUS_OCULTO # Função Move Nome NavLink
            nl_comit = BOTTOM_MENUS_OCULTO # Função Move Nome NavLink
            nl_conf = BOTTOM_MENUS_OCULTO # Função Move Nome NavLink
            nl_perfi = BOTTOM_MENUS_OCULTO # Função Move Nome NavLink
            bt_perf = ICON_STYLE_FRENT # Botão Move Performance
            bt_prem = ICON_STYLE_FRENT # Botão Move Premissas
            bt_fee = ICON_STYLE_FRENT # Botão Move Fee
            bt_camp = ICON_STYLE_FRENT # Botão Move Campanha
            bt_rank = ICON_STYLE_FRENT # Botão Move Ranking
            bt_bass = ICON_STYLE_FRENT # Botão Move Base
            bt_comit = ICON_STYLE_FRENT # Botão Move Comitiva
            bt_conf = ICON_STYLE_FRENT # Botão Move Configuração
            bt_perfil = ICON_STYLE_FRENT # Botão Move Perfil
            cur_click = "HIDDEN" # Função Click

        return(menulateral, content, cur_click, botaomenu, avatar_style, nameuser, nl_perf, nl_premiss, nl_fee, nl_camp, 
            nl_rank, nl_bas, nl_comit, nl_conf, nl_perfi, bt_perf, bt_prem, bt_fee, bt_camp, bt_rank, bt_bass, bt_comit, 
            bt_conf, bt_perfil)

 # ========================================================================================= #


# ============================================================================= #