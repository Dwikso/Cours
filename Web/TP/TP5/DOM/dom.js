function nodeMajuscule(n) {
  if (typeof n !== "object") return;
  var n = n.firstChild;
  while (n) {
    if (n.nodeType === Node.TEXT_NODE) {
      n.nodeValue = n.nodeValue.toUpperCase();
    } else {
      nodeMajuscule(n);
    }
    n = n.nextSibling;
  }
}

function majh1(n) {
  if (!(n instanceof Node)) return;
  let child = n.firstChild;
  while (child) {
    if (child.nodeType === Node.TEXT_NODE) {
      child.nodeValue = child.nodeValue.toUpperCase();
    } else {
      majh1(child);
    }
    child = child.nextSibling;
  }
}

function capitalizeTextInHeaders(node) {
  if (node.nodeType === Node.ELEMENT_NODE) {
      if (node.tagName === 'H1' || node.tagName === 'H2') {
          node.childNodes.forEach(child => {
              if (child.nodeType === Node.TEXT_NODE) {
                  child.textContent = child.textContent.toUpperCase();
              }
          });
      }
      node.childNodes.forEach(capitalizeTextInHeaders);
  }
}

function isTitle(node) {
  if (node.nodeType === Node.ELEMENT_NODE) {
    if (node.tagName === "H1" || node.tagName === "H2") {
      return true;
    }
  }
  return false;
}

function anyRec(f, node) {
  if (f(node)) return true;
  
}

document.addEventListener("DOMContentLoaded",  () =>{
  const title = document.title;
  alert(`Titre de la page : ${title}`);
  document.getElementById("h1").textContent = "Document Object Model (DOM)";
  capitalizeTextInHeaders(document.body);
  const h1Element = document.getElementById("h1");
  majh1(h1Element);
  console.log(isTitle(h1Element));
});
