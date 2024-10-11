function Tableau_plein(tab) {
  let tab2 = [];
  let i = 0;
  for (i; i < tab.length; i++) {
    if (tab[i] != undefined) {
      tab2.push(tab[i]);
    }
  }
  return tab2;
}

tab = ["1", "2", " ", " ", "4"];

console.log(Tableau_plein(tab));
