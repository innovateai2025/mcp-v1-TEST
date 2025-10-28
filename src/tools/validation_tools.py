from datetime import datetime
from mcp import Tool
from ..models.menu import ValidationResult


class ValidationTools:
    """Herramientas de validación de menús"""
    
    @Tool
    async def validate_executive_menu(self, date: str, time: str, residente_argentino: bool = False) -> dict:
        """
        Valida disponibilidad del menú ejecutivo.
        
        Reglas:
        - Días: Lunes a Viernes únicamente
        - Horario: 12:30 - 16:30 (almuerzo)
        - Requisito: Solo residentes argentinos
        
        Args:
            date: Fecha en formato YYYY-MM-DD
            time: Hora en formato HH:MM
            residente_argentino: Si el cliente es residente argentino
            
        Returns:
            dict con valid, message y priority_rule
        """
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            time_obj = datetime.strptime(time, "%H:%M")
            
            # Día de la semana (0=lunes, 6=domingo)
            weekday = date_obj.weekday()
            
            # Hora en minutos desde medianoche
            time_in_minutes = time_obj.hour * 60 + time_obj.minute
            start_time = 12 * 60 + 30  # 12:30
            end_time = 16 * 60 + 30    # 16:30
            
            # Validar día (lunes=0 a viernes=4)
            is_weekday = 0 <= weekday <= 4
            
            # Validar horario
            is_lunch_time = start_time <= time_in_minutes <= end_time
            
            # Validar todas las condiciones
            if not is_weekday:
                return {
                    "valid": False,
                    "message": "❌ El menú ejecutivo solo está disponible de lunes a viernes",
                    "priority_rule": "RECHAZAR_FIN_DE_SEMANA",
                    "alternativas": ["carta completa"]
                }
            
            if not is_lunch_time:
                return {
                    "valid": False,
                    "message": "❌ El menú ejecutivo solo está disponible de 12:30 a 16:30hs",
                    "priority_rule": "RECHAZAR_HORARIO",
                    "alternativas": ["carta completa"]
                }
            
            if not residente_argentino:
                return {
                    "valid": False,
                    "message": "❌ El menú ejecutivo está disponible solo para residentes argentinos",
                    "priority_rule": "RECHAZAR_NO_RESIDENTE",
                    "alternativas": ["carta completa"]
                }
            
            return {
                "valid": True,
                "message": "✅ Menú ejecutivo disponible",
                "priority_rule": "ACEPTAR"
            }
            
        except Exception as e:
            return {
                "valid": False,
                "message": f"Error al validar: {str(e)}",
                "priority_rule": "ERROR"
            }
    
    @Tool
    async def validate_manso_menu(self, date: str, time: str) -> dict:
        """
        Valida disponibilidad del menú manso con regla de prioridad.
        
        Reglas:
        - Días: Lunes a Jueves únicamente (PRIORIDAD ABSOLUTA)
        - Horarios: 12:30 - 16:30 (almuerzo) Y 20:00 - 23:30 (cena)
        - Sin restricción de residencia
        
        Args:
            date: Fecha en formato YYYY-MM-DD
            time: Hora en formato HH:MM
            
        Returns:
            dict con valid, message y priority_rule
        """
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            time_obj = datetime.strptime(time, "%H:%M")
            
            # Día de la semana (0=lunes, 6=domingo)
            weekday = date_obj.weekday()
            
            # Hora en minutos desde medianoche
            time_in_minutes = time_obj.hour * 60 + time_obj.minute
            
            # Horarios permitidos
            lunch_start = 12 * 60 + 30   # 12:30
            lunch_end = 16 * 60 + 30     # 16:30
            dinner_start = 20 * 60       # 20:00
            dinner_end = 23 * 60 + 30    # 23:30
            
            # REGLA DE PRIORIDAD ABSOLUTA: Validar día primero
            # Lunes=0, Martes=1, Miércoles=2, Jueves=3, Viernes=4, Sábado=5, Domingo=6
            
            if weekday in [0, 1, 2, 3]:  # Lunes a Jueves
                # Validar horario
                is_lunch_time = lunch_start <= time_in_minutes <= lunch_end
                is_dinner_time = dinner_start <= time_in_minutes <= dinner_end
                
                if is_lunch_time or is_dinner_time:
                    return {
                        "valid": True,
                        "message": "¡Perfecto! Podés disfrutar del menú manso",
                        "priority_rule": "ACEPTAR_SIEMPRE"
                    }
                else:
                    return {
                        "valid": False,
                        "message": "❌ El menú manso está disponible de 12:30 a 16:30hs y de 20:00 a 23:30hs",
                        "priority_rule": "RECHAZAR_HORARIO",
                        "alternativas": ["carta completa"]
                    }
            else:  # Viernes a Domingo
                return {
                    "valid": False,
                    "message": "Lamento informarte que el menú manso solo está disponible de lunes a jueves",
                    "priority_rule": "RECHAZAR_SIEMPRE",
                    "alternativas": ["carta completa"]
                }
                
        except Exception as e:
            return {
                "valid": False,
                "message": f"Error al validar: {str(e)}",
                "priority_rule": "ERROR"
            }

