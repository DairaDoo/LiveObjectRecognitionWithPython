import numpy as np
import cv2

# definimos las rutas principales
image_path = "imgs/sala_de_casa1.jpg"
prototxt_path = "models/MobileNetSSD_deploy.prototxt"
model_path = "models/mobilenet_iter_73000.caffemodelz"

# añadimos confianza mínima de 20%
min_confidence = 0.2

classes = ["background", "aeroplane", "bicycle", "bird", "boat",
"bottle", "bus", "car", "cat", "chair", "cow", "diningtable"
"dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

np.random.seed(543210)
colors = np.random.uniform(0, 255, size=(len(classes), 3))