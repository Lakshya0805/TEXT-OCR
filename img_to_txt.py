import cv2 as cv
import pytesseract

#defining preprocessing
def preprocess(image_path):
    img = cv.imread(image_path)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    resized = cv.resize(gray, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
    blurred = cv.GaussianBlur(resized, (5, 5), 0)
    threshold, thresh = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    return thresh

#defining text extraction
def extract_text(processed_image):
    config = '--oem 3 --psm 3'
    return pytesseract.image_to_string(processed_image, config=config).strip()


#Text Extraction
image_path = r"E:\Full Data Science Stack\Complete Python\opencv\txt images\download (2).jpeg"
processed = preprocess(image_path)
text = extract_text(processed)

#Storing/Printing the output
print("Extracted Text:\n")
print(text)
with open('extracted_text.txt', 'w') as f:
    f.write(text)

print("\nText saved to 'extracted_text.txt'")
