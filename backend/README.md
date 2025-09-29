### コマンド
- テスト実行コマンド
  - uv run pytest -q
- バックエンドスタートコマンド
  - uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
- container start
  - docker compose up -d
- データベース更新コマンド
  - uv run alembic revision --autogenerate -m "message"
  - uv run alembic upgrade head