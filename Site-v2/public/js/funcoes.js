// sessão
function validarSessao() {
    // aguardar();

    var email = sessionStorage.EMAIL_USUARIO;
    var senha = sessionStorage.SENHA_USUARIO;

    var b_usuario = document.getElementById("b_usuario");

    if (email != null ) {
        // window.alert(`Seja bem-vindo, ${nome}!`);
        // b_usuario.innerHTML = nome;

        // finalizarAguardar();
    } else {
        window.location = "./login.html";
    }
}

function limparSessao() {
    // aguardar();
    sessionStorage.clear();
    // finalizarAguardar();
    window.location = "./login.html";
}



