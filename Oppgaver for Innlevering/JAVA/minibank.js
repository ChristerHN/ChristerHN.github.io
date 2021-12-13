var pinkode = prompt("Hva er pinkoden din?");
var penger = 4000;

function sjekkBank(){
    var penger = document.getElementById("penger").value;
    if (penger >4000) {
        alert("Du har ikke nokk penger")
    }
    else if (penger <=4000) {
        alert("Du har ikke nokk penger")
    }


    var pinkode = document.getElementById("pinkode").value;
    if (pinkode ==  pinkode) {
    alert("Det er feil kode")
    }
}

