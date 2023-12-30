let currentPage = 1;
const itemsPerPage = 2; 
let data = []; 

function showPage(page) {
    const metadataTablesContainer = document.getElementById('metadataTablesContainer');
    metadataTablesContainer.innerHTML = '';

    const startIndex = (page - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;
    data.slice(startIndex, endIndex).forEach(fileData => {
        const fileTitle = document.createElement('h2');
        fileTitle.className = 'file-title';
        fileTitle.textContent = fileData.file_name;
        metadataTablesContainer.appendChild(fileTitle);

        const table = document.createElement('table');
        table.className = 'metadata-table';

        const thead = table.createTHead();
        const headerRow = thead.insertRow();
        headerRow.appendChild(document.createElement('th')).textContent = 'Attribut';
        headerRow.appendChild(document.createElement('th')).textContent = 'Valeur';

        const tbody = table.createTBody();
        if (fileData.metadata) {
            Object.entries(fileData.metadata).forEach(([key, value]) => {
                const row = tbody.insertRow();
                row.insertCell().textContent = key;
                row.insertCell().textContent = value;
            });
        } else {
            const row = tbody.insertRow();
            row.insertCell().textContent = 'Erreur';
            row.insertCell().textContent = 'Aucune métadonnée disponible';
        }

        metadataTablesContainer.appendChild(table);
    });

    currentPage = page;
}

function nextPage() {
    if (currentPage * itemsPerPage < data.length) {
        showPage(currentPage + 1);
    }
}

function previousPage() {
    if (currentPage > 1) {
        showPage(currentPage - 1);
    }
}

document.addEventListener('DOMContentLoaded', function () {
    fetch('/metadata_data')
        .then(response => response.json())
        .then(fetchedData => {
            data = fetchedData; 
            showPage(currentPage); 
        })
        .catch(error => console.error('Error fetching metadata:', error));

    document.getElementById('prev-btn').addEventListener('click', previousPage);
    document.getElementById('next-btn').addEventListener('click', nextPage);
});
