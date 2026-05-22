import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def detect_box():

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.resize(frame, (640, 480))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        edges = cv2.Canny(blur, 50, 150)

        contours, _ = cv2.findContours(
            edges,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        for cnt in contours:

            area = cv2.contourArea(cnt)

            if area > 2500:

                x, y, w, h = cv2.boundingRect(cnt)

                aspect_ratio = float(w) / h

                if 0.8 < aspect_ratio < 1.2:

                    cv2.rectangle(
                        frame,
                        (x, y),
                        (x+w, y+h),
                        (0, 255, 0),
                        2
                    )

                    cx = x + w // 2
                    cy = y + h // 2

                    cv2.circle(
                        frame,
                        (cx, cy),
                        5,
                        (0, 0, 255),
                        -1
                    )

                    cv2.putText(
                        frame,
                        "BOX DETECTED",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0,255,0),
                        2
                    )

                    cv2.imshow("Detection", frame)

                    return cx, cy

        cv2.imshow("Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
