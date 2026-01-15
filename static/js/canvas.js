function predict() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    
    if (!file) {
        alert('Veuillez sélectionner une image');
        return;
    }
    
    // Afficher l'aperçu
    const reader = new FileReader();
    reader.onload = function(e) {
        document.getElementById('preview').innerHTML = 
            `<img src="${e.target.result}" style="max-width: 200px;">`;
    };
    reader.readAsDataURL(file);
    
    // Envoyer au serveur
    const formData = new FormData();
    formData.append('file', file);
    
    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert('Erreur : ' + data.error);
            return;
        }
        
        // Afficher les résultats
        document.getElementById('result').style.display = 'block';
        document.getElementById('predicted-class').textContent = data.predicted_class;
        document.getElementById('confidence').textContent = (data.confidence * 100).toFixed(2);
        
        // Afficher le top 3
        let top3HTML = '<h3>Top 3 prédictions :</h3><ul>';
        data.top3.forEach(item => {
            top3HTML += `<li>Classe ${item.class} : ${(item.probability * 100).toFixed(2)}%</li>`;
        });
        top3HTML += '</ul>';
        document.getElementById('top3').innerHTML = top3HTML;
    })
    .catch(error => {
        alert('Erreur : ' + error);
    });
}
