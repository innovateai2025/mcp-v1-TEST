from mcp import Tool
from typing import Optional
from ..services.google_sheets import GoogleSheetsService


class RestaurantInfoTools:
    """Herramientas para obtener información del restaurante"""
    
    def __init__(self):
        self.sheets_service = GoogleSheetsService()
    
    @Tool
    async def get_restaurant_info(self, category: str = "general") -> str:
        """
        Obtiene información actualizada del restaurante desde Google Sheets.
        
        Args:
            category: Categoría de información (general, ubicacion, horarios, etc.)
            
        Returns:
            Información del restaurante
        """
        try:
            info = await self.sheets_service.get_business_info()
            
            if category in info:
                return info[category]
            
            # Si no se encuentra la categoría específica, devolver info general
            if "general" in info:
                return info["general"]
                
            return "Información no disponible. Por favor, consulte con administración."
            
        except Exception as e:
            return f"Error al obtener información: {str(e)}. Por favor, consulte con administración."
    
    @Tool
    async def get_menu_prices(self, menu_type: str) -> dict:
        """
        Obtiene precios actualizados de menús desde Google Sheets.
        NUNCA hardcodear precios - siempre consultar fuente dinámica.
        
        Args:
            menu_type: Tipo de menú (ejecutivo, manso, carta)
            
        Returns:
            Diccionario con información de precios
        """
        try:
            prices = await self.sheets_service.get_menu_prices()
            
            menu_type_lower = menu_type.lower()
            
            if menu_type_lower in prices:
                return prices[menu_type_lower]
            
            # Buscar por nombre similar
            for key in prices.keys():
                if menu_type_lower in key or key in menu_type_lower:
                    return prices[key]
            
            return {
                "error": f"Precio no encontrado para {menu_type}",
                "message": "Consultar con administración para información de precios"
            }
            
        except Exception as e:
            return {
                "error": str(e),
                "message": "Error al obtener precios. Consultar con administración."
            }
    
    @Tool
    async def get_business_hours(self) -> dict:
        """
        Obtiene horarios de atención actualizados desde Google Sheets.
        
        Returns:
            Diccionario con horarios de atención
        """
        try:
            hours = await self.sheets_service.get_business_hours()
            return hours
            
        except Exception as e:
            return {
                "error": str(e),
                "message": "Error al obtener horarios. Consultar con administración."
            }
    
    @Tool
    async def get_menu_details(self, menu_section: Optional[str] = None) -> dict:
        """
        Obtiene detalles del menú completo o de una sección específica.
        
        Args:
            menu_section: Sección del menú (entradas, principales, postres, bebidas)
            
        Returns:
            Detalles del menú
        """
        try:
            menu = await self.sheets_service.get_menu_details()
            
            if menu_section and menu_section in menu:
                return {menu_section: menu[menu_section]}
            
            return menu
            
        except Exception as e:
            return {
                "error": str(e),
                "message": "Error al obtener detalles del menú. Consultar con administración."
            }

