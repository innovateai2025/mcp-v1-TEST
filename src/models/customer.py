from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class CustomerInfo(BaseModel):
    """Información del cliente"""
    name: str
    phone: str
    email: Optional[EmailStr] = None
    is_resident: Optional[bool] = None


class CustomerQuery(BaseModel):
    """Consulta del cliente para derivación"""
    query: str
    customer_info: CustomerInfo
    timestamp: datetime
    conversation_id: Optional[str] = None


class AdminEscalation(BaseModel):
    """Escalamiento a administración"""
    customer_query: str
    customer_name: str
    customer_phone: str
    customer_email: Optional[str] = None
    timestamp: str
    additional_context: Optional[str] = None

