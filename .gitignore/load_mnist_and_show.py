import matplotlib.pyplot as plt
from pathlib import Path
from mnist_loader import load_idx_images, load_idx_labels

root = Path(".")  # dossier courant

train_images = load_idx_images(root / "train-images.idx3-ubyte")
train_labels = load_idx_labels(root / "train-labels.idx1-ubyte")

print("Train images:", train_images.shape)
print("Train labels:", train_labels.shape)

# afficher quelques images
for i in range(10):
    plt.subplot(2,5,i+1)
    plt.imshow(train_images[i], cmap="gray")
    plt.title(str(train_labels[i]))
    plt.axis("off")

plt.tight_layout()
plt.show()
