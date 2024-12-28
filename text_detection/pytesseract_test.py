import cv2
import pytesseract

image_path = "data.jpg"
img = cv2.imread(image_path)

# 이미지 전처리
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # 이진화

# 텍스트 인식
custom_config = r'--oem 3 --psm 6' # OCR 엔진 모드와 페이지 분할 모드 설정
text = pytesseract.image_to_string(binary, config=custom_config, lang='eng')

# 텍스트 바운딩 박스 추출
h, w, _ = img.shape
boxes = pytesseract.image_to_boxes(binary)

for b in boxes.splitlines():
    b = b.split()
    x, y, x2, y2 = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, h-y), (x2, h-y2), (0, 255, 0), 2)

cv2.imwrite("result.jpg", img)

print("인식된 텍스트:")
print(text)