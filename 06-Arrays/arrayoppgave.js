const farger =["Gul", "Grønn", "Rød", "Blå", "Oransj"];
farger.sort();
console.log(farger);


const bilmerker=["Opel", "Volvo", "Tesla", "DMC","Ferrari"];
bilmerker.sort();
bilmerker.reverse();
console.log(bilmerker);

const tal =["70", "60", "91", "20", "320", "66", "420"];
tal.sort(function(a,b){return a - b});
console.log(tal);

const tal2 =["84", "69", "43", "1000", "550"]
tal.sort(function(a,b){return a -b});
console.log(tal2);

function myFunction() {
    tal2.sort();
document.getElementById("array4").innerHTML = tal2;
}
