"""
Application Flask minimale pour tester l'installation
"""

from flask import Flask, render_template, request, jsonify
import numpy as np
import os

app = Flask(__name__)

# Configuration basique
app.config['SECRET_KEY'] = 'test-key'
app.config['DEBUG'] = True

@app.route('/')
def index():
    """Page d'accueil"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Test MNIST App</title>
    </head>
    <body>
        <h1>Application MNIST - Test Installation</h1>
        <p>✓ Flask fonctionne correctement</p>
        <a href="/test">Tester les imports</a>
    </body>
    </html>
    """

@app.route('/test')
def test():
    """Tester les imports nécessaires"""
    results = {}
    
    # Test TensorFlow
    try:
        import tensorflow as tf
        results['tensorflow'] = f"✓ Version {tf.__version__}"
    except ImportError as e:
        results['tensorflow'] = f"✗ Erreur: {e}"
    
    # Test Keras
    try:
        import keras
        results['keras'] = f"✓ Version {keras.__version__}"
    except ImportError as e:
        results['keras'] = f"✗ Erreur: {e}"
    
    # Test NumPy
    try:
        import numpy as np
        results['numpy'] = f"✓ Version {np.__version__}"
    except ImportError as e:
        results['numpy'] = f"✗ Erreur: {e}"
    
    # Test Pillow
    try:
        from PIL import Image
        results['pillow'] = "✓ Installé"
    except ImportError as e:
        results['pillow'] = f"✗ Erreur: {e}"
    
    # Créer le HTML de réponse
    html = "<h1>Test des dépendances</h1><ul>"
    for lib, status in results.items():
        html += f"<li><strong>{lib}</strong>: {status}</li>"
    html += "</ul>"
    html += '<br><a href="/">Retour</a>'
    
    return html

@app.route('/health')
def health():
    """Healthcheck"""
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    print("=" * 50)
    print("Démarrage de l'application de test")
    print("Accéder à: http://localhost:5000")
    print("=" * 50)
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )