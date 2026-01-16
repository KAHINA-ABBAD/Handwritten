import zipfile
from pathlib import Path

zip_path = Path("archive.zip")
extract_dir = Path(".")

if not zip_path.exists():
    raise FileNotFoundError("archive.zip introuvable dans ce dossier !")

print("Extraction de archive.zip dans le dossier courant...")

with zipfile.ZipFile(zip_path, 'r') as z:
    z.extractall(extract_dir)

print("Extraction terminée !")
print("Fichiers extraits :")
for file in ["train-images.idx3-ubyte", "train-labels.idx1-ubyte",
             "t10k-images.idx3-ubyte", "t10k-labels.idx1-ubyte"]:
    print(" -", file, "✓" if Path(file).exists() else "✗")
