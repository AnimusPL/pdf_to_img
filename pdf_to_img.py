import os
import fitz  # PyMuPDF

# Tworzenie podfolderu "images"
output_folder = "images"
os.makedirs(output_folder, exist_ok=True)

# Funkcja do zapisywania stron jako obrazów
def save_pages_as_images(pdf_path, output_folder):
    try:
        # Tworzenie osobnego folderu dla każdego pliku PDF
        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
        pdf_output_folder = os.path.join(output_folder, pdf_name)
        os.makedirs(pdf_output_folder, exist_ok=True)

        document = fitz.open(pdf_path)
        for page_number in range(len(document)):
            page = document.load_page(page_number)
            pix = page.get_pixmap()
            
            # Tworzenie nazwy pliku
            image_filename = f"page_{page_number + 1:03d}.png"
            image_path = os.path.join(pdf_output_folder, image_filename)
            
            # Zapisywanie obrazu
            pix.save(image_path)
            print(f"Zapisano stronę jako obraz: {image_filename} w folderze {pdf_name}")
    except Exception as e:
        print(f"Błąd przy przetwarzaniu pliku PDF: {pdf_path}, {e}")

# Przeglądanie folderu i przetwarzanie plików PDF
for filename in os.listdir():
    if filename.lower().endswith(".pdf"):
        print(f"Przetwarzanie pliku: {filename}")
        save_pages_as_images(filename, output_folder)

print(f"Zakończono. Strony zapisano jako obrazy w folderze: {output_folder}")
