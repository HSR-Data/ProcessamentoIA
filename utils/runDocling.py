#%%
import os
import glob
from docling.document_converter import DocumentConverter

# Setup paths
pdf_dir = "dados/questionarios"
output_dir = "dados/questionarios/md"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Get all PDF files in the questionarios directory
pdf_files = glob.glob(os.path.join(pdf_dir, "*.pdf"))

# Initialize converter
converter = DocumentConverter()

# Process each PDF file
processed_count = 0
error_count = 0

for pdf_file in pdf_files:
    try:
        print(f"Processing: {pdf_file}")
        
        # Convert PDF to markdown
        result = converter.convert(pdf_file)
        md = result.document.export_to_markdown()
        
        # Create output filename (same name but with .md extension)
        pdf_filename = os.path.basename(pdf_file)
        md_filename = os.path.splitext(pdf_filename)[0] + ".md"
        output_path = os.path.join(output_dir, md_filename)
        
        # Write markdown to file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(md)
        
        print(f"OK Converted {pdf_filename} -> {md_filename}")
        print(f"  Markdown length: {len(md)} characters")
        processed_count += 1
        
    except Exception as e:
        error_count += 1
        pdf_filename = os.path.basename(pdf_file)
        print(f"ERROR processing {pdf_filename}: {str(e)}")
        print(f"  Skipping corrupted/invalid file and continuing...")
        continue

print(f"\nConversion completed!")
print(f"Successfully processed: {processed_count} files")
print(f"Errors encountered: {error_count} files")
print(f"Output files saved to: {output_dir}")
