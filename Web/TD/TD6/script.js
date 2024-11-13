document.addEventListener('DOMContentLoaded', function() {
  var books = document.getElementById('totor-books');
  const li = document.createElement('li');
  li.textContent = "Totor à la crèche"
  books.insertBefore(li, books.firstChild);
  const li2 = document.createElement("li");
  li2.textContent = "Totor en grève"
  books.insertBefore(li2,books.lastElementChild)
  const newBooks = document.createElement('li');
  newBooks.textContent = "Totor fait fortune";
  books.appendChild(newBooks);
  
})


Node.prototype.insertAfter = function(noeudAInserer, noeudDeRef) {
    if(noeudDeRef.nextSibling) {
      return this.insertBefore(noeudAInserer,noeudDeRef.nextSibling)
    } else {
      return this.appendChild(noeudAInserer)
    }
}


