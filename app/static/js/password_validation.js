function validate(){
  senha = document.getElementById('senha').value;
  confirm_senha = document.getElementById('confirm_senha').value;

  if (senha != confirm_senha) {
    alert("Senhas não estão corretas")
    return false;
  }else{
    return true;
  }
}

document.getElementById('submit').addEventListener('click', validate);