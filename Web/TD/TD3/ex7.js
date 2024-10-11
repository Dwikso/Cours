function doublons(tab) {
  let i = 0;
  let j = i + 1;
  for (i; i < tab.length; i++) {
    for (j; j < tab.length; j++) {
      if (tab[i] === tab[j]) {
        tab.splice(j, 1);
        j--;
      }
    }
  }
  return tab;
}

tab = [9, 12, 77, 31, 14, 54, 11];
console.log(doublons(tab));
