//teste de validação de dados. Apos Login//
//function logar() {

    //var login = document.getElementById('usuario-login').value;
    //var senha = document.getElementById('password-login').value;

    //if (login == "admin@outlook.com" && senha == "admin") {
     //   alert('Login Efetuado Com Sucesso');
        //location.href = "../templates/py/dash.py"
    //    window.location.href = "{{ url_for('DashBoard') }}"
    //} else {
      //  alert('Usuario Ou Senha Incorretos, Tente Novamente');
    //}

//}

//visualizador de senha open-eye/ closed-eye// - LOGIN
function viewersenha() {

    var senha = document.getElementById('password-login')

    document.getElementById('eye-open').addEventListener('click', () => {
        if (senha) {
            senha.type == 'password' ? senha.type = 'text' : senha.type = 'password';
            document.getElementById('eye-closed').style.display = 'inline-block';
            document.getElementById('eye-open').style.display = 'none';
        }
    })

    document.getElementById('eye-closed').addEventListener('click', () => {
        if (senha) {
            senha.type == 'text' ? senha.type = 'password' : senha.type = 'text';
            document.getElementById('eye-closed').style.display = 'none';
            document.getElementById('eye-open').style.display = 'inline-block';
        }
    })

}