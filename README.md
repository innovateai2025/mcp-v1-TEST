# Servidor MCP - La Cabrera Mendoza

Servidor MCP (Model Context Protocol) para La Cabrera Mendoza que integra herramientas de validación de menús, gestión de reservas, información del restaurante y administración.

## 📁 Estructura del Proyecto

```
MCP-V1/
├── src/
│   ├── tools/              # Herramientas MCP
│   │   ├── info_tools.py           # Información del restaurante
│   │   ├── reservation_tools.py    # Gestión de reservas
│   │   ├── validation_tools.py     # Validación de menús
│   │   └── admin_tools.py          # Herramientas administrativas
│   ├── models/             # Modelos de datos
│   │   ├── reservation.py          # Modelos de reserva
│   │   ├── menu.py                 # Modelos de menú
│   │   └── customer.py             # Modelos de cliente
│   ├── services/           # Servicios
│   │   ├── google_sheets.py        # Integración Google Sheets
│   │   ├── calendar_service.py     # Gestión de calendario
│   │   └── memory_service.py       # Gestión de memoria
│   └── config/             # Configuración
│       └── settings.py             # Configuración global
├── main.py                 # Servidor principal
├── requirements.txt        # Dependencias Python
├── Dockerfile             # Imagen Docker
├── docker-compose.yml     # Orquestación Docker
└── .env.example           # Ejemplo de variables de entorno
```

## 🚀 Inicio Rápido

### 1. Configurar Variables de Entorno

```bash
cp .env.example .env
# Editar .env con tus credenciales
```

### 2. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar Localmente

```bash
python main.py
```

### 4. Ejecutar con Docker

```bash
docker-compose up -d
```

## 🛠️ Herramientas Disponibles

### Herramientas de Información
- `get_restaurant_info`: Información general del restaurante
- `get_menu_prices`: Precios dinámicos actualizados
- `get_business_hours`: Horarios de atención
- `get_menu_details`: Detalles del menú completo

### Herramientas de Validación
- `validate_executive_menu`: Valida menú ejecutivo (lunes-viernes, 12:30-16:30, residentes argentinos)
- `validate_manso_menu`: Valida menú manso (lunes-jueves, almuerzo y cena)

### Herramientas de Reserva
- `create_reservation`: Crea reserva con validación completa
- `check_availability`: Verifica disponibilidad

### Herramientas Administrativas
- `escalate_to_human`: Deriva consultas al equipo humano
- `mark_as_human_required`: Marca conversación para atención humana
- `send_admin_notification`: Envía notificaciones a administración

## 📋 Reglas de Negocio

### Menú Ejecutivo
- **Días**: Lunes a Viernes únicamente
- **Horario**: 12:30 - 16:30 (almuerzo)
- **Requisito**: Solo residentes argentinos
- **Precio**: Dinámico desde Google Sheets

### Menú Manso
- **Días**: Lunes a Jueves únicamente
- **Horarios**: 12:30 - 16:30 (almuerzo) Y 20:00 - 23:30 (cena)
- **Requisito**: Sin restricción de residencia
- **Precio**: Dinámico desde Google Sheets

## 🔧 Configuración

### Variables de Entorno Requeridas

- `N8N_API_URL`: URL de la API de N8N
- `GOOGLE_SHEETS_CREDENTIALS`: Ruta a credenciales de Google Sheets
- `GOOGLE_SHEETS_ID`: ID de la hoja de cálculo

### Variables Opcionales

- `DATABASE_URL`: URL de base de datos
- `SMTP_HOST`, `SMTP_USER`, `SMTP_PASSWORD`: Configuración de email
- `LOG_LEVEL`: Nivel de logging (default: INFO)

## 🐳 Despliegue en EASYPANEL

1. Crear nueva aplicación en EASYPANEL
2. Configurar desde repositorio Git
3. Agregar variables de entorno desde `.env.example`
4. Subir archivo `credentials.json` para Google Sheets
5. Desplegar

## 📝 Notas Importantes

- **NUNCA hardcodear precios**: Siempre obtener desde Google Sheets
- **Validaciones estrictas**: Las reglas de menú ejecutivo y manso no son negociables
- **Sin credenciales en código**: Todas las credenciales vía variables de entorno
- **Estructura base**: Este es el código base, configurar credenciales según entorno

## 🔗 Integración con N8N

El servidor MCP se integra con N8N para:
- Recibir consultas de clientes
- Procesar validaciones de menús
- Gestionar reservas
- Derivar consultas complejas

## 📄 Licencia

Propietario - La Cabrera Mendoza

