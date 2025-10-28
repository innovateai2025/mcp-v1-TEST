import os
from typing import Optional
from pydantic import BaseModel


class Settings(BaseModel):
    """Configuración del servidor MCP"""
    
    # Configuración del servidor
    server_name: str = "la-cabrera-mcp"
    server_host: str = "0.0.0.0"
    server_port: int = 8080
    
    # Configuración de Google Sheets
    google_sheets_credentials: Optional[str] = None
    google_sheets_id: Optional[str] = None
    
    # Configuración de N8N
    n8n_api_url: Optional[str] = None
    n8n_api_key: Optional[str] = None
    
    # Configuración de base de datos
    database_url: Optional[str] = None
    
    # Configuración de email
    smtp_host: Optional[str] = None
    smtp_port: int = 587
    smtp_user: Optional[str] = None
    smtp_password: Optional[str] = None
    admin_email: Optional[str] = None
    
    # Configuración de logging
    log_level: str = "INFO"
    
    # Horarios de negocio (configurables)
    business_hours: dict = {
        "menu_ejecutivo": {
            "dias": ["lunes", "martes", "miércoles", "jueves", "viernes"],
            "hora_inicio": "12:30",
            "hora_fin": "16:30"
        },
        "menu_manso": {
            "dias": ["lunes", "martes", "miércoles", "jueves"],
            "horarios": {
                "almuerzo": {"inicio": "12:30", "fin": "16:30"},
                "cena": {"inicio": "20:00", "fin": "23:30"}
            }
        }
    }
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def load_settings() -> Settings:
    """
    Carga configuración desde variables de entorno.
    
    Returns:
        Instancia de Settings con configuración cargada
    """
    return Settings(
        # Cargar desde variables de entorno
        google_sheets_credentials=os.getenv("GOOGLE_SHEETS_CREDENTIALS"),
        google_sheets_id=os.getenv("GOOGLE_SHEETS_ID"),
        n8n_api_url=os.getenv("N8N_API_URL"),
        n8n_api_key=os.getenv("N8N_API_KEY"),
        database_url=os.getenv("DATABASE_URL"),
        smtp_host=os.getenv("SMTP_HOST"),
        smtp_port=int(os.getenv("SMTP_PORT", "587")),
        smtp_user=os.getenv("SMTP_USER"),
        smtp_password=os.getenv("SMTP_PASSWORD"),
        admin_email=os.getenv("ADMIN_EMAIL"),
        log_level=os.getenv("LOG_LEVEL", "INFO")
    )


# Instancia global de configuración
settings = load_settings()

