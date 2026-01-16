from flask import Flask, render_template, request
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

model = load_model("cnn_mnist_final.h5")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    probabilities = None

    if request.method == "POST":
        file = request.files["file"]

        path = "static/upload.png"
        file.save(path)

        img = image.load_img(path, color_mode="grayscale", target_size=(28, 28))
        img = image.img_to_array(img)
        img = img / 255.0
        img = img.reshape(1, 28, 28, 1)

        preds = model.predict(img)
        prediction = int(np.argmax(preds))
        probabilities = preds[0]

    return render_template(
        "index.html",
        prediction=prediction,
        probabilities=probabilities
    )

if __name__ == "__main__":
    app.run(debug=True)
