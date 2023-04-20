# ================= importacion packeges ==================== #
from dash import html
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify
# =========================================================== #


# ======================= Estilo Para Layout ======================= #
MENULATERAL_STYLE = {       # Estilo Estrutura Da Barra Lateral
    "position": "fixed",
    "margin": 0,
    "margin-left": 0,
    "top": 0,
    "left": 0,
    "padding": "1px",
    "bottom": 0,
    "width": "12rem",
    "transition": "1s",
    "background-image": "linear-gradient(#021128, #021138, #021148, #021158, #021158, #021168)",
}

MENULATERAL_OCULTA = {      # Estilo Estrutura Barra Lateral Oculta
    "position": "fixed",
    "margin": 0,
    "margin-left": 0,
    "top": "-190px",
    "left": 0,
    "padding": "17px",
    "bottom": 0,
    "height": "200vh",
    "width": "0px",
    "transition": "1s",
    "background-image": "linear-gradient(#021128, #021138, #021148, #021158, #021158, #021168)",
}

BARRASUPERIOR_STYLE = {  # Barra Estrutura Superior
    "position": "fixed",
    "margin-left": 0,
    "margin-top": 0,
    "top": 0,
    "left": 0,
    "height": "31px",
    "width": "100%",
    "background-image": "linear-gradient(to right, #021128, #021128, #021138, #021148, #021158, #021168)", 
}

CONTENT_STYLE = { # Estilo Da Pagina Demostrativo
    "position": "fixed",
    "transition": "all 1s",
    "margin-left": "12rem",
    "margin-top": "3rem",
    "height": "100vh",
}

CONTENT_STYLE_OCULTO = { # Estilo Da Pagina Demostrativo Abertura Com O Fechamento Do Menu Lateral
    "position": "fixed",
    "transition": "all 1s",
    "margin-left": "2rem",
    "margin-top": "3rem",
    "height": "100vh",
}

BOTÃO_MENU = {  # Botão 3 Pontos Para Abertura Do Menu Lateral
    "position": "absolute",
    "transition": "1s",
    "top": 0,
    "left": "160px",
    "cursor": "pointer",
}

BOTÃO_MENU2 = { # Botão 3 Pontos Para Fechamento Do Menu Lateral
    "position": "absolute",
    "transition": "1s",
    "top": 0,
    "left": 0,
    "cursor": "pointer",
}

IMAGEM_ESTILO = {  # Estilo Da Imagem Do Perfil
    "transition": "1s",
    "display": "flex",
    "position": "flex",
    "width": "105px",
    "border": "1px solid #2c2f3f", 
    "border-radius": "50%",
    "padding": "1px",
    "cursor": "pointer",
    "margin-top": "10px"
}

IMAGEM_ESTILO_MODAL1 = { # Estilo Do Avatar Modal 1 perfil
    "transistion": "1s",
    "display": "flex",
    "position": "flex",
    "height": "150px",
    "width": "150px",
    "margin-left": "75px",
    "margin-top": "25px",
    "border": "1px solid background-color: rgba(0, 0, 0, 0.5)",
    "border-radius": "50%",
    "cursor": "pointer",
    "padding": "1px"
}

IMAGEM_ESTILO_OCULTO ={ # Estilo Da Imagem Do Perfil Oculta
    "margin": 0,
    "width": "-110px",
    "margin-top": "8px",
    "margin-left": "-300px",
    "transition": "1s"
}

IMG_BUTTOM_PERFIL = { # Estilo Da Foto Do Usuário
    "background-color": "transparent",
    "border-color": "transparent",
    "padding": 0,
    "margin-left": "40px",
    "border-radius": "10%"
}

NAME_USER = {  # Estilo Do Nome Do Usuário
    "color": "#fff",
    "text-align": "center",
    "transition": "1s",
    "font-size": "25px",
    "margin": 0,
    "margin-top": "10px",
    "cursor": "pointer",
    "text-shadow": "2px 2.5px 1px #555"
}

NAME_USER_OCULTO = { # Estilo Do Nome Do Usuário Oculto
    "color": "#fff",
    "margin-left": "-300px",
    "transition": "1s",
    "font-size": "25px",
    "margin": 0,
    "margin-top": "10px",
    "text-shadow": "2px 2.5px 1px #555"
}

BOTTOM_MENUS = { # Estilo De Todos Icones Botões
    "margin-top": 0,
    "top": 0,
    "text-decoration":"none",
    "color":"#A2B5CD",
    "transition": "1s",
}

BOTTOM_MENUS_OCULTO = { # Estilo De Todos Icones Botões Oculto
    "margin-top": 0,
    "text-decoration":"none",
    "color":"#A2B5CD",
    "padding": 0,
    "transition": "1s",
    "margin-left": "-250px",
}

ICON_STYLE = {  # Estilo Dos Icones Individual 
    "padding": "0rem 0.5rem",
    "margin": "1px",
    "margin-left": "10px",
    "margin-top": "5px",
    "padding": 0,
    "transition": ".5s",
    "background-color": "transparent",
    "border-color": "transparent",
    "color": "#A2B5CD",
}

ICON_STYLE_FRENT = { # Estilo Dos Icones Individual Para Frente Apos Fechamento Do Menu Lateral
    "padding": "0rem",
    "transition": ".5s",
    "margin-left": "-12px",
    "margin-top": "22px",
    "padding": 0,
    "top": 0,
    "background-color": "transparent",
    "border-color": "transparent",
    "color": "#A2B5CD",
}

DASHBOARD = { # Letreiro Dashboard 
    "display": "flex",
    "color": "#fff",
    "margin-left":"15px",
    "margin-top": "5px",
    "letter-spacing": "8px",
    "padding": 0,
    "font-size": "16px",
    "cursor": "pointer",
    "text-shadow": "2px 3px 1px rgba(30,144,255,0.5)"
}

SICRONIZAÇÃO_DOWN = { # Estilo Do Aviso De Sincronização
    "position": "fixed", 
    "top": "7px", 
    "left": "80.4%", 
    "display": "none"
}
# ================================================================== #


# =============================== BARA LATERAL ======================================= #
barra_superior = dbc.Container(       # BARRA SUPERIOR
    [
        html.Div( # BOTÃO ABRIR E FECHA MENU SIDEBAR
            [     
                dbc.Button(
                    [
                        dbc.Input(type="checkbox", id="checkbox-menu", style={"position": "absolute", "opacity": 0, "heigth": 0}),
                        html.Label(
                            [
                                html.Span(id="span-1"), #Menu Hambuguer
                                html.Span(id="span-2"), #Menu Hambuguer
                                html.Span(id="span-3")  #Menu Hambuguer
                            ], htmlFor="checkbox-menu", className="btn_menu_sidebar", id="bottom_sidebar"
                        )
                    ], outline=True, id="btn_sidebar", className="btn_menu_closedopen", style=BOTÃO_MENU2
                )
            ], style={"position": "fixed"}, className="#btn_sidebar"
        ),

        html.Div(
            [
                dbc.Button(    # Botão Saída Para tela De Login On-off.
                    [
                        DashIconify(icon="bx:power-off", width=22, height=22),
                    ], id="btn_exit", href="/login/", external_link="html/login.html", className="btn_saida_login", title="Sair", color=None
                )
            ], className="botton_saida_dash"
        ),

        html.Div(
            [
                dbc.Button(     # Sinalizador Sicronização #
                    [
                        html.H4(DashIconify(icon="line-md:downloading-loop", width=25, height=25, className="iconi_sicronização"), title="sicronização"), #Alerta Sincrinização--
                        #html.H4(DashIconify(icon="line-md:loading-twotone-loop", width=25, height=25, inline=True, style=SICRONIZAÇÃO_DOWN), title="sincronização"),  #Aqui caso comunicação caia.                                   
                        html.H1("02/09/2022 11:45:35", className="alerta_sicronização", title="Sicronização")  # Alerta Sinconização--
                    ], outline=True, className="    zação", style={"margin-left": "12px"}
                )
            ], className="status_sicronização"
        )
    ], id="barra_superior", style=BARRASUPERIOR_STYLE, className="barra_superior_completo", fluid=True
)
# ==================================================================================== #


# ================================= Layout Menu Lateral ==================================== #
sidebar = dbc.Container(   # Menu Lateral #
    [
        dbc.Col(    #SIDEBAR 
            [
                html.I(["DASHBOARD"], style=DASHBOARD, className="text_dashboard"), # letreiro nome Dashboard
                html.Hr(style={"size": "50", "color": "#fff", "borderHeight": "10vh", "width": "90%", "margin": 0, "margin-left": "8px"}), #linha de separação entre nome Dashboard e a imagem do avatar   
                html.Div(     # Alteração de Foto Do Perfil - AVATAR #
                    [
                        dbc.Button( # Imagem Do Usuário
                            [
                                html.Img(src="assets/img/img_hom.png", id="avata_img", alt="Avata", className="perfil_avatar", style=IMAGEM_ESTILO) 
                            ], id="btn_avatar", style=IMG_BUTTOM_PERFIL, className="img_perfil_button", n_clicks=0, color=None, active=True
                        )               
                    ], id="perfil-user", className="foto_avatar"
                ),

                html.Div( # Apresentação Do Nome Do Usuário
                    [
                        html.H2("User Name", className="nome_perfil", id="nome_usuario", style=NAME_USER) 
                    ], style={"margin-top": "10px"}, className="name_perfil"
                ),

                html.Div(  #Modal Atualização Foto Avatar
                    [
                        dbc.Modal(
                            [
                                dbc.ModalHeader(dbc.ModalTitle(html.H2("FOTO DE PERFIL", style={"margin-left": "120px", "margin-top": "10px"}))),
                                dbc.ModalBody("Altere Sua Foto De Perfil Aqui", style={"text-align": "center"}),
                                dbc.ModalFooter(
                                    [
                                        dbc.Button(
                                            [
                                                html.Img(src="assets/img/img_hom.png", alt="image", height="100%", width="100%", style={
                                                    "border": "1px solid #2c2f3f", "border-radius": "50%"}
                                                )
                                            ], id="btn_avatar_perfil", outline=True, n_clicks=0, color=None, active=True
                                        )
                                    ]
                                )
                            ], id="modal_perfil", is_open=False
                        )
                    ]
                ),

                html.Div(    # Tela Performance #
                    [
                        html.Div(
                            [
                                dbc.NavItem(   
                                    [         
                                        dbc.Nav(
                                            [        
                                                html.I(                                      
                                                    dbc.Button(
                                                        [
                                                            DashIconify(icon="bi:activity", width=20, height=20)
                                                        ], style=ICON_STYLE_FRENT, href="/Performance/", id="bottom-perf", className="button_icon_perf" 
                                                    ), title="Performance"
                                                ),                   

                                                dbc.NavLink(
                                                    [
                                                        html.I("Performance", title="Performance")
                                                    ], href="/Performance/", active=True, style=BOTTOM_MENUS_OCULTO, id="navlink_perf", className="name_icon_performance",
                                                )
                                            ], pills=True
                                        )
                                    ], style={"margin-bottom": "10px"}
                                )
                            ]
                        ),
                        
                        html.Div(
                            [
                                dbc.NavItem(   # Tela Premissas #
                                    [  
                                        dbc.Nav(
                                            [ 
                                                html.I(
                                                    dbc.Button(
                                                        [
                                                            DashIconify(icon="bi:bar-chart-line", width=20, height=20)
                                                        ], style=ICON_STYLE_FRENT, href="/Premissas/", id="bottom-prem", className="button_icon_premissas"
                                                    ), title="Premissas"
                                                ),

                                                dbc.NavLink(
                                                    [
                                                        html.I("Premissas", title="Premissas")
                                                    ], href="/Premissas/", active="exact", style=BOTTOM_MENUS_OCULTO, id="navlink_premiss", className="name_icon_premissas"
                                                )
                                            ], pills=True
                                        )
                                    ], style={"margin-bottom": "10px"}
                                )
                            ]
                        ),

                        html.Div(
                            [
                                dbc.NavItem(    # Tela Fee #
                                    [    
                                        dbc.Nav(
                                            [
                                                html.I(
                                                    dbc.Button(
                                                        [
                                                            DashIconify(icon="bi:cash-coin", width=20, height=20)
                                                        ], style=ICON_STYLE_FRENT, href="/Fee/", id="bottom-fee", className="button_icon_fee"
                                                    ),title="Fee"
                                                ),

                                                dbc.NavLink(
                                                    [
                                                        html.I("Fee", title="Fee")
                                                    ], href="/Fee/", active="exact", style=BOTTOM_MENUS_OCULTO, id="navlink_fee", className="name_icon_fee"
                                                )
                                            ], pills=True
                                        )
                                    ], style={"margin-bottom": "10px"}
                                )
                            ]
                        ),

                        html.Div(
                            [
                                dbc.NavItem(    # Tela Companha #
                                    [   
                                        dbc.Nav(
                                            [
                                                html.I(
                                                    dbc.Button(
                                                        [
                                                            DashIconify(icon="bi:award", width=20, height=20)
                                                        ], style=ICON_STYLE_FRENT, href="/Campanha/", id="bottom-camp", className="button_icon_campanha"
                                                    ),title="Campanha"
                                                ),

                                                dbc.NavLink(
                                                    [ 
                                                        html.I("Campanha", title="Campanha")
                                                    ], href="/Campanha/", active="exact", style=BOTTOM_MENUS_OCULTO, id="navlink_camp", className="name_icon_campanha"
                                                )
                                            ], pills=True
                                        )
                                    ], style={"margin-bottom": "10px"}
                                )
                            ]
                        ),
                        
                        html.Div(
                            [
                                dbc.NavItem(    # Tela Ranking #
                                    [    
                                        dbc.Nav(
                                            [
                                                html.I(
                                                    dbc.Button(
                                                        [
                                                            DashIconify(icon="fa6-solid:ranking-star", width=20, height=20)
                                                        ], style=ICON_STYLE_FRENT, href="/Ranking/", id="bottom-rank", className="button_icon_ranking"
                                                    ),title="Ranking"
                                                ),  

                                                dbc.NavLink(
                                                    [
                                                        html.I("Ranking", title="Ranking")
                                                    ], href="/Ranking/", active="exact", style=BOTTOM_MENUS_OCULTO, id="navlink_rank", className="name_icon_ranking"
                                                )
                                            ], pills=True
                                        )
                                    ], style={"margin-bottom": "10px"}
                                )
                            ]
                        ),

                        html.Div(
                            [
                                dbc.NavItem(    # Tela Base #
                                    [  
                                        dbc.Nav(
                                            [ 
                                                html.I(
                                                    dbc.Button(
                                                        [
                                                            DashIconify(icon="bi:bootstrap", width=20, height=20)
                                                        ], style=ICON_STYLE_FRENT, href="/Base/", id="bottom-bass", className="button_icon_base"
                                                    ),title="Base"
                                                ),

                                                dbc.NavLink(
                                                    [   
                                                        html.I("Base", title="Base")
                                                    ], href="/Base/", active="exact", style=BOTTOM_MENUS_OCULTO, id="navlink_bas", className="name_icon_base"
                                                )
                                            ], pills=True
                                        )
                                    ], style={"margin-bottom": "10px"}
                                )
                            ]
                        ),
                        
                        html.Div(
                            [
                                dbc.NavItem(     # Tela Comitiva #
                                    [   
                                        dbc.Nav(
                                            [
                                                html.I(
                                                    dbc.Button(
                                                        [
                                                            DashIconify(icon="bi:clipboard-data", width=20, height=20)
                                                        ], style=ICON_STYLE_FRENT, href="/Comitiva/", id="bottom-comit", className="button_icon_comitiva"
                                                    ),title="Comitiva"
                                                ),

                                                dbc.NavLink(
                                                    [   
                                                        html.I("Comitiva", title="Comitiva")
                                                    ], href="/Comitiva/", active="exact", style=BOTTOM_MENUS_OCULTO, id="navlink_comit", className="name_icon_comitava"
                                                )
                                            ], pills=True
                                        )
                                    ], style={"margin-bottom": "10px"}
                                )
                            ]
                        ),

                        html.Div(
                            [
                                dbc.NavItem(    # Tela Configuração #
                                    [   
                                        dbc.Nav(
                                            [   
                                                html.I(
                                                    dbc.Button(
                                                        [
                                                            DashIconify(icon="bi:gear", width=20, height=20)
                                                        ], style=ICON_STYLE_FRENT, href="/Configuracao/", id="bottom-conf", className="button_icon_config"
                                                    ), title="Configuração"
                                                ),

                                                dbc.NavLink(
                                                    [

                                                        html.I("Configuração", title="Configuração")
                                                    ], href="/Configuracao/", active="exact", style=BOTTOM_MENUS_OCULTO, id="navlink_conf", className="name_icon_config"
                                                )
                                            ], pills=True
                                        )
                                    ], style={"margin-bottom": "10px"}
                                )
                            ]
                        ),

                        html.Div(
                            [
                                dbc.NavItem(    # Tela Perfil #
                                    [   
                                        dbc.Nav(
                                            [
                                                html.I(
                                                    dbc.Button(
                                                        [
                                                            DashIconify(icon="bi:person", width=20, height=20)
                                                        ], style=ICON_STYLE_FRENT, href="/Perfil/", id="bottom-perfil", className="button_icon_perfil"
                                                    ),title="Perfil"   
                                                ),

                                                dbc.NavLink(
                                                    [
                                                        html.I("Perfil", title="Perfil")
                                                    ], href="/Perfil/", active="exact", style=BOTTOM_MENUS_OCULTO, id="navlink_perfil", className="name_icon_perfil"
                                                )
                                            ], pills=True
                                        )
                                    ], style={"margin-bottom": "10px"}
                                )
                            ]
                        )
                    ], style={"margin-top": "15px"}, className="menu_lateral_completo"
                )
            ], className="sidebar_menu"
        )
    ], id="sidebar", className="sidebar_completo", fluid=True, style=MENULATERAL_OCULTA
)      
# ============================================================================= #