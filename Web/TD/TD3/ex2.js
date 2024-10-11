function reverse(tab) {
  let tab2 = [];
  let i = 0;
  let tab_len = tab.length;
  for (i; i < tab_len; i++) {
    var elt = tab.shift();
    tab2.unshift(elt);
  }
  return tab2;
}

console.log(reverse([1, 2, 3]));
