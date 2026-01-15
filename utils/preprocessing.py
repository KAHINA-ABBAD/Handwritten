import numpy as np
from PIL import Image
import io

def preprocess_image(img_bytes, target_size=(28, 28)):
    """
    Prétraite une image pour le modèle MNIST
    
    Args:
        img_bytes: bytes de l'image
        target_size: tuple (height, width)
    
    Returns:
        np.array de shape (1, 28, 28, 1) normalisé
    """
    # Charger l'image
    img = Image.open(io.BytesIO(img_bytes))
    
    # Convertir en niveaux de gris
    img = img.convert('L')
    
    # Redimensionner
    img = img.resize(target_size, Image.Resampling.LANCZOS)
    
    # Convertir en array numpy
    img_array = np.array(img)
    
    # Inverser si nécessaire (MNIST = blanc sur fond noir)
    if img_array.mean() > 127:
        img_array = 255 - img_array
    
    # Normaliser [0, 255] -> [0, 1]
    img_array = img_array.astype('float32') / 255.0
    
    # Reshape pour le modèle (batch, height, width, channels)
    img_array = img_array.reshape(1, target_size[0], target_size[1], 1)
    
    return img_array

def allowed_file(filename, allowed_extensions):
    """Vérifie si l'extension du fichier est autorisée"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions
