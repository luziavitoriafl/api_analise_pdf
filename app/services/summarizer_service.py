from pathlib import Path
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import re
from datetime import datetime
from app.core.logger import logger


DIR_GERADOS = Path("arquivos_gerados")
DIR_GERADOS.mkdir(exist_ok=True)

MODEL_PATH = "./app/models/gpt2-small-portuguese"
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH)


def clean_generated_text(text: str) -> str:
    # Formata o texto removendo elementos indesejados
    text = re.sub(r"public\s+static\s+.*?;", "", text)
    text = re.sub(r"[\n\r]+", " ", text)  # remove quebras de linha
    text = re.sub(r"[{}[\]()<>]", "", text)  # remove parênteses e chaves
    text = re.sub(r"\s{2,}", " ", text)  # remove espaços duplicados
    return text.strip()

def salvar_texto_gerado(texto: str) -> Path:
    base_dir = Path("arquivos_gerados")
    hoje = datetime.now().strftime("%Y-%m-%d")
    dir_dia = base_dir / hoje
    dir_dia.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%H%M%S")
    arquivo_path = dir_dia / f"gerado_{timestamp}.txt"

    with open(arquivo_path, "w", encoding="utf-8") as f:
        f.write(texto)

    logger.info(f"Texto gerado salvo em: {arquivo_path}")
    return arquivo_path

def generate_continuation(text: str) -> str:
    try:
        logger.info("Iniciando geração de continuação para texto com %d caracteres.", len(text))  
        # Limita o texto para 800 caracteres para evitar prompts muito grandes
        text = text[:800]

        prompt = (
            "Analise cuidadosamente o texto a seguir e escreva uma continuação coerente e filosófica com o texto, com início, meio e fim, clara e natural em português do Brasil. "
            "Evite repetir frases ou palavras do texto original e mantenha o mesmo contexto e tom. "
            "Continue a narrativa de forma fluida.\n\n"
            f"Texto:\n{text}\n\nContinuação:"
        )

        inputs = tokenizer(prompt, return_tensors="pt")
        logger.debug("Prompt tokenizado com sucesso")

        outputs = model.generate(
            **inputs,
            max_new_tokens=100,
            temperature=0.8,
            top_p=0.95,
            repetition_penalty=1.2,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
        )

        logger.info("Geração de texto concluída com sucesso")

        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Extrai somente a continuação, se possível
        if "Continuação:" in generated_text:
            continuation = generated_text.split("Continuação:")[-1].strip()
        else:
            continuation = generated_text.strip()

        cleaned = clean_generated_text(continuation)

        # Usa a função de salvar texto para manter padrão e organização
        arquivo_path = salvar_texto_gerado(cleaned)

        return cleaned
    
    except Exception as e:
        logger.error("Erro ao gerar continuação: %s", str(e))
        raise e
