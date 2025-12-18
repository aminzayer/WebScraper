from PyPDF2 import PdfFileReader

# Single Responsibility Principle (SRP):
# This class follows SRP by handling only the responsibilities related to reading text from PDF files.


class PdfReader:
    def read_text(self, file_path: str) -> str:
        """Reads text content from a PDF file."""
        try:
            with open(file_path, 'rb') as f:
                pdf_reader = PdfFileReader(f)
                # Optimization: Use list accumulation and join for O(n) performance
                # instead of string concatenation which is O(n^2)
                pages = []
                for page_num in range(pdf_reader.numPages):
                    pages.append(pdf_reader.getPage(page_num).extractText())
                return "".join(pages)
        except Exception as e:
            return f"Error reading PDF file {file_path}: {e}"
