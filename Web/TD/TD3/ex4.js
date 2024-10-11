function mypop(tab) {
  let last_element = tab.slice(-1);
  tab.length--;
  return last_element[0];
}

console.log(mypop([1, 2, 3]));

function mypopSplice(tab) {
  return tab.splice[0];
}
