import asyncio
from mcp import MCPServer
from src.tools.info_tools import RestaurantInfoTools
from src.tools.validation_tools import ValidationTools
from src.tools.reservation_tools import ReservationTools
from src.tools.admin_tools import AdminTools
from src.config.settings import settings


class LaCabreraMCPServer:
    """Servidor MCP para La Cabrera Mendoza"""
    
    def __init__(self):
        self.server = MCPServer(settings.server_name)
        self.setup_tools()
    
    def setup_tools(self):
        """Registra todas las herramientas del servidor MCP"""
        
        # Instanciar herramientas
        info_tools = RestaurantInfoTools()
        validation_tools = ValidationTools()
        reservation_tools = ReservationTools()
        admin_tools = AdminTools()
        
        # Registrar herramientas de información
        self.server.add_tool(info_tools.get_restaurant_info)
        self.server.add_tool(info_tools.get_menu_prices)
        self.server.add_tool(info_tools.get_business_hours)
        self.server.add_tool(info_tools.get_menu_details)
        
        # Registrar herramientas de validación
        self.server.add_tool(validation_tools.validate_executive_menu)
        self.server.add_tool(validation_tools.validate_manso_menu)
        
        # Registrar herramientas de reserva
        self.server.add_tool(reservation_tools.create_reservation)
        self.server.add_tool(reservation_tools.check_availability)
        
        # Registrar herramientas administrativas
        self.server.add_tool(admin_tools.escalate_to_human)
        self.server.add_tool(admin_tools.mark_as_human_required)
        self.server.add_tool(admin_tools.send_admin_notification)
        
        print(f"✅ Servidor MCP '{settings.server_name}' configurado con todas las herramientas")
    
    async def run(self):
        """Inicia el servidor MCP"""
        print(f"🚀 Iniciando servidor MCP en {settings.server_host}:{settings.server_port}")
        print(f"📋 Herramientas disponibles:")
        print("   - Información del restaurante (info, precios, horarios, menú)")
        print("   - Validación de menús (ejecutivo, manso)")
        print("   - Gestión de reservas (crear, verificar disponibilidad)")
        print("   - Administración (derivar a humano, notificaciones)")
        
        await self.server.run()


def main():
    """Punto de entrada principal"""
    server = LaCabreraMCPServer()
    asyncio.run(server.run())


if __name__ == "__main__":
    main()

