from mcp import Tool
from typing import Optional
from datetime import datetime
from ..models.reservation import ReservationData, ReservationResponse
from .validation_tools import ValidationTools


class ReservationTools:
    """Herramientas para gestión de reservas"""
    
    def __init__(self):
        self.validation_tools = ValidationTools()
    
    @Tool
    async def create_reservation(self, reservation_data: dict) -> dict:
        """
        Crea una nueva reserva con validación completa.
        
        Args:
            reservation_data: Diccionario con datos de reserva
            
        Returns:
            Respuesta con éxito o error
        """
        try:
            # Validar datos obligatorios
            required_fields = ["nombre", "telefono", "email", "personas", "fecha", "hora"]
            missing_fields = [field for field in required_fields if not reservation_data.get(field)]
            
            if missing_fields:
                return {
                    "success": False,
                    "message": f"Faltan campos obligatorios: {', '.join(missing_fields)}",
                    "errors": missing_fields
                }
            
            # Validar menú si se especifica
            if reservation_data.get("tipo_menu"):
                tipo_menu = reservation_data["tipo_menu"].lower()
                
                if "ejecutivo" in tipo_menu:
                    # Verificar que se haya proporcionado el dato de residencia
                    if reservation_data.get("residente_argentino") is None:
                        return {
                            "success": False,
                            "message": "Para el menú ejecutivo es obligatorio indicar si es residente argentino"
                        }
                    
                    validation = await self.validation_tools.validate_executive_menu(
                        reservation_data["fecha"],
                        reservation_data["hora"],
                        reservation_data.get("residente_argentino", False)
                    )
                    
                elif "manso" in tipo_menu:
                    validation = await self.validation_tools.validate_manso_menu(
                        reservation_data["fecha"],
                        reservation_data["hora"]
                    )
                    
                else:
                    # Menú regular o carta completa
                    validation = {"valid": True, "message": "Menú regular disponible"}
                
                # Si la validación falla, retornar el error
                if not validation["valid"]:
                    return {
                        "success": False,
                        "message": validation["message"],
                        "alternativas": validation.get("alternativas", [])
                    }
            
            # Guardar reserva
            result = await self.save_reservation(reservation_data)
            
            return {
                "success": True,
                "message": "✅ Reserva confirmada exitosamente",
                "reservation_id": result.get("id"),
                "details": {
                    "nombre": reservation_data["nombre"],
                    "fecha": reservation_data["fecha"],
                    "hora": reservation_data["hora"],
                    "personas": reservation_data["personas"],
                    "tipo_menu": reservation_data.get("tipo_menu", "carta completa")
                }
            }
            
        except Exception as e:
            return {
                "success": False,
                "message": f"Error al crear reserva: {str(e)}"
            }
    
    async def save_reservation(self, data: dict) -> dict:
        """
        Guarda la reserva en la base de datos.
        
        Args:
            data: Datos de la reserva
            
        Returns:
            Diccionario con ID de reserva
        """
        try:
            # Generar ID único para la reserva
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            reservation_id = f"RES_{timestamp}_{hash(str(data)) % 10000:04d}"
            
            # Aquí se implementaría la lógica para guardar en base de datos
            # Por ahora, retornamos el ID generado
            
            reservation_record = {
                "id": reservation_id,
                "nombre": data["nombre"],
                "telefono": data["telefono"],
                "email": data["email"],
                "personas": data["personas"],
                "fecha": data["fecha"],
                "hora": data["hora"],
                "tipo_menu": data.get("tipo_menu"),
                "preferencias": data.get("preferencias"),
                "residente_argentino": data.get("residente_argentino"),
                "created_at": datetime.now().isoformat(),
                "status": "confirmada"
            }
            
            # TODO: Guardar en base de datos (Google Sheets, PostgreSQL, etc.)
            # await self.database.save(reservation_record)
            
            return {"id": reservation_id, "record": reservation_record}
            
        except Exception as e:
            raise Exception(f"Error al guardar reserva: {str(e)}")
    
    @Tool
    async def check_availability(self, fecha: str, hora: str) -> dict:
        """
        Verifica disponibilidad para una fecha y hora específica.
        
        Args:
            fecha: Fecha en formato YYYY-MM-DD
            hora: Hora en formato HH:MM
            
        Returns:
            Disponibilidad
        """
        try:
            # TODO: Implementar verificación real de disponibilidad
            # Por ahora, asumimos disponibilidad
            return {
                "available": True,
                "fecha": fecha,
                "hora": hora,
                "message": "Disponibilidad confirmada"
            }
            
        except Exception as e:
            return {
                "available": False,
                "message": f"Error al verificar disponibilidad: {str(e)}"
            }

