function union(liste1, liste2) {
  if (!Array.isArray(liste1) || !Array.isArray(liste2)) {
    return void 0;
  }
  var obj = {};
  for (var i = liste1.length - 1; i >= 0; i--) {
    obj[liste1[i]] = liste1[i];
  }
  for (var j = liste2.length - 1; j >= 0; j--) {
    obj[liste2[j]] = liste2[j];
  }
  return Object.keys(obj);
}

liste1 = [1, 2, 3];
liste2 = [2, 3, 4];

console.log(union(liste1, liste2));
