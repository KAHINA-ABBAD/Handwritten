import os
from pathlib import Path

# Chemins de base
BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / 'models'
STATIC_DIR = BASE_DIR / 'static'
UPLOAD_DIR = STATIC_DIR / 'uploads'

class Config:
    """Configuration de base pour Flask"""
    
    # Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-change-in-production'
    DEBUG = False
    TESTING = False
    
    # Upload
    UPLOAD_FOLDER = str(UPLOAD_DIR)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    
    # Model
    MODEL_PATH = str(MODELS_DIR / 'best_cnn_model.h5')
    
    # Image processing
    IMG_HEIGHT = 28
    IMG_WIDTH = 28
    IMG_CHANNELS = 1

class DevelopmentConfig(Config):
    """Configuration développement"""
    DEBUG = True

class ProductionConfig(Config):
    """Configuration production"""
    DEBUG = False

# Dictionnaire des configs
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
