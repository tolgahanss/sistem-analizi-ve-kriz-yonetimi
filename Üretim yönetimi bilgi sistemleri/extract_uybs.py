import fitz  # PyMuPDF
import os

pdf_dir = r"c:\Users\tolga\Desktop\sistem analizi\Üretim yönetimi bilgi sistemleri"
output_dir = os.path.join(pdf_dir, "extracted")
os.makedirs(output_dir, exist_ok=True)

pdf_files = sorted([f for f in os.listdir(pdf_dir) if f.endswith('.pdf')])

for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_dir, pdf_file)
    txt_name = pdf_file.replace('.pdf', '.txt')
    txt_path = os.path.join(output_dir, txt_name)
    
    print(f"Processing: {pdf_file}")
    try:
        doc = fitz.open(pdf_path)
        full_text = []
        for page_num, page in enumerate(doc, 1):
            text = page.get_text()
            full_text.append(f"--- SAYFA {page_num} ---\n{text}")
        doc.close()
        
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(full_text))
        print(f"  -> Saved to {txt_name} ({len(full_text)} pages)")
    except Exception as e:
        print(f"  -> ERROR: {e}")

print("\nDone!")
