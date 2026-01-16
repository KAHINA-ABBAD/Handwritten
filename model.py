from tensorflow.keras.models import load_model

def load_model_cnn():
    return load_model("cnn_mnist_final.h5")
