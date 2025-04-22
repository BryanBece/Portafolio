
function showChampionDetails(championId) {
    fetch(`/lolWeb/champion/${championId}/`)
        .then(response => response.text())
        .then(html => {
            document.getElementById('championDetails').innerHTML = html;
            document.getElementById('championModal').style.display = 'block';
        });
}

document.querySelector('.close').onclick = function() {
    document.getElementById('championModal').style.display = 'none';
}

window.onclick = function(event) {
    if (event.target == document.getElementById('championModal')) {
        document.getElementById('championModal').style.display = 'none';
    }
}
