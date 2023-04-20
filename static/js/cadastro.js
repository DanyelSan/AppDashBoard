//visualizador de senha eye-open/close-eye// - CADASTRO
function viewersenha1() {

    var senha1 = document.getElementById('senha-cad')
  
    document.getElementById('eye-black-open-1').addEventListener('click', () => {
      if (senha1) {
        senha1.type == 'password' ? senha1.type = 'text' : senha1.type = 'password';
        document.getElementById('eye-black-open-1').style.display = 'none';
        document.getElementById('eye-black-closed-1').style.display = 'inline-block';
      }
    })
  
    document.getElementById('eye-black-closed-1').addEventListener('click', () => {
      if (senha1) {
        senha1.type == 'text' ? senha1.type = 'password' : senha1.type = 'text';
        document.getElementById('eye-black-closed-1').style.display = 'none';
        document.getElementById('eye-black-open-1').style.display = 'inline-block';
      }
    })
  
  }
  function viewersenha2() {
  
    var senha2 = document.getElementById('senha-cad-two')
  
    document.getElementById('eye-black-open-2').addEventListener('click', () => {
      if (senha2) {
        senha2.type == 'password' ? senha2.type = 'text' : senha2.type = 'password';
        document.getElementById('eye-black-open-2').style.display = 'none';
        document.getElementById('eye-black-closed-2').style.display = 'inline-block';
      }
    })
  
    document.getElementById('eye-black-closed-2').addEventListener('click', () => {
      if (senha2) {
        senha2.type == 'text' ? senha2.type = 'password' : senha2.type = 'text';
        document.getElementById('eye-black-closed-2').style.display = 'none';
        document.getElementById('eye-black-open-2').style.display = 'inline-block';
      }
    })
  
  }