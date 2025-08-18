from tensorflow import keras 


model = keras.models.load_model("model.keras")
model.summary()


for layer in model.layers:
    print(layer.get_weights())
