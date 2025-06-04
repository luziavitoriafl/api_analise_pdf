from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
from app.services.docling_service import extract_text_from_pdf
from app.services.summarizer_service import generate_continuation 
from app.core.logger import logger
from app.api.schemas import PdfAnalysisResponse


router = APIRouter()

@router.post("/upload-pdf", response_model=PdfAnalysisResponse)
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        logger.warning(f"Arquivo {file.filename} rejeitado: tipo {file.content_type} inválido.")
        raise HTTPException(status_code=400, detail="O arquivo deve ser um PDF.")

    save_dir = Path("arquivos")
    save_dir.mkdir(exist_ok=True)
    file_path = save_dir / file.filename

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    logger.info(f"Arquivo {file.filename} recebido e salvo em {file_path}")  

    try:
        texto_extraido = extract_text_from_pdf(str(file_path))
        logger.info(f"Texto extraído com sucesso do arquivo: {file.filename}")
    except Exception as e:
        logger.error(f"Erro ao extrair texto do arquivo {file.filename}: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao extrair texto do PDF.")

    try:
        continuacao = generate_continuation(texto_extraido)
        logger.info(f"Continuação gerada com sucesso para o arquivo: {file.filename}")
    except Exception as e:
        logger.error(f"Erro ao gerar continuação para {file.filename}: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao gerar continuação do texto.")

    logger.info(f"Resposta pronta para enviar para o cliente, arquivo {file.filename}")

    return PdfAnalysisResponse(
        message="Arquivo recebido com sucesso",
        texto_extraido=texto_extraido,
        continuacao=continuacao
    )
