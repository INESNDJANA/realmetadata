document.addEventListener('DOMContentLoaded', function () {
    fetch('/metadata_data')
        .then(response => response.json())
        .then(data => {
            const metadataList = document.getElementById('metadataList');
            for (const [fileName, fileMetadata] of Object.entries(data)) {
                const listItem = document.createElement('li');
                
                // Convertit les métadonnées en chaîne pour l'affichage
                const metadataStr = JSON.stringify(fileMetadata, null, 2);
                listItem.textContent = `${fileName}: ${metadataStr}`;
                metadataList.appendChild(listItem);
            }
        })
        .catch(error => console.error('Error fetching metadata:', error));
});
