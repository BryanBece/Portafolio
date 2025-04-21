function loadPokemonDetails(name) {
    fetch(`/pokemon/${name.toLowerCase()}/`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert("Error: " + data.error);
            } else {
                document.getElementById('pokemonModalLabel').innerText = data.name.charAt(0).toUpperCase() + data.name.slice(1);
                
                document.getElementById('pokemonTypes').innerHTML = data.types.map(type => `<span class="type-badge type-${type.toLowerCase()}">${type}</span>`).join(", ");
                document.getElementById('pokemonStrongAgainst').innerHTML = data.strong_against.map(type => `<span class="type-badge type-${type.toLowerCase()}">${type}</span>`).join(", ") || "N/A";
                document.getElementById('pokemonWeakAgainst').innerHTML = data.weak_against.map(type => `<span class="type-badge type-${type.toLowerCase()}">${type}</span>`).join(", ") || "N/A";
                
                document.getElementById('pokemonGeneration').innerText = data.generation;
                document.getElementById('pokemonSprite').src = data.sprite || 'https://via.placeholder.com/120';

                // Cargar estadísticas en texto plano
                loadStatsList(data.stats);

                let pokemonModal = new bootstrap.Modal(document.getElementById('pokemonModal'));
                pokemonModal.show();
            }
        })
        .catch(error => console.error('Error al cargar detalles:', error));
}

function loadStatsList(stats) {
    const statsList = document.getElementById('pokemonStats');
    statsList.innerHTML = ''; // Limpiar la lista antes de agregar nuevos elementos
    
    for (const [stat, value] of Object.entries(stats)) {
        statsList.innerHTML += `<li><strong>${stat}:</strong> ${value}</li>`;
    }
}

function searchPokemon() {
    const searchValue = document.getElementById('pokemonSearchInput').value.trim();
    if (searchValue) {
        loadPokemonDetails(searchValue);
    } else {
        alert("Por favor, ingresa un nombre o número de Pokémon.");
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                loadPokemonSprite(entry.target);
                observer.unobserve(entry.target);
            }
        });
    }, {
        rootMargin: '50px'
    });

    document.querySelectorAll(".pokemon-sprite").forEach(img => {
        observer.observe(img);
    });
});

function loadPokemonSprite(element) {
    const pokemonName = element.dataset.pokemon;
    fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`)
        .then(response => response.json())
        .then(data => {
            element.src = data.sprites.front_default;
            element.alt = `${pokemonName} sprite`;
        })
        .catch(error => console.error("Error al cargar el sprite de Pokémon:", error));
}

