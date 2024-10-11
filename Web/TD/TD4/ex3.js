var p1 = { x: 5, y: 3 };
var p2 = { x: 3, y: 5 };

function distManhattan(p1, p2) {
  return Math.abs(p1.x - p2.x) + Math.abs(p1.y - p2.y);
}

console.log("Exercice 3 : Distance Manhattan", distManhattan(p1, p2));
