from PyPDF2 import PdfFileReader

# Single Responsibility Principle (SRP):
# This class follows SRP by handling only the responsibilities related to reading text from PDF files.


class PdfReader:
    def read_text(self, file_path: str) -> str:
        """Reads text content from a PDF file."""
        try:
            with open(file_path, 'rb') as f:
                pdf_reader = PdfFileReader(f)
                text = ""
                for page_num in range(pdf_reader.numPages):
                    text += pdf_reader.getPage(page_num).extractText()
                return text
        except Exception as e:
            return f"Error reading PDF file {file_path}: {e}"
