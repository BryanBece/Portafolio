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
    // Llama a la función de carga de sprites cuando el contenido de la página esté listo
    loadPokemonSprites();
});

function loadPokemonSprites() {
    const pokemonElements = document.querySelectorAll(".pokemon-sprite");
    pokemonElements.forEach(element => {
        const pokemonName = element.id.replace("sprite-", ""); // Extrae el nombre de Pokémon desde el id
        fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`)
            .then(response => response.json())
            .then(data => {
                const spriteUrl = data.sprites.front_default; // Obtiene la URL del sprite
                element.src = spriteUrl; // Asigna la URL de la imagen al atributo src de la tarjeta
                element.alt = `${pokemonName} sprite`; // Añade un alt descriptivo
            })
            .catch(error => console.error("Error al cargar el sprite de Pokémon:", error));
    });
}

