function changeColor() {
    const body = document.body;
    body.style.backgroundColor = body.style.backgroundColor === 'white' ? 'yellow' : 'white';
}

document.addEventListener("DOMContentLoaded", () => {  
    const getdiv = document.querySelector("div");
    getdiv.addEventListener('mouseover', () => {
        rdmimg();
        getdiv.style.backgroundColor = getdiv.style.backgroundColor === 'white' ? 'yellow' : 'white';
    })

  });


function rdmimg() {
    const listeImg = ['./MBAPPE.jpg', './edf.jpg', './lens.png', './Bride.webp']
    var random = Math.floor(Math.random() * listeImg.length);
    document.body.style.backgroundImage = `url(${listeImg[random]})`;
}

