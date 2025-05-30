from document_correction.document_transform import scan_document

if __name__ == "__main__":
    image_path = "document_correction/input/desk.JPG"
    output = scan_document(image_path)
