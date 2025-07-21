import cv2

def put_string(frame, text, position, value, color=(120, 200, 90)):
    string = f"{text} {value}"
    cv2.putText(frame, string, position, cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

def print_matInfo(name, image):
    print(f"{name} 정보:")
    print(f" - Shape: {image.shape}")
    print(f" - Dtype: {image.dtype}")
    print(f" - Size: {image.size}")
    print(f" - Type: {type(image)}")