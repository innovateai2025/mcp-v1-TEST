from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime


class ReservationData(BaseModel):
    """Modelo para datos de reserva"""
    nombre: str = Field(..., description="Nombre completo del cliente")
    telefono: str = Field(..., description="Número de WhatsApp del cliente")
    email: EmailStr = Field(..., description="Correo electrónico del cliente")
    personas: int = Field(..., ge=1, le=20, description="Cantidad de personas (1-20)")
    fecha: str = Field(..., description="Fecha de la reserva (formato: YYYY-MM-DD)")
    hora: str = Field(..., description="Hora de la reserva (formato: HH:MM)")
    tipo_menu: Optional[str] = Field(None, description="Tipo de menú: ejecutivo, manso o carta")
    preferencias: Optional[str] = Field(None, description="Preferencias alimentarias o de ubicación")
    residente_argentino: Optional[bool] = Field(None, description="Si es residente argentino (requerido para menú ejecutivo)")


class ReservationResponse(BaseModel):
    """Modelo para respuesta de creación de reserva"""
    success: bool
    message: str
    reservation_id: Optional[str] = None
    errors: Optional[list[str]] = None


class ReservationRecord(BaseModel):
    """Modelo para registro completo de reserva en base de datos"""
    id: str
    nombre: str
    telefono: str
    email: str
    personas: int
    fecha: str
    hora: str
    tipo_menu: Optional[str] = None
    preferencias: Optional[str] = None
    residente_argentino: Optional[bool] = None
    created_at: datetime
    status: str = "confirmada"

