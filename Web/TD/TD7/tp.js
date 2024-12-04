function Complexe(r = 0, i = 0) {
  Object.defineProperty(this, "real", {
    value: r,
    writable: false,
    enumerable: true,
    configurable: false,
  });
  Object.defineProperty(this, "imaginary", {
    value: i,
    writable: false,
    enumerable: true,
    configurable: false,
  });
}

// Définit rho et theta sur le prototype, en utilisant une propriété à chaque fois
Object.defineProperty(Complexe.prototype, "rho", {
  get: function () {
    return this.mod();
  },
  enumerable: true,
  configurable: false,
});

Object.defineProperty(Complexe.prototype, "theta", {
  get: function () {
    if (this.rho === 0) {
      return 0;
    }
    if (this.imaginary >= 0) {
      return Math.acos(this.real / this.rho);
    }
    return -Math.acos(this.real / this.rho);
  },
  enumerable: true,
  configurable: false,
});

// Définition des méthodes du prototype pour l'addition et la multiplication
Complexe.prototype.addition = function (otherComplexe) {
  return new Complexe(
    this.real + otherComplexe.real,
    this.imaginary + otherComplexe.imaginary,
  );
};

Complexe.prototype.multiplication = function (otherComplexe) {
  const real =
    this.real * otherComplexe.real - this.imaginary * otherComplexe.imaginary;
  const imaginary =
    this.real * otherComplexe.imaginary + this.imaginary * otherComplexe.real;

  return new Complexe(real, imaginary);
};

Complexe.prototype.conj = function () {
  return new Complexe(this.real, -this.imaginary);
};

Complexe.prototype.mod = function () {
  return Math.sqrt(this.real * this.real + this.imaginary * this.imaginary);
};

Complexe.prototype.toString = function () {
  return `(${this.real}, ${this.imaginary})`;
};

function ComplexeMut(real = 0, img = 0) {
  this.real = real;
  this.img = img;
}

ComplexeMut.prototype = Object.create(Complexe.prototype);
