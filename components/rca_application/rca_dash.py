# ================= importacion packeges ==================== #
import dash 
from dash import dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url
from dash.dependencies import Output, Input, State 

from components.rca_application.vlayout import *
from components.rca_application import vbase, vcampanha, vcomitiva, vconfiguração, vfee, vperfil, vperformance, vpremissas, vranking, vlayout
# =========================================================== # 


# ----------------- Estilos e Fontes ------------------- #
estilos = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css", 
    "https://fonts.googleapis.com/icon?family=Material+Icons", dbc.themes.COSMO]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
# ------------------------------------------------------ #


# ================================ LAYOUT ===================================== #
def rca_dash_application(flask_app):
    app_dash = dash.Dash(
        server=flask_app, name="Vendedor", url_base_pathname="/Vendedor/", external_scripts=estilos + [dbc_css] + [FONT_AWESOME], 
        external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css], use_pages=True, pages_folder="", meta_tags=[
            {"name": "viewport", "content": "width=device-width, initial-scale=1, maximum-scale=1.2, minimum-scale=0.5"}
        ]
    )
    dash.register_page(vperformance.__name__, path="/", layout=vperformance.layout)
    app_dash.config["suppress_callback_exceptions"] = True
    app_dash.scripts.config.serve_locally = True
    #server = app_dash.server


    # ----------- Titulo Da Página & Favivon -------------- #
    app_dash.title = "Vendedor"
    app_dash._favicon = ("../assets/favicon/dash.ico")
    # ----------------------------------------------------- # 


    app_dash.layout = dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Store(id="side_click"),
                            dcc.Location(id="url", refresh=True),
                            vlayout.barra_superior,
                            vlayout.sidebar
                        ], md=2, style={"padding": 0}
                    ),
                    
                    dbc.Col(
                        [
                            dbc.Col([], id="page-content")
                        ], md=10, style={"padding": 0}
                    )
                ]
            )
        ], fluid=True
    )
 # ===================================================================================== #


 # ======================== Callback Page Content =============================== #
    @app_dash.callback(
        Output("page-content", "children"),
        [Input("url", "pathname")]
    )
    def render_page_content(pathname):
        if pathname == "/Vendedor/":
            return vperformance.layout

        if pathname == "/Performance/":
            return vperformance.layout

        if pathname == "/Premissas/":
            return vpremissas.layout

        if pathname == "/Fee/":
            return vfee.layout
        
        if pathname == "/Campanha/":
            return vcampanha.layout

        if pathname == "/Ranking/":
            return vranking.layout

        if pathname == "/Base/":
            return vbase.layout

        if pathname == "/Comitiva/":
            return vcomitiva.layout

        if pathname == "/Configuracao/":
            return vconfiguração.layout

        if pathname == "/Perfil/":
            return vperfil.layout
 # ============================================================================== #


  # ============================ CallBack Modal - FOTO PERFIL ================================ #
    @app_dash.callback(
        Output("modal_perfil", "is_open"),
        [Input("btn_avatar", "n_clicks")],
        [State("modal_perfil", "is_open")]
    )
    def toggle_modal(n1, is_open):
        if n1:
            return not is_open
        return is_open
 # ================================================================================================== #


     # ===================== CallBack SIDEBAR - Menu Lateral ================== #
    @app_dash.callback(
        [  
            Output("sidebar", "style"),         # Construção Sidebar
            Output("page-content", "style"),    # Pagina Content "md-10"
            Output("side_click", "data"),       # Side Click
            Output("bottom_sidebar", "style"),  # Botão Do Menu Lateral
            Output("avata_img", "style"),       # Foto Avatar - Perfil
            Output("nome_usuario", "style"),    # H2 Do Nome Do Usuario
            Output("navlink_perf", "style"),    # NavLink Performance
            Output("navlink_premiss", "style"), # NavLick Premissas
            Output("navlink_fee", "style"),     # NavLink Fee
            Output("navlink_camp", "style"),    # NavLink Campanha
            Output("navlink_rank", "style"),    # NavLink Ranking
            Output("navlink_bas", "style"),     # NavLink Base
            Output("navlink_comit", "style"),   # NavLink Comitiva
            Output("navlink_conf", "style"),    # Navlink Configuração
            Output("navlink_perfil", "style"),  # NavLink Perfil
            Output("bottom-perf", "style"),     # Botão Performance
            Output("bottom-prem", "style"),     # Botão Premissas
            Output("bottom-fee", "style"),      # Botão Fee
            Output("bottom-camp", "style"),     # Botão Campanha
            Output("bottom-rank", "style"),     # Botão Ranking
            Output("bottom-bass", "style"),     # Botão Base
            Output("bottom-comit", "style"),    # Botão Comitiva
            Output("bottom-conf", "style"),     # Botão Configuração
            Output("bottom-perfil", "style")    # Botão Perfil
        ],

        [
            Input("btn_sidebar", "n_clicks")    # Botão Do Menu Lateral
        ],

        [
            State("side_click", "data")         # Side Click
        ]
    )
    def toggle_sidebar(n, nclick):
        if nclick == "HIDDEN":
            menulateral = MENULATERAL_STYLE  # Função Menu Lateral
            content = CONTENT_STYLE          # Função Com Content - Page-Content
            botaomenu = BOTÃO_MENU           # Função Botão Abrir e Fecha Menu lateral
            avatar_style = IMAGEM_ESTILO     # Função Foto Perfil
            nameuser = NAME_USER             # Função Nome do Usuario
            nl_perf = BOTTOM_MENUS           # Função Move o Nome NavLink
            nl_premiss = BOTTOM_MENUS        # Função Move Nome NavLink
            nl_fee = BOTTOM_MENUS            # Função Move Nome NavLink
            nl_camp = BOTTOM_MENUS           # Função Move Nome NavLink
            nl_rank = BOTTOM_MENUS           # Função Move Nome NavLink
            nl_bas = BOTTOM_MENUS            # Função Move Nome NavLink
            nl_comit = BOTTOM_MENUS          # Função Move Nome NavLink
            nl_conf = BOTTOM_MENUS           # Função Move Nome NavLink
            nl_perfi = BOTTOM_MENUS          # Função Move Nome NavLink
            bt_perf = ICON_STYLE             # Botão Move Performance
            bt_prem = ICON_STYLE             # Botão Move Premissas
            bt_fee = ICON_STYLE              # Botão Move Fee
            bt_camp = ICON_STYLE             # Botão Move Campanha
            bt_rank = ICON_STYLE             # Botão Move Ranking
            bt_bass = ICON_STYLE             # Botão Move Base
            bt_comit = ICON_STYLE            # Botão Move Comitiva
            bt_conf = ICON_STYLE             # Botão Move Configuração
            bt_perfil = ICON_STYLE           # Botão Move Perfil   
            cur_click = "SHOW"               # Função Click
        else:
            menulateral = MENULATERAL_OCULTA      # Função Menu Lateral
            content =  CONTENT_STYLE_OCULTO       # Função Com Content - Page-Content
            botaomenu = BOTÃO_MENU2               # Função Botão Abrir e Fecha Menu lateral
            avatar_style = IMAGEM_ESTILO_OCULTO   # Função Foto Perfil
            nameuser = NAME_USER_OCULTO           # Função Nome do Usuario
            nl_perf = BOTTOM_MENUS_OCULTO         # Função Move Nome NavLink
            nl_premiss = BOTTOM_MENUS_OCULTO      # Função Move Nome NavLink
            nl_fee = BOTTOM_MENUS_OCULTO          # Função Move Nome NavLink
            nl_camp = BOTTOM_MENUS_OCULTO         # Função Move Nome NavLink
            nl_rank = BOTTOM_MENUS_OCULTO         # Função Move Nome NavLink
            nl_bas = BOTTOM_MENUS_OCULTO          # Função Move Nome NavLink
            nl_comit = BOTTOM_MENUS_OCULTO        # Função Move Nome NavLink
            nl_conf = BOTTOM_MENUS_OCULTO         # Função Move Nome NavLink
            nl_perfi = BOTTOM_MENUS_OCULTO        # Função Move Nome NavLink
            bt_perf = ICON_STYLE_FRENT            # Botão Move Performance
            bt_prem = ICON_STYLE_FRENT            # Botão Move Premissas
            bt_fee = ICON_STYLE_FRENT             # Botão Move Fee
            bt_camp = ICON_STYLE_FRENT            # Botão Move Campanha
            bt_rank = ICON_STYLE_FRENT            # Botão Move Ranking
            bt_bass = ICON_STYLE_FRENT            # Botão Move Base
            bt_comit = ICON_STYLE_FRENT           # Botão Move Comitiva
            bt_conf = ICON_STYLE_FRENT            # Botão Move Configuração
            bt_perfil = ICON_STYLE_FRENT          # Botão Move Perfil
            cur_click = "HIDDEN"                  # Função Click
               
        return[menulateral, content, cur_click, botaomenu, avatar_style, nameuser, nl_perf, nl_premiss, nl_fee, nl_camp, nl_rank, nl_bas, nl_comit, nl_conf, 
            nl_perfi, bt_perf, bt_prem, bt_fee, bt_camp, bt_rank, bt_bass, bt_comit, bt_conf, bt_perfil]
 # ========================================================================================= #


# ============================================================================= #