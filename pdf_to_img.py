import os
import fitz  # PyMuPDF

# Tworzenie podfolderu "images"
output_folder = "images"
os.makedirs(output_folder, exist_ok=True)

# Funkcja do zapisywania obrazów z pliku PDF
def save_images_from_pdf(pdf_path, output_folder):
    try:
        # Tworzenie osobnego folderu dla każdego pliku PDF
        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
        pdf_output_folder = os.path.join(output_folder, pdf_name)
        os.makedirs(pdf_output_folder, exist_ok=True)

        document = fitz.open(pdf_path)
        image_count = 0

        for page_number in range(len(document)):
            page = document.load_page(page_number)
            
            # Wyodrębnianie obrazów z strony
            image_list = page.get_images(full=True)
            
            for img_index, img in enumerate(image_list):
                xref = img[0]  # Indeks obrazu w pliku PDF
                base_image = document.extract_image(xref)
                image_bytes = base_image["image"]  # Obraz jako bajty

                # Tworzenie nazwy pliku obrazu
                image_filename = f"image_{page_number + 1}_{img_index + 1}.png"
                image_path = os.path.join(pdf_output_folder, image_filename)

                # Zapisanie obrazu
                with open(image_path, "wb") as img_file:
                    img_file.write(image_bytes)
                image_count += 1
                print(f"Zapisano obraz: {image_filename} w folderze {pdf_name}")

        if image_count == 0:
            print("Brak obrazów w pliku PDF.")
    except Exception as e:
        print(f"Błąd przy przetwarzaniu pliku PDF: {pdf_path}, {e}")

# Przeglądanie folderu i przetwarzanie plików PDF
for filename in os.listdir():
    if filename.lower().endswith(".pdf"):
        print(f"Przetwarzanie pliku: {filename}")
        save_images_from_pdf(filename, output_folder)

print(f"Zakończono. Obrazy zapisano w folderze: {output_folder}")
