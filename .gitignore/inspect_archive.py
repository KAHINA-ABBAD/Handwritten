import zipfile
from pathlib import Path
from collections import Counter

zip_path = Path("archive.zip")
if not zip_path.exists():
    print("archive.zip introuvable.")
    raise SystemExit(1)

with zipfile.ZipFile(zip_path, "r") as z:
    names = z.namelist()

print(f"Nombre d'entrées dans archive.zip : {len(names)}\n")

# regrouper par extension et afficher exemples
exts = [Path(n).suffix.lower() for n in names]
cnt = Counter(exts)
for ext, c in cnt.most_common():
    print(f"{ext or '[noext]'} : {c}")

print("\n--- 20 premières entrées ---")
for n in names[:20]:
    print(n)

# lister seulement images / csv / npz
image_exts = {'.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif'}
images = [n for n in names if Path(n).suffix.lower() in image_exts]
csvs = [n for n in names if Path(n).suffix.lower() == '.csv']
npzs = [n for n in names if Path(n).suffix.lower() == '.npz']

print(f"\nImages trouvées dans ZIP : {len(images)} (exemples : {images[:10]})")
print(f"CSV trouvés : {len(csvs)} (exemples : {csvs[:10]})")
print(f"NPZ trouvés : {len(npzs)} (exemples : {npzs[:10]})")
import zipfile
from pathlib import Path
from collections import Counter

zip_path = Path("archive.zip")
if not zip_path.exists():
    print("archive.zip introuvable.")
    raise SystemExit(1)

with zipfile.ZipFile(zip_path, "r") as z:
    names = z.namelist()

print(f"Nombre d'entrées dans archive.zip : {len(names)}\n")

# regrouper par extension et afficher exemples
exts = [Path(n).suffix.lower() for n in names]
cnt = Counter(exts)
for ext, c in cnt.most_common():
    print(f"{ext or '[noext]'} : {c}")

print("\n--- 20 premières entrées ---")
for n in names[:20]:
    print(n)

# lister seulement images / csv / npz
image_exts = {'.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif'}
images = [n for n in names if Path(n).suffix.lower() in image_exts]
csvs = [n for n in names if Path(n).suffix.lower() == '.csv']
npzs = [n for n in names if Path(n).suffix.lower() == '.npz']

print(f"\nImages trouvées dans ZIP : {len(images)} (exemples : {images[:10]})")
print(f"CSV trouvés : {len(csvs)} (exemples : {csvs[:10]})")
print(f"NPZ trouvés : {len(npzs)} (exemples : {npzs[:10]})")
