function traverse(obj, cond, f) {
  for (var i in obj) {
    if (obj.hasOwnProperty(i) && cond(obj[i])) {
      f(obj[i]);
    }
    if (typeof obj[i] === "object") {
      traverse(obj[i], cond, f);
    }
  }
}
