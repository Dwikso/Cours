window.addEventListener('DOMContentLoaded', () => {
    createButton();
})

function createButton() {
    let div = document.getElementById('div-button')
    let l = document.getElementById('log')
    for(let i = 0; i < 10; i++) {
        let button = document.createElement('button');
        div.appendChild(button);
        button.textContent = `Button ${i}`
        button.addEventListener('click', function() {
            log.textContent = i;
        })
        setTimeout(function(elm) {
            return function() {
                elm.parentNode.removeChild(elm);
            };
        }(button), Math.random()*5000 + 5000)
    }
}

button = document.getElementById('clickme');
// Desactiver fonction anonyme
button.addEventListener('click', function(){alert("click");});

var button, parent, newest;
document.getElementById("stop").addEventListener('click', function(){
    parent = button.parentNode;
    newest = button.cloneNode(true);

    parent.insertBefore(newest, button)
    parent.removeChild(button);
    // Parent.appendChild(newest): si tout seul
})

