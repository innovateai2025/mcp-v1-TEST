FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar requirements y instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fuente
COPY . .

# Exponer puerto
EXPOSE 8080

# Variables de entorno por defecto
ENV PYTHONUNBUFFERED=1
ENV LOG_LEVEL=INFO

# Comando de inicio
CMD ["python", "main.py"]

