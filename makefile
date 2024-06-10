# Makefile для проекта на FastAPI с использованием Poetry

# Название проекта
PROJECT_NAME := my_fastapi_project

# Параметры для запуска uvicorn
UVICORN_HOST := 127.0.0.1
UVICORN_PORT := 8000
UVICORN_MODULE := main:app

# Команды для установки и активации виртуального окружения
.PHONY: install
install:
	poetry install

.PHONY: run
run:
	cd src && poetry run uvicorn $(UVICORN_MODULE) --host $(UVICORN_HOST) --port $(UVICORN_PORT) --reload

.PHONY: test
test:
	cd src && poetry run pytest tests

.PHONY: lint
lint:
	poetry run pre-commit

.PHONY: clean
clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .coverage
	rm -rf htmlcov

.PHONY: help
help:
	@echo "Использование: make [цель]"
	@echo ""
	@echo "Цели:"
	@echo "  install    - Установить зависимости с использованием Poetry"
	@echo "  run        - Запустить сервер разработки"
	@echo "  test       - Запустить тесты"
	@echo "  lint       - Запустить линтеры"
	@echo "  clean      - Очистить проект от временных файлов"
	@echo "  help       - Показать это сообщение"

.DEFAULT_GOAL := help
