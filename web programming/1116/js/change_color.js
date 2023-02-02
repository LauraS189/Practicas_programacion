var heading = document.querySelector('#heading');
heading.onclick = function() {
    if(heading.style.color == 'blue')
        heading.style.color = 'red';
    else 
        heading.style.color = 'blue';
}
