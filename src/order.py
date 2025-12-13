"""
Order representation for the order book.
"""

from dataclasses import dataclass
from typing import Literal


@dataclass
class Order:
    """
    Represents a limit order in the book.
    
    Attributes:
        id: Unique order identifier
        price: Limit price for the order
        quantity: Number of shares/contracts
        is_buy: True for buy orders, False for sell orders
        timestamp: Unix timestamp when order was created
    """
    id: int
    price: float
    quantity: int
    is_buy: bool
    timestamp: float
    
    @property
    def side(self) -> Literal["BUY", "SELL"]:
        """Human-readable side"""
        return "BUY" if self.is_buy else "SELL"
    
    def __repr__(self) -> str:
        return f"Order({self.id}, {self.side}, {self.quantity}@${self.price:.2f})"
    
    def __hash__(self) -> int:
        """Make Order hashable for use in sets/dicts"""
        return hash(self.id)
    
    def __eq__(self, other) -> bool:
        """Orders are equal if they have the same ID"""
        if not isinstance(other, Order):
            return False
        return self.id == other.id