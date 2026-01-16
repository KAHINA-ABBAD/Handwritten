import os
from pathlib import Path
import zipfile
import shutil
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import csv

# CONFIG 
PROJECT_ROOT = Path('.')  
DATA_FOLDER = PROJECT_ROOT / "datas"
OUTPUT_FOLDER = PROJECT_ROOT / "outputs"
OUTPUT_FOLDER.mkdir(exist_ok=True)
IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif'}

print("DEBUG START")
print("Project root:", PROJECT_ROOT.resolve())
print("Data folder:", DATA_FOLDER.resolve())

# Trouver fichiers récursivement
def find_files_recursively(folder: Path, exts=None):
    files = []
    if not folder.exists():
        return files
    for p in folder.rglob('*'):
        if p.is_file():
            if exts is None or p.suffix.lower() in exts:
                files.append(p)
    return sorted(files)

# 1) Cherche images dans datas/
image_files = find_files_recursively(DATA_FOLDER, IMAGE_EXTS)
print(f"\nImages trouvées dans {DATA_FOLDER}: {len(image_files)}")

# 2) Si aucune image trouvée, regarde s'il y a un archive.zip à la racine et liste son contenu
archive = PROJECT_ROOT / "archive.zip"
if not image_files and archive.exists():
    print(f"\nAucune image trouvée dans {DATA_FOLDER}. Le fichier archive.zip existe -> on l'inspecte.")
    with zipfile.ZipFile(archive, 'r') as z:
        all_names = z.namelist()
        print(f"Nombre d'entrées dans archive.zip : {len(all_names)}")
        # compter les images dans l'archive
        images_in_zip = [n for n in all_names if Path(n).suffix.lower() in IMAGE_EXTS]
        print(f"Images repérées dans archive.zip : {len(images_in_zip)} (exemples : {images_in_zip[:10]})")
        if images_in_zip:
            # extraire automatiquement dans datas/extracted
            extracted_dir = DATA_FOLDER / "extracted_from_archive"
            print(f"Extraction des images dans : {extracted_dir} ...")
            extracted_dir.mkdir(parents=True, exist_ok=True)
            for name in images_in_zip:
                # créer sous-fichiers nécéssaires 
                target_path = extracted_dir / name
                target_path.parent.mkdir(parents=True, exist_ok=True)
                with z.open(name) as src, open(target_path, 'wb') as dst:
                    shutil.copyfileobj(src, dst)
            print("Extraction terminée.")
            # mise à jour de la liste d'images
            image_files = find_files_recursively(DATA_FOLDER, IMAGE_EXTS)

# 3) Si toujours aucune image, cherche tout type de fichier utile (csv, npz)
if not image_files:
    other_files = list(PROJECT_ROOT.rglob('*.*'))
    # filtrer utiles
    useful = [p for p in other_files if p.suffix.lower() in {'.csv', '.npz', '.zip', '.txt'}]
    print("\nAucune image trouvée. Fichiers 'utiles' trouvés à la racine / sous-dossiers (csv/npz/zip/txt) :")
    for p in useful[:50]:
        print(" -", p.relative_to(PROJECT_ROOT))
    # on génère un rapport et quitte proprement
    with open(OUTPUT_FOLDER / "file_report.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["path", "suffix", "size_bytes"])
        for p in useful:
            try:
                writer.writerow([str(p.relative_to(PROJECT_ROOT)), p.suffix.lower(), p.stat().st_size])
            except Exception:
                pass
    print(f"\nUn rapport a été sauvegardé : {OUTPUT_FOLDER / 'file_report.csv'}")
    print("Si tu veux que j'extraie ou que je lise un fichier spécifique (par ex. un .csv ou .npz), indique son chemin ou colle ici le contenu de file_report.csv.")
    print("FIN DEBUG (aucune image détectée).")
    exit(0)

# 4) Si on a des images : rapport et affichage
print(f"\nTotal images détectées : {len(image_files)}")
# compte par extension
from collections import Counter
ext_counts = Counter([p.suffix.lower() for p in image_files])
print("Répartition par extension :", dict(ext_counts))

# montrer 20 premiers fichiers
print("\nExemples (20 premiers) :")
for p in image_files[:20]:
    print(" -", p.relative_to(PROJECT_ROOT))

# sauvegarder le rapport complet
with open(OUTPUT_FOLDER / "file_report.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["path", "suffix", "size_bytes"])
    for p in image_files:
        try:
            writer.writerow([str(p.relative_to(PROJECT_ROOT)), p.suffix.lower(), p.stat().st_size])
        except Exception:
            pass
print(f"\nRapport complet sauvegardé : {OUTPUT_FOLDER / 'file_report.csv'}")

# 5) Tenter de charger et d'afficher un échantillon par label si la structure est label/dossier/*.ext
# Détecter si on a des sous-dossiers numériques (0..9)
label_dirs = [d for d in DATA_FOLDER.iterdir() if d.is_dir()]
label_dirs = sorted(label_dirs, key=lambda p: p.name)
numeric_dirs = [d for d in label_dirs if d.name.isdigit()]
if numeric_dirs:
    print("\nStructure par dossiers détectée (labels) :")
    for d in numeric_dirs:
        print(" -", d.name, ":", sum(1 for _ in d.rglob('*') if _.is_file()))
    # construire images + labels comme avant
    images_arr = []
    labels_arr = []
    for d in numeric_dirs:
        label = int(d.name)
        for img_file in d.rglob('*'):
            if img_file.is_file() and img_file.suffix.lower() in IMAGE_EXTS:
                try:
                    im = Image.open(img_file).convert('L').resize((28,28))
                    images_arr.append(np.array(im))
                    labels_arr.append(label)
                except Exception as e:
                    print("Erreur lecture", img_file, e)
    images_arr = np.array(images_arr)
    labels_arr = np.array(labels_arr)
else:
    # sinon, on prend simplement les premières images détectées 
    print("\nAucune structure label/dossier numérique détectée. On charge les premières images sans label.")
    images_arr = []
    labels_arr = []
    for p in image_files:
        try:
            im = Image.open(p).convert('L').resize((28,28))
            images_arr.append(np.array(im))
            labels_arr.append(Path(p).parent.name)  
        except Exception as e:
            print("Erreur lecture", p, e)
    images_arr = np.array(images_arr)
    labels_arr = np.array(labels_arr)

print(f"\nImages chargées pour affichage : {len(images_arr)}")
print("Labels exemples :", np.unique(labels_arr)[:20])

# afficher une image par label 
from collections import OrderedDict
digits = OrderedDict()
for img, lbl in zip(images_arr, labels_arr):
    try:
        key = int(lbl)
    except Exception:
        key = str(lbl)
    if key not in digits:
        digits[key] = img
    if len(digits) >= 10:
        break

# plot 
nkeys = list(digits.keys())
cols = min(10, max(1, len(nkeys)))
rows = 1 if cols <= 10 else int(np.ceil(len(nkeys)/10))
plt.figure(figsize=(cols*1.5, 3))
i = 1
for k, img in digits.items():
    plt.subplot(1, len(nkeys), i)
    plt.imshow(img, cmap='gray')
    plt.title(str(k))
    plt.axis('off')
    i += 1
plt.tight_layout()
plt.show()

print("\nDEBUG END")
