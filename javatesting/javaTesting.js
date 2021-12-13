var date = new Date(); // henter informasjon om dagen
var tid = date.getHours(); // henter klokken
var mnd = date.getMonth();
var dato = date.getDate();
var navn = "Lars"

if(navn === "Lars" && mnd === 7 && dato === 10) {
    console.log("Gratulerer med navnedagen, Lars!");
} else{
    console.log("Det er desverre ikkje navnedagen din i dag");
}

