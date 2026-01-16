import os
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from collections import Counter

# === CONFIGURATION ===
DATA_FOLDER = Path("datas")
OUTPUT_FOLDER = Path("outputs")
OUTPUT_FOLDER.mkdir(exist_ok=True)

print("Chargement des données…")

images = []
labels = []

# Lecture des images dans les sous-dossiers
for label_folder in DATA_FOLDER.iterdir():
    if label_folder.is_dir():
        label = label_folder.name  # nom du dossier = label
        print(f" - Lecture du dossier : {label}")

        for img_path in label_folder.glob("*.png"):
            try:
                img = Image.open(img_path).convert("L")     # gris
                img = img.resize((28, 28))                  # normalisation
                img_array = np.array(img)

                images.append(img_array)
                labels.append(label)

            except Exception as e:
                print(f"Erreur avec {img_path} : {e}")

images = np.array(images)
labels = np.array(labels)

print(f"\nTotal images chargées : {len(images)}")

# === APERÇU D’IMAGES ===
def show_samples():
    plt.figure(figsize=(10, 4))
    for i in range(10):
        plt.subplot(2, 5, i + 1)
        plt.imshow(images[i], cmap="gray")
        plt.title(f"Label : {labels[i]}")
        plt.axis("off")

    plt.tight_layout()
    plt.savefig(OUTPUT_FOLDER / "sample_images.png")
    plt.show()

print("Affichage d'un échantillon…")
show_samples()

# === HISTOGRAMME DES LABELS ===
def plot_label_distribution():
    count = Counter(labels)
    plt.figure(figsize=(6, 4))
    plt.bar(count.keys(), count.values())
    plt.xlabel("Labels")
    plt.ylabel("Nombre d'images")
    plt.title("Distribution des classes")
    plt.savefig(OUTPUT_FOLDER / "class_distribution.png")
    plt.show()

print("Génération de l'histogramme des labels…")
plot_label_distribution()

print("\n✔️ Analyse terminée !")
print("→ Résultats enregistrés dans le dossier : outputs/")
