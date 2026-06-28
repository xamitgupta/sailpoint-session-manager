FROM python:3.11-slim

LABEL maintainer="Amit Gupta <apphelp.csw@gmail.com>"
LABEL description="SailPoint Session Manager - Multi-app session management and revocation"

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml README.md LICENSE /app/
COPY sailpoint_session_manager/ /app/sailpoint_session_manager/

RUN pip install --no-cache-dir -e .

RUN useradd -m -u 1000 sessionmgr && chown -R sessionmgr:sessionmgr /app
USER sessionmgr

ENTRYPOINT ["session-manager"]
CMD ["--help"]
