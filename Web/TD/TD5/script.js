function findp(n) {
  if (typeof n !== "object") return null;
  n = n.firstChild;
  var m;

  while (n) {
    if (n.nodeType == Node.ELEMENT_NODE && n.nodeName == "P") {
      return n;
    } else {
      m = findp(n);
      if (m !== null) {
        return m;
      }
    }
    n = n.nextSibling;
  }
  return null;
}

function maj(n) {
  if (typeof n !== "object") return;
  var n = n.firstChild;
  while (n) {
    if (n.nodeType === Node.TEXT_NODE) {
      n.nodeValue = n.nodeValue.toUpperCase();
    } else {
      maj(n);
    }
    n = n.nextSibling;
  }
}

docuement.addEventListener("DOMContentLoaded", function () {
  maj(document.body);
});
