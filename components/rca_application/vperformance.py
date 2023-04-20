# ================= importacion packeges ==================== #
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State

import plotly_express as px
import plotly.graph_objects as go

import pandas as pd

from components.rca_application.rca_dash import *
# ============================================================ #


# ============================ Tratamento se Dados ==================================== #
files_premissas = pd.read_excel('database/Premissas/Premissas.xlsx')
pd_vendedor = pd.DataFrame(files_premissas, columns=[
    "MÊS", "GERENTE", "VENDEDOR", "CRITÉRIO", "META", "REALIZADO", "%", "R$"
])
#================================================================================#


#============= tratamento de dados FEE Vendedor. ===============#
files_feevendedor = pd.read_excel('database/FEE (Vendedor)/FEE (Vendedor).xlsx')
pd_fee1 = pd.DataFrame(files_feevendedor, columns=[
    "COD RCA", "COD FORN.", "RAZÃO", "CRITÉRIO", "REALIZADO", "%"
])
#===============================================================#


#=================== tratamento de dados FEE Gestão. ===================#
files_feegestão = pd.read_excel('database/FEE (Gestão)/FEE (Gestão).xlsx')
pd_fee2 = pd.DataFrame(files_feegestão, columns=[
    "COD RCA", "COD FORN.", "RAZÃO", "CRITÉRIOS", "OBJETIVO", "REALIZADO", "%"
])
#=======================================================================#


#======================= tratamento de dados Camapanhas. =======================#
files_campanhas = pd.read_excel('database/Campanha/Campanhas.xlsx')
pd_campanha = pd.DataFrame(files_campanhas, columns=[
    "EQUIPE", "RCA", "COD FORN.", "FORNECEDOR", "BASE RCA", "POSITICADOS", "MIX. CAD", "MIX REAL.",
    "FATURAMENTO", "%POS", "CÓD SUP.", "INTERIOR", "BASE", "RCA", "EQUIPE"
])
#===============================================================================#


#=================== tratamento de dados EMBALAPAN. PESO =====================#
file_peso = pd.read_excel('database/Técnicos/Peso/D.peso.xlsx').rename(
    columns={"PEDO (KG)": "PESO(Kg)"}
)
# informações abreviadas
pd_peso = pd.DataFrame(file_peso, columns=["MÊS", "PESO(Kg)"])
# informações abreviadas
pd_fat = pd.DataFrame(file_peso, columns=["MÊS", "VALOR FAT."])
# informações abreviadas
pd_forn = pd.DataFrame(file_peso, columns=["MÊS", "CÓD", "FORNECEDOR"])
# informações abreviadas
pd_qt = pd.DataFrame(file_peso, columns=["MÊS", "QT"])
#=============================================================================#


#=============== tratamento de dados de visitas dos técnicos.VISITAS ==============#
file_visits = pd.read_excel('database/Técnicos/Visitas/D.visits.xlsx').rename(
    columns={
        "YEAR": "ANO", "MONTH": "MÊS", "EMPLOYEE": "TÉCNICO",
        "FANTASY NAME": "NOME FANTASIA", "DURATION": "DURAÇÃO"
    })
dt_visits = pd.DataFrame(file_visits, columns=[
    "ANO", "MÊS", "TÉCNICO", "RAZÃO", "NOME FANTASIA", "CNPJ-CPF",
    "CHECK-IN", "CHECK-OUT", "DURAÇÃO"
])


fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])

# ===================================================================================== #


# --------------------------- STYLE DOS CARDS ----------------------------------- #
CARDS_DASH = {
    "position": "block",
    "background": "#149ddd",
    "textAlign": "center",
    "margin": 0,
    "height": "100px",
    "margin-left": "80px",
    "width": "35px",
    "border-radius": "0px 10px 10px 0px",
}
# ------------------------------------------------------------------------------- # 


# ========================================= LAYOUT ============================================== #
layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                dbc.CardGroup(
                                    [
                                        dbc.Card(
                                            [
                                                html.Legend("FATURAMENTO", style={"color": "#7CF6FD", "letter-spacing": "5px", "fontSize": 17}),
                                                html.H5("R$ -", id="up-faturamento-dashboard", style={"color": "#7CF6FD"})
                                            ], style={"padding-left": "15px", "padding-top": "10px"}
                                        ),

                                        dbc.Card(
                                            [
                                                html.Div(
                                                    [
                                                        DashIconify(icon="fluent-mdl2:money", color="#000", width=30, height= 30, 
                                                            style={"margin-top": "35px", "margin": 0}
                                                        )
                                                    ], style=CARDS_DASH
                                                )
                                            ], style={"margin": 0}
                                        )
                                    ], style={"display": "flex", "background": "#6f7180", "border-radius": "10px 10px 10px 10px"}
                                )
                            ], style={"border": "1px solid #7CF6FD", "margin-left": 0, "width": "250px", "border-radius": "10px 10px 10px 10px"}
                        )
                    ]
                ),

                dbc.Col(
                    [
                        html.Div(
                            [
                                dbc.CardGroup(
                                    [
                                        dbc.Card(
                                            [
                                                html.Legend("POSITIVAÇÂO", style={"color": "#7CF6FD", "letter-spacing": "5px", "fontSize": 17}),
                                                html.H5("R$ -", id="up-positivacao-dashboard", style={"color": "#7CF6FD"})
                                            ], style={"padding-left": "15px", "padding-top": "10px"}
                                        ),

                                        dbc.Card(
                                            html.Div(
                                                [
                                                    DashIconify(icon="fluent-mdl2:money", color="#000", width=30, height= 30, 
                                                        style={"margin-top": "35px"}
                                                    )
                                                ], style=CARDS_DASH
                                            )
                                        )
                                    ], style={"display": "flex", "background": "#6f7180", "border-radius": "10px 10px 10px 10px"}
                                )
                            ], style={"border": "1px solid #7CF6FD", "margin-left": "30px", "width": "250px", "border-radius": "40px 40px 40px 40px"}
                        )
                    ]
                ),

                dbc.Col(
                    [
                        html.Div(
                            [
                                dbc.CardGroup(
                                    [
                                        dbc.Card(
                                            [
                                                html.Legend("LUCRO", style={"color": "#7CF6FD", "letter-spacing": "5px", "fontSize": 17}),
                                                html.H5("R$ -", id="up-lucro-dashboard", style={"color": "#7CF6FD"})
                                            ], style={"padding-left": "15px", "padding-top": "10px"}
                                        ),

                                        dbc.Card(
                                            html.Div(
                                                [
                                                    DashIconify(icon="fluent-mdl2:money", color="#000", width=30, height= 30, 
                                                        style={"margin-top": "35px"}
                                                    )
                                                ],  style=CARDS_DASH
                                            )
                                        )
                                    ], style={"display": "flex", "background": "#6f7180", "border-radius": "10px 10px 10px 10px"}
                                )
                            ], style={"border": "1px solid #7CF6FD", "margin-left": "30px", "width": "250px", "border-radius": "10px 10px 10px 10px"}
                        )
                    ]
                ),

                dbc.Col(
                    [
                        html.Div(
                            [
                                dbc.CardGroup(
                                    [
                                        dbc.Card(
                                            [
                                                html.Legend("MIX", style={"color": "#7CF6FD", "letter-spacing": "5px", "fontSize": 17}),
                                                html.H5("R$ -", id="up-mix-dashboard", style={"color": "#7CF6FD"})
                                            ], style={"padding-left": "15px", "padding-top": "10px"}
                                        ),

                                        dbc.Card(
                                            html.Div(
                                                [
                                                    DashIconify(icon="fluent-mdl2:money", color="#000", width=30, height= 30, 
                                                        style={"margin-top": "35px"}
                                                    )
                                                ], style=CARDS_DASH
                                            )
                                        )
                                    ], style={"display": "flex", "background": "#6f7180", "border-radius": "10px 10px 10px 10px"}
                                )
                            ], style={"border": "1px solid #7CF6FD", "margin-left": "30px", "width": "250px", "border-radius": "10px 10px 10px 10px"}
                        )
                    ]
                ),

                dbc.Col(
                    [
                        html.Div(
                            [
                                dbc.CardGroup(
                                    [
                                        dbc.Card(
                                            [
                                                html.Legend("INADIMPLÊNCIA", style={"color": "#7CF6FD", "letter-spacing": "5px", "fontSize": 17}),
                                                html.H5("R$ -", id="up-lucro-dashboard", style={"color": "#7CF6FD"})
                                            ], style={"padding-left": "15px", "padding-top": "10px"}
                                        ),

                                        dbc.Card(
                                            html.Div(
                                                [
                                                    DashIconify(icon="fluent-mdl2:money", color="#000", width=30, height= 30, 
                                                        style={"margin-top": "35px"}
                                                    )
                                                ], style=CARDS_DASH
                                            )
                                        )
                                    ], style={"display": "flex", "background": "#6f7180", "border-radius": "10px 10px 10px 10px"}
                                )
                            ], style={"border": "1px solid #7CF6FD", "margin-left": "30px", "width": "250px", "border-radius": "10px 10px 10px 10px"}
                        )
                    ]
                )
            ], id="cards_criterios"
        )
    ], className="layout_performance_completo", fluid=True
)
# =============================================================================================== #
