FROM python:3.11-slim

WORKDIR /app

COPY . .

# Instalar cron, pg_dump y dependencias
RUN apt-get update && \
    apt-get install -y cron postgresql-client && \
    pip install --no-cache-dir requests psycopg[binary] && \
    rm -rf /var/lib/apt/lists/*

# Copiar archivo de cron al contenedor
COPY backend_cronjob /etc/cron.d/backend_cronjob

# Dar permisos y registrar el cronjob
RUN chmod 0644 /etc/cron.d/backend_cronjob && \
    crontab /etc/cron.d/backend_cronjob

# Ejecutar cron en primer plano
CMD ["sh", "-c", "python actualizar_datos.py && cron -f"]