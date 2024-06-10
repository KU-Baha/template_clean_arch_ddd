import logging
import sys

from infrastructure.rest.app import create_app as create_rest_app

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("app.log")
    ]
)
logger = logging.getLogger(__name__)

app = create_rest_app()
