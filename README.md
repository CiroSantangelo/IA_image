# IA_image
Questo programma è un'applicazione Python che utilizza TensorFlow per creare e addestrare un modello di rete neurale convoluzionale (CNN) per la classificazione delle immagini utilizzando il dataset CIFAR-10. Ecco una descrizione delle sue principali funzionalità e componenti:

Caricamento del dataset CIFAR-10: Utilizza TensorFlow per caricare il dataset CIFAR-10, che contiene immagini di 10 diverse categorie di oggetti come aereo, automobile, uccello, gatto, cervo, cane, rana, cavallo, nave e camion.
Definizione e addestramento del modello CNN: Utilizza TensorFlow e Keras per definire un modello di rete neurale convoluzionale (CNN) con diversi strati convoluzionali e completamente connessi. Il modello viene quindi compilato e addestrato utilizzando il metodo fit().
Predizione delle immagini: Dopo l'addestramento del modello, il programma chiede all'utente di specificare il percorso di una directory contenente immagini da predire. Carica quindi ciascuna immagine dalla directory, le preprocessa e le sottopone a predizione utilizzando il modello addestrato. Infine, mostra l'immagine predetta insieme alla classe prevista.
Funzione load_and_preprocess_image: Una funzione ausiliaria che carica un'immagine da un percorso specificato, la ridimensiona alle dimensioni richieste (32x32 pixel) e la normalizza in modo che i valori dei pixel siano compresi tra 0 e 1.
Interpretazione delle predizioni: Le predizioni del modello vengono interpretate utilizzando un elenco di classi di oggetti possibili nel dataset CIFAR-10, e viene visualizzata la classe prevista per ciascuna immagine.
Visualizzazione delle immagini predette: Utilizzando Matplotlib, il programma mostra ciascuna immagine predetta insieme alla classe prevista.
