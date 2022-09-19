
function carregar(){
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    var minutos = data.getMinutes()
    
    
    msg.innerHTML = `Agora são ${hora}:${minutos}`
    if (hora >= 0 && hora < 12){
        img.src = 'fotomanha.gif'
        document.body.style.background = '#f09d61'
        
    }
    else if(hora >= 12 && hora < 18){
        img.src = 'fotodia.gif'
        document.body.style.background = '#abc6ed'
    }
    else {
        img.src = 'fotonoite.gif'
        document.body.style.background = '#3a2c43'
    }
}
