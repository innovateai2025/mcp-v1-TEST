from typing import Dict, List, Optional, Any
from datetime import datetime


class MemoryService:
    """Servicio para gestión de memoria de conversaciones"""
    
    def __init__(self):
        # En producción, esto podría ser Redis, MongoDB, etc.
        self.conversations: Dict[str, List[Dict[str, Any]]] = {}
        self.customer_context: Dict[str, Dict[str, Any]] = {}
    
    async def get_conversation_history(
        self,
        conversation_id: str,
        limit: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Obtiene historial de conversación.
        
        Args:
            conversation_id: ID de la conversación
            limit: Número máximo de mensajes a retornar
            
        Returns:
            Lista de mensajes de la conversación
        """
        history = self.conversations.get(conversation_id, [])
        
        if limit:
            return history[-limit:]
        
        return history
    
    async def add_message(
        self,
        conversation_id: str,
        role: str,
        content: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> None:
        """
        Agrega un mensaje al historial de conversación.
        
        Args:
            conversation_id: ID de la conversación
            role: Rol del mensaje (user, assistant, system)
            content: Contenido del mensaje
            metadata: Metadatos adicionales
        """
        if conversation_id not in self.conversations:
            self.conversations[conversation_id] = []
        
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "metadata": metadata or {}
        }
        
        self.conversations[conversation_id].append(message)
    
    async def get_customer_context(self, customer_id: str) -> Dict[str, Any]:
        """
        Obtiene contexto del cliente (preferencias, historial, etc.).
        
        Args:
            customer_id: ID del cliente
            
        Returns:
            Contexto del cliente
        """
        return self.customer_context.get(customer_id, {})
    
    async def update_customer_context(
        self,
        customer_id: str,
        context: Dict[str, Any]
    ) -> None:
        """
        Actualiza contexto del cliente.
        
        Args:
            customer_id: ID del cliente
            context: Nuevo contexto o actualización
        """
        if customer_id not in self.customer_context:
            self.customer_context[customer_id] = {}
        
        self.customer_context[customer_id].update(context)
    
    async def check_first_interaction(self, conversation_id: str) -> bool:
        """
        Verifica si es la primera interacción en una conversación.
        
        Args:
            conversation_id: ID de la conversación
            
        Returns:
            True si es la primera interacción
        """
        history = await self.get_conversation_history(conversation_id)
        return len(history) == 0
    
    async def clear_conversation(self, conversation_id: str) -> None:
        """
        Limpia el historial de una conversación.
        
        Args:
            conversation_id: ID de la conversación
        """
        if conversation_id in self.conversations:
            del self.conversations[conversation_id]

