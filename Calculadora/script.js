var numero1 = document.querySelector("input#number1")
var numero2 = document.querySelector("input#number2")
var resultado = document.getElementById("resultado")

var num1 = Number(numero1)
var num2 = Number(numero2)


function somar(num1=0,num2=0){
    resultado.innerHTML = `Soma ${num1+num2}`
}

function subtrair(numero1,numero2,resultado){
    resultado = numero1 - numero2
    return resultado
}

function multiplicar(numero1,numero2,resultado){
    resultado = numero1 * numero2
    return resultado
}

function dividir(numero1,numero2,resultado){
    resultado = numero1 / numero2
    return resultado
}