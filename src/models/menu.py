from pydantic import BaseModel
from typing import Optional


class MenuEjecutivoRestrictions(BaseModel):
    """Restricciones del Menú Ejecutivo"""
    dias_permitidos: list[str] = ["lunes", "martes", "miércoles", "jueves", "viernes"]
    hora_inicio: str = "12:30"
    hora_fin: str = "16:30"
    requiere_residente_argentino: bool = True
    descripcion: str = "Menú ejecutivo disponible lunes a viernes de 12:30 a 16:30hs para residentes argentinos"


class MenuMansoRestrictions(BaseModel):
    """Restricciones del Menú Manso"""
    dias_permitidos: list[str] = ["lunes", "martes", "miércoles", "jueves"]
    horarios_almuerzo: dict = {"inicio": "12:30", "fin": "16:30"}
    horarios_cena: dict = {"inicio": "20:00", "fin": "23:30"}
    requiere_residente_argentino: bool = False
    descripcion: str = "Menú manso disponible lunes a jueves de 12:30 a 16:30hs y de 20:00 a 23:30hs"


class MenuInfo(BaseModel):
    """Información de menú"""
    tipo: str
    nombre: str
    precio: Optional[float] = None
    descripcion: Optional[str] = None
    disponible: bool = True


class ValidationResult(BaseModel):
    """Resultado de validación de menú"""
    valid: bool
    message: str
    priority_rule: Optional[str] = None
    alternativas: Optional[list[str]] = None

