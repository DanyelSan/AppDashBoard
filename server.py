# ============ importação das bibliotecas. ================ #
from flask import render_template
from flask_bootstrap import Bootstrap
import flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flask_login.mixins import UserMixin
# ========================================================= #

# ======================= Importação de Telas Dashboard ============================ #
from components.rca_application.rca_dash import rca_dash_application                                 # DashBoard Tela Vendedor.
from components.rca_application.rca_dash import vperformance
from components.rca_application.rca_dash import vpremissas
from components.supervisor_application.supervisor_dash import supervisor_dash_application            # DashBoard Tela Supervisor.
from components.analista_application.analista_dash import analista_dash_application                  # DashBoard Tela Analista.
from components.gerente_application.gerente_dash import gerente_dash_application                     # DashBoard Tela Gerente.
from components.diretoria_application.diretoria_dash import diretoria_dash_application               # DashBoard Tela Diretoria.
from components.representante_application.representante_dash import representante_dash_application   # DashBoard Tela Representantes.
# ================================================================================== #


# =============== Criação Do App. ================ #
server = flask.Flask(__name__)
Bootstrap(server)
migrate = Migrate(server)
login = LoginManager(server)
login.init_app(server)


# ------------------------------- SERVER DISPLAYS ------------------------------ #
# ================= RCA - TELAS =========================== #
rca_dash_application(server) # Tela RCA
# ========================================================= #

# ====================== Supervisor =============== #
supervisor_dash_application(server)    # Tela Supervisor
# ================================================= #

# ====================== Analista =============== #
analista_dash_application(server)  # Tela Analista
# =============================================== #

# ====================== Gerente =============== #
gerente_dash_application(server)    # Tela Gerente
# ============================================== #

# ====================== Diretoria =============== #
diretoria_dash_application(server)    # Tela Diretoria
# ================================================ #

# ====================== Representante =============== #
representante_dash_application(server)    # Tela Representante
# ==================================================== #
# ------------------------------------------------------------------------------ #


# ------------------------------- DIRECIONAMENTO DE TELAS ---------------------------------------- #
# ====================== Tela Rca / TELAS =================== #
@login.user_loader
def user_loader():
    return Rca  # Vendedor
# =================================================== #

# ======================== Telas DashBoard //Supervisor//=================== #
@login.user_loader
def user_loader():
    return Supervisor # Supervisores
# ========================================================================== #

# ======================== Telas DashBoard //Analista//=================== #
@login.user_loader
def user_loader():
    return Analista   # Analista
# ======================================================================== #

# ======================== Telas DashBoard //Gerente//=================== #
@login.user_loader
def user_loader():
    return Gerente    # Gerente
# ======================================================================= #

# ======================== Telas DashBoard //Diretoria//=================== #
@login.user_loader
def user_loader():
    return Diretoria  # Diretoria
# ========================================================================= #

# ======================== Telas DashBoard //Representante//=================== #
@login.user_loader
def user_loader():
    return Representante # Representante
# ============================================================================= #
# -------------------------------------------------------------------------------------------------- #


 # ===================== Telas Primarias - HTML/CSS/JS ==================== #
@server.route("/")
def login1():
    return render_template('html/login.html') # Telas Principais Login - HTML

@server.route("/login/", methods=["GET", "POST"])
def login():
    return render_template('html/login.html') # Telas Principais Login - HTML

@server.route("/cadastro/", methods=["GET", "POST"])
def cadastro():
   return render_template("html/cadastro.html") # Tela de Cadastro - HTML

@server.route("/recuperacao/", methods=["GET", "POST"])
def recuperacao():
    return render_template("html/recuperacao.html") # Tela de Recuperação - HTML
 # ============================================================= #


 # ==================== Telas Primarias Dos Dash's ========================= #
@server.route("/Rca/",  methods=["GET", "POST"])  # -RCA
def Rca(Rca):
    if Rca == "/Performance/": 
        return render_template("components/rca_application/rca_dash.py")     # Rca
    if Rca == "/Premissas/":
        return render_template("components/rca_application/vpremissas")

@server.route("/Performance/")  # - RCA
def Vperformance():
    return render_template("components/rca_application/vperformance.py")    # Tela Performance - VENDEDOR

@server.route("/Premissas/")
def Vpremissas():
    return render_template("compondnts/rca_application/vpremissas.py")      # Tela Premissas - VENDEDOR

@server.route("/Supervisor/", methods=["GET", "POST"]) # - SUPERVISOR 
def Supervisor():
    return render_template("components/supervisor_application/supervisor_dash.py")    # Supervisor

@server.route("/Analista/", methods=["GET", "POST"]) # - ANALISTA
def Analista():
    return render_template("components/analista_application/analista_dash.py")  # Analista

@server.route("/Gerente/", methods=["GET", "POST"]) # - GERENTE
def Gerente():
    return render_template("components/gerente_application/gerente_dash.py")    # Gerente

@server.route("/Diretoria/", methods=["GET", "POST"]) # - DIRETORIA
def Diretoria():
    return render_template("components/diretoria_application/diretoria_dash.py.py")    # Diretoria

@server.route("/Representante/", methods=["GET", "POST"])  # - REPRESENTANTE
def Representante():
    return render_template("components/representante_application/representante_dash.py")    # Representante
 # ============================================================================ #


# ================================ aplicação do server. =================================== #
if __name__ == '__main__':
    server.run(host='192.168.0.147', debug=True, port=5000) #porta local - todos acessarem
    #server.run(host="10.0.0.251", debug=True, port=5000) #porta local - todos acessarem
    #server.run(debug=True, port=8090) #porta desenvolvimento
# ========================================================================================= #
