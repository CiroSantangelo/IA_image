import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Caricamento del dataset CIFAR-10
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.cifar10.load_data()

# Normalizzazione delle immagini
train_images, test_images = train_images / 255.0, test_images / 255.0

# Definizione dell'architettura del modello
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compilazione del modello
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Addestramento del modello
model.fit(train_images, train_labels, epochs=10, batch_size=64, validation_split=0.2)

# Funzione per caricare e preprocessare un'immagine
def load_and_preprocess_image(img_path):
    try:
        img = image.load_img(img_path, target_size=(32, 32))
        img_array = image.img_to_array(img) / 255.0  # Converti l'immagine direttamente in un array numpy e normalizzalo
        img_array = np.expand_dims(img_array, axis=0)
        return img_array
    except Exception as e:
        print("Errore durante il caricamento dell'immagine:", e)
        return None

# Allenamento del modello
# (Il codice di addestramento del modello va qui)

# Percorso della directory contenente le immagini da predire
images_directory = input("Inserisci il percorso della directory contenente le immagini da predire: ")

# Verifica se il percorso della directory esiste
if not os.path.exists(images_directory):
    print("Il percorso specificato non esiste.")
else:
    # Elenco dei file nella directory
    image_files = [os.path.join(images_directory, f) for f in os.listdir(images_directory) if f.endswith('.jpg')]

    # Predizione sulle immagini
    for img_path in image_files:
        # Caricamento e preprocessamento dell'immagine
        img_array = load_and_preprocess_image(img_path)

        # Se l'immagine è stata caricata con successo, effettua le predizioni e visualizza
        if img_array is not None:
            # Effettua le predizioni sull'immagine
            predictions = model.predict(img_array)

            # Interpretazione delle predizioni
            predicted_class = np.argmax(predictions)
            class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
            predicted_label = class_names[predicted_class]
            print("Classe predetta per l'immagine", img_path, ":", predicted_label)

            # Mostra l'immagine predetta
            plt.imshow(image.load_img(img_path))
            plt.axis('off')
            plt.title(predicted_label)
            plt.show()
