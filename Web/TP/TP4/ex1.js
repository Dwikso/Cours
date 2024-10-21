function randomInt1(max) {
  return Math.round(Math.random() * max);
}

// console.log(randomInt1(10));

function randomInt2(min, max) {
  return Math.round(Math.random() * (max - min) + min);
}

// console.log(randomInt2(10, 50));

function randomIntArray(min, max, n) {
  let tab = [];
  for (let i = 0; i < n; i++) {
    tab.push(randomInt2(min, max));
  }
  return tab;
}

// console.log(randomIntArray(3, 15, 5));

function moyenne(tab) {
  let somme = 0;
  for (let i = 0; i < tab.length; i++) {
    somme += tab[i];
  }
  return somme / tab.length;
}

var tab = randomIntArray(1, 101, 10000);
// console.log(moyenne(tab));

// On remarque le moyenne est toujours proche de 50

function occurences(tab, min, max) {
  let res = new Object();
  for (let i = min; i < max; i++) {
    res[i] = 0;
  }
  for (let i = 0; i < tab.length; i++) {
    if (tab[i] >= min && tab[i] < max) {
      res[tab[i]]++;
    }
  }
  return res;
}

// let tab3 = randomIntArray(1, 11, 10);
// console.log(occurences(tab3, 1, 11));

function stats(tab, min, max) {
  let occurence = occurences(tab, min, max);
  let total = tab.length;
  let stats = new Object();
  for (let i = min; i < max; i++) {
    stats[i] = occurence[i] / total;
  }
  return stats;
}

// let tab4 = randomIntArray(1, 11, 10);
// console.log(stats(tab4, 1, 11));

// Exercice 2

function excusotron(textArray) {
  let excuse = "";
  for (let i = 0; i < textArray.length; i++) {
    let randomIndex = Math.floor(Math.random() * textArray[i].length);
    excuse += textArray[i][randomIndex] + " ";
  }
  return excuse;
}

var pipoText1 = [
  ["Ce matin,", "Tantôt,"],
  ["j'ai eu une panne"],
  ["de réveil.", "d'oreiller."],
];
var pipoText2 = [
  [
    "Tôt dans la matinée,",
    "Vers 4h du matin,",
    "Hier soir,",
    "Tard dans la nuit,",
    "En pleine nuit,",
  ],
  [
    "alors que",
    "pendant que",
    "au moment où",
    "tandis que",
    "comme",
    "cependant que",
  ],
  [
    "je dormais après avoir relu pour la 3ème fois la Comédie humaine de Balzac,",
    "je sommeillais en attendant de me lever pour mon footing quotidien de 5h du matin,",
    "je somnollais après avoir passé en revue une étude du Figaro Economique,",
    "je m'étais assoupi sur une des oeuvres passionnantes de Friedrich Wilheim Nietzsche,",
    "je me reposais après avoir pratiqué 2h intenses de Squash,",
    "je m'étais endormis sur un article fort intéressant du Herald Tribune,",
    "je faisais un somme après avoir fini de traduire Guerre & Paix en Mandarin,",
    "je m'étais assoupi sur la brillante émission 'Chasse et Pêche',",
  ],
  [
    "mon chat",
    "mon chien",
    "ma vieille grand-mère",
    "mon perroquet",
    "mon sanglier domestique",
    "ma belle-mère",
    "mon iguane asthmatique",
  ],
  [
    "a joué avec le fil électrique de",
    "s'est pris les pates dans le fil électrique de",
    "a appuyé par mégarde sur le bouton OFF de",
    "a effleuré par inadvertance le Snooze de",
    "a renversé du Coca sur",
    "a fait tomber dans la baignoire",
    "a rebooté",
  ],
  ["mon radio-réveil qui n'a donc pas sonné, et ce n'est"],
  [
    "que lorsque les pompiers sont entrés en hurlant 'AU FEU!'",
    "qu'au moment où les huissiers (venus pour le voisin) ont enfoncé la porte",
    "qu'avec l'arrivée du SAMU, venu chercher ma grand-mère",
    "qu'après l'entrée fracassante de la SPA",
    "qu'au moment où les pompes-funèbres (venues chercher ma belle-mère) ont sonné à la porte",
    "que quand le plombier est venu réparer l'inondation",
    "qu'avec la visite d'un représentant du Téléthon venu me remercier pour mon généreux don de la veille",
  ],
  [
    "que je me suis réveillé, trop en retard pour être à l'heure à la fac.",
    "que j'ai repris connaissance et me suis précipité tardivement à la fac.",
    "que j'ai réalisé qu'il était trop tard pour venir à la fac ce matin.",
    "que j'ai bondi hors de mon lit pour me ruer à la fac.",
  ],
];

console.log(excusotron(pipoText2));
