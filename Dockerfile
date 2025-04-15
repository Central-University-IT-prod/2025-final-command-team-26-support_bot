FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PATH="/app/.venv/bin:$PATH"

# UV installation
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# UV project copy
COPY pyproject.toml .
COPY uv.lock .

RUN uv sync --frozen --group bot

COPY films_bot films_bot

CMD ["python", "-m", "films_bot.bot.main"]
