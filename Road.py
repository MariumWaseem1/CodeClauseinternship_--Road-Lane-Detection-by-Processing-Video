import cv2
import numpy as np

def region_of_interest(image, vertices):
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, vertices, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def draw_lines(image, lines, color=(0, 255, 0), thickness=5):
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(image, (x1, y1), (x2, y2), color, thickness)

def pipeline(image):
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

   
    edges = cv2.Canny(blurred, 50, 150)

    
    height, width = image.shape[:2]
    vertices = np.array([[(0, height), (width / 2, height / 2), (width, height)]], dtype=np.int32)
    roi = region_of_interest(edges, vertices)

   
    lines = cv2.HoughLinesP(roi, 2, np.pi / 180, 100, np.array([]), minLineLength=40, maxLineGap=5)

   
    line_image = np.zeros_like(image)

    
    draw_lines(line_image, lines)

   
    result = cv2.addWeighted(image, 0.8, line_image, 1, 0)

    return result

video_path = 'C:\\Users\\Dell 7410\\Desktop\\golden project\\WhatsApp Video 2024-03-12 at 5.46.29 PM.mp4'


cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

   
    processed_frame = pipeline(frame)

    
    cv2.imshow('Lane Detection', processed_frame)

   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()