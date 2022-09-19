function verificar(){
    var dataAtual = new Date()
    var anoAtual = dataAtual.getFullYear()
    var formAno = document.getElementById("ano_nascimento")
    var resultado = document.getElementById("resultado")
    if(formAno.value == 0 || formAno.value > anoAtual){
        window.alert("[Erro] Selecione uma idade válida.")
    }
    else{
        var formSex = document.getElementsByName('radsex')
        var idade = anoAtual - formAno.value
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if(formSex[0].checked){
            genero = 'um homem'
            if(idade >= 0 && idade <= 1){
                //bb
                img.setAttribute('src','bebehomem.gif')
            }
            else if(idade <= 15){
                //criança
                img.setAttribute('src','menino.gif')
            }
            else if(idade <= 50){
                //homem
                img.setAttribute('src','homem.gif')
            }
            else{
                //idoso
                img.setAttribute('src','idoso.gif')
            }
        }
        else if(formSex[1].checked){
            genero = 'uma mulher'
            if(idade >= 0 && idade <= 1){
                //bb
                img.setAttribute('src','bebemulher.gif')
            }
            else if(idade <= 15){
                //criança
                img.setAttribute('src','menina.gif')
            }
            else if(idade <= 50){
                //mulher
                img.setAttribute('src','mulher.gif')
            }
            else{
                //idosa
                img.setAttribute('src','idosa.gif')
            }
        }

        
        resultado.innerHTML = `Detectamos ${genero} com ${idade} anos`
        resultado.appendChild(img)
        

        
        
    }
}