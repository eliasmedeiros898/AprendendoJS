var init_bet = 20
var saldo_ini = 12500
var saldo = saldo_ini
var num = 8

const mult = 2.1
total_apostado = init_bet
var cont = 1



    for(var i=1;i<num;i++){
    total_apostado += init_bet * mult
    console.log(`Aposta ${cont}: ${init_bet}`)
    init_bet = init_bet * mult
    
    saldo -= init_bet
    cont++
    
}
console.log(`Aposta ${cont}: ${init_bet}`)
console.log(`Total apostado: ${total_apostado}`)
console.log(`Saldo restante: ${saldo}`)
console.log(`Saldo recomendado para próxima bet: ${saldo_ini+(init_bet*mult-saldo)}`)

