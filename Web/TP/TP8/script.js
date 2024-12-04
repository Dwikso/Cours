class Joujou {
  constructor(name, poids, prix, volume, estEmballe, destinataire) {
    this.name = name;
    this.poids = poids;
    this.prix = prix;
    this.volume = volume;
    this.estEmballe = estEmballe;
    this.destinataire = destinataire;
  }
}

Joujou.prototype.afficher = function () {
  console.log(
    `Le joujou ${this.name} est de ${this.poids} kg, prix de ${this.prix} euros, un volume de ${this.volume} m³,est-il emballe ? ${this.estEmballe}, destinataire ${this.destinataire}`,
  );
};

Joujou.prototype.emballe = function () {
  this.estEmballe = true;
};

class Hotte {
  constructor(poidsMax, volMax) {
    this.joujoux = [];
    this.poidsMax = poidsMax;
    this.volMax = volMax;
  }

  get poidsContenu() {
    return this.joujoux.reduce((total, joujou) => total + joujou.poids, 0);
  }

  get volumeContenu() {
    return this.joujoux.reduce((total, joujou) => total + joujou.volume, 0);
  }
}

Hotte.prototype.afficher = function () {
  return (
    "Dans la Hoote, il y a " +
    this.joujoux.map((joujou) => joujou.name).join(", ")
  );
};

Hotte.prototype.sontEmballes = function () {
  return this.joujoux.every((joujou) => joujou.estEmballe);
};

Hotte.prototype.emballeTout = function () {
  this.joujoux.forEach((joujou) => joujou.emballe());
};

Hotte.prototype.ajouterJoujou = function (joujou) {
  if (this.poidsContenu + joujou.poids <= this.poidsMax) {
    if (this.sontEmballes()) {
      this.emballeTout();
    }
    this.joujoux.push(joujou);
  }
};

Hotte.prototype.chercheJoujoux = function (destinataire) {
  return this.joujoux.filter((joujou) => joujou.destinataire === destinataire);
};

Hotte.prototype.retireJoujoux = function (destinataire) {
  this.joujoux = this.joujoux.filter(
    (joujou) => joujou.destinataire !== destinataire,
  );
};

const joujou1 = new Joujou("Joujou 1", 10, 100, 100, false, "Jean");
joujou1.afficher();
joujou1.emballe();
joujou1.afficher();

const joujou2 = new Joujou("Joujou 2", 20, 200, 200, false, "dest");
joujou2.afficher();
joujou2.emballe();
joujou2.afficher();

const joujou3 = new Joujou("Joujou 3", 30, 300, 300, false, "Jean");
joujou3.afficher();
joujou3.afficher();

const Hotte1 = new Hotte(100, 100);
Hotte1.ajouterJoujou(joujou1);
Hotte1.ajouterJoujou(joujou2);
Hotte1.ajouterJoujou(joujou3);
console.log(Hotte1.afficher());
console.log(Hotte1.sontEmballes());
console.log(Hotte1.chercheJoujoux("dest"));
Hotte1.retireJoujoux("dest");
console.log(Hotte1.afficher());
