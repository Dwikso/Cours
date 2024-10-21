function reverse(tab) {
  let tab2 = [];
  let i = 0;
  let tab_len = tab.length;
  for (i; i < tab_len; i++) {
    var elt = tab.pop();
    tab2.push(elt);
  }
  return tab2;
}

console.log(reverse([1, 2, 3]));
