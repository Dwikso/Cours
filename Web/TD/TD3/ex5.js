function myShiftSlice(tab) {
  var elt = tab.slice(0, 1);
  var tab2 = tab.slice(1);
  for (var i = 0; i < tab2.length; i++) {
    tab[i] = tab2[i];
  }
  tab.length--;
  return elt[0];
}

tab = [1, 2, 3, 4, 5];
console.log(myShiftSlice(tab));

function myShiftSplice(tab) {
  var res = tab.splice(0, 1);
  return res[0];
}

tab = [1, 2, 3, 4, 5];
console.log(myShiftSplice(tab));
