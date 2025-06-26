import cv2
from ultralytics import YOLO

def analisar_frames(video_path: str) -> list:
    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture(video_path)
    resultados = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        result = model.predict(frame, verbose=False)
        for r in result:
            boxes = r.boxes
            if boxes:
                resultados.append([model.names[int(cls)] for cls in boxes.cls])
    cap.release()
    return resultados
