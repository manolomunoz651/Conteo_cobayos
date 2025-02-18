import cv2
from ultralytics import YOLO

modelo = YOLO("best_detec_cuyes.pt")

#cap = cv2.VideoCapture('video_cuyes.mp4')  # índice 1 para la cámara externa
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("No se pudo abrir la cámara externa.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Realiza la predicción frame a frame
    results = modelo.predict(frame, conf=0.2)  # Devuelve una lista de resultados

    # Para cada resultado, YOLO puede dibujar directamente los bounding boxes
    # en la imagen si lo indicas en la función 'plot()'
    annotada = results[0].plot()  # Devuelve el frame con las anotaciones dibujadas

    num_cuyes = len(results[0])

    num_cuyes_text = f"Numero de cuyes: {num_cuyes}"
    cv2.putText(
        annotada,
        num_cuyes_text,
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2,
        cv2.LINE_AA
    )

    cv2.imshow("Detección de cuyes", annotada)
    ancho = int(cap.get(3))
    alto = int(cap.get(4))

    #print(ancho, alto)

    # cv2.VideoWriter(Nombre, Codificacion, FPS, Tamaño)

    cv2.VideoWriter('Video.mp4v', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (ancho, alto))
    t = cv2.waitKey(1)
    if t == 27:
        break

cap.release()
cv2.destroyAllWindows()