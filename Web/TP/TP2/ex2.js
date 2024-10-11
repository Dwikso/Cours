function CompteMots(phrase) {
  let mots = phrase.split(" ");
  return mots.length;
}

// console.log(CompteMots("la maman de Colette et de Daniel"));

// Compte le nombre de mots dans une phrase séparés par un au moins un  espace
// Exemple : CompteMots2(" la maman    de Colette et de   Daniel  ") => 7

function CompteMots2(phrase) {
  let mots = phrase.split(" ");
  return mots.filter((mot) => mot.length > 0).length;
}

// console.log(CompteMots2(" la maman    de Colette et de   Daniel  "));
