import logging
from pathlib import Path

# Criar pasta logs se não existir
Path("logs").mkdir(exist_ok=True)

# Configurar logging
logging.basicConfig(
    filename="logs/api.log",   # arquivo onde os logs serão salvos
    level=logging.INFO,        # nível mínimo de log (INFO, WARNING, ERROR, DEBUG)
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)