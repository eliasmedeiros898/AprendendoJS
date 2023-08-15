function limpar(){
   document.getElementById("resultado").innerHTML = "";
}


function insert(value){
    var numerosTela = document.getElementById("resultado").innerHTML;
    if(numerosTela == "Error"){
        numerosTela = "";
        document.getElementById("resultado").innerHTML = numerosTela + value;
    }
    if(numerosTela.length <= 12){
        document.getElementById("resultado").innerHTML = numerosTela + value;
    }
    else{
        document.getElementById("resultado").innerHTML = "Error"
        
    }
    
}



function apagarUltimo(){
    var numerosTela = document.getElementById("resultado").innerHTML;
    document.getElementById("resultado").innerHTML = numerosTela.substring(0,numerosTela.length-1);
}

function calcular(){
    var numerosTela = document.getElementById("resultado").innerHTML;
    if(numerosTela){
        var resultado = eval(numerosTela).toFixed(2);
        if(resultado.includes(".00")){
            document.getElementById("resultado").innerHTML = eval(numerosTela);
        }
        else{
            document.getElementById("resultado").innerHTML = eval(numerosTela).toFixed(2);
        }
        
    }
}
    