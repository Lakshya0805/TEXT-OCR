## OCR Text Extraction using OpenCV & Tesseract

This is a simple OCR project that extracts text from images using OpenCV for preprocessing and Tesseract for recognition. The output is printed in the console and saved to a `.txt` file.

### Features
- Grayscale conversion, resizing, noise reduction, and thresholding
- Text extraction using Tesseract (`--oem 3 --psm 3`)
- Clean, modular Python code

### How to Use
1. Set your image path in the script.
2. Run: python ocr_text_extractor.py
3. Output will be printed and saved to `extracted_text.txt`.