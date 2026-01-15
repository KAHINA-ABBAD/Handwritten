# Handwritten Digits Classification

## 📋 Description
Système de classification de chiffres manuscrits MNIST utilisant des réseaux de neurones profonds (MLP et CNN) avec déploiement Flask.

## 🎯 Objectif
Atteindre un taux d'erreur < 1% sur le dataset MNIST et déployer le modèle via une interface web interactive.

## 📊 Dataset
- **Source** : MNIST Database
- **Training set** : 60,000 images
- **Test set** : 10,000 images
- **Format** : 28x28 pixels, niveaux de gris

## 🏗️ Architecture du projet
```
digits-classification/
├── notebooks/          # Exploration et modélisation
├── models/            # Modèles sauvegardés
├── app/               # Application Flask
└── assets/            # Visualisations
```

## 🚀 Installation
```bash
# Cloner le repository
git clone https://github.com/votre-username/digits-classification.git
cd digits-classification

# Créer l'environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Installer les dépendances
pip install -r requirements.txt
```

## 💻 Utilisation

### Entraînement des modèles
```bash
jupyter notebook notebooks/02_modeling.ipynb
```

### Lancer l'application web
```bash
cd app
python app.py
```
Accéder à : http://localhost:5000

## 📈 Résultats

| Modèle | Accuracy | Loss | Params |
|--------|----------|------|--------|
| MLP    | TBD      | TBD  | TBD    |
| CNN    | TBD      | TBD  | TBD    |

## 🔧 Technologies
- **Deep Learning** : TensorFlow/Keras
- **Web** : Flask, HTML/CSS/JavaScript
- **Data Science** : NumPy, Pandas, Scikit-learn
- **Visualisation** : Matplotlib, Seaborn

## 👤 Auteur
Kahina ABBAD - Oussama DEBBOU - Pape Ahmed Fall

Master 1 Expert en IA 

## 📝 License
MIT
