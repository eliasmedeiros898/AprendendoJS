var date = new Date()
var hora = date.getHours()
var minuto = date.getMinutes()

console.log(`Agora são exatamente ${hora}:${minuto}`)
if(hora >= 0 && hora <= 4){
    console.log("Boa madrugada!")
}
else if(hora < 12 ){
    console.log("Bom dia!")
}
else if(hora < 18){
    console.log("Boa tarde!")

}
else if(hora <= 23){
    console.log("Boa noite!")
}
