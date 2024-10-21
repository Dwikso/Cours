function AfficheTable() {
  let i = 0;
  while (i < 10) {
    let table = document.createElement("table");
    table.innerHTML = `<tr><td>{i}</td></tr>`;
    document.body.appendChild(table);
    i++;
  }
}

AfficheTable();
