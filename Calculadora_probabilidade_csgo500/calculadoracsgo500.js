
var init_bet = 10
var saldo_ini = 14000
var num = 9
var saldo = saldo_ini


function arredondar(n){
    return (Math.round(n*100) / 100).toFixed(0)
}


function calcular(num, saldo, init_bet, resultado){
    var cont = 1
    var total_apostado = init_bet
    const mult = 2.1
    
    for(var i=1;i<num;i++){
    total_apostado += init_bet * mult
    console.log(`Aposta ${cont}: ${arredondar(init_bet)}`)
    init_bet = init_bet * mult
    
    saldo -= init_bet
    cont++
    
}
console.log(`Aposta ${cont}: ${arredondar(init_bet)}`)
console.log(`Total apostado: ${arredondar(total_apostado)}`)

if(saldo>=0){
    console.log(`Saldo restante: ${arredondar(saldo)}`)
    console.log(`Saldo recomendado para chegar na ${cont+1} bet: ${arredondar(total_apostado*mult)}`)
}else{
    console.log(`Saldo que falta para chegar nessa aposta: ${arredondar(total_apostado - saldo_ini)}`)
    console.log(`Saldo recomendado para chegar na ${cont+1} bet: ${arredondar(total_apostado *mult)}`)
}
}
    


calcular(num,saldo,init_bet)
