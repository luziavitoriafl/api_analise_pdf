from pydantic import BaseModel


class PdfAnalysisResponse(BaseModel):
    message: str
    texto_extraido: str
    continuacao: str
