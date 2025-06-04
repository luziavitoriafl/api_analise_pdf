from docling.document_converter import DocumentConverter
from app.core.logger import logger  


def extract_text_from_pdf(file_path: str) -> str:
    try:
        logger.info(f"Iniciando extração de texto do PDF: {file_path}")

        converter = DocumentConverter()
        result = converter.convert(file_path)

        markdown_text = result.document.export_to_markdown()
        logger.info(f"Texto extraído com sucesso do PDF: {file_path}")

        return markdown_text
    


    except Exception as e:
        logger.error(f"Erro ao extrair texto do PDF {file_path}: {str(e)}")
        raise RuntimeError(f"Erro na extração do PDF") from e