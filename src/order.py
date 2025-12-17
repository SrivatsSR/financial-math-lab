"""
Order representation for the order book.
"""

from dataclasses import dataclass
from typing import Literal, Optional


@dataclass
class Order:
    """
    Represents an order in the book.
    
    Attributes:
        id: Unique order identifier
        quantity: Number of shares/contracts
        is_buy: True for buy orders, False for sell orders
        timestamp: Unix timestamp when order was created
        price: Limit price (None for market orders)
        order_type: 'limit' or 'market'
    """
    id: int
    quantity: int
    is_buy: bool
    timestamp: float
    price: Optional[float] = None
    order_type: Literal["limit", "market"] = "limit"
    
    def __post_init__(self):
        """Validate order after initialization"""
        if self.order_type == "limit" and self.price is None:
            raise ValueError("Limit orders must have a price")
        if self.order_type == "market" and self.price is not None:
            raise ValueError("Market orders should not have a price")
    
    @property
    def side(self) -> Literal["BUY", "SELL"]:
        """Human-readable side"""
        return "BUY" if self.is_buy else "SELL"
    
    @property
    def is_market_order(self) -> bool:
        """Check if this is a market order"""
        return self.order_type == "market"
    
    def __repr__(self) -> str:
        if self.is_market_order:
            return f"Order({self.id}, {self.side} MARKET, {self.quantity} shares)"
        else:
            return f"Order({self.id}, {self.side}, {self.quantity}@${self.price:.2f})"
    
    def __hash__(self) -> int:
        """Make Order hashable for use in sets/dicts"""
        return hash(self.id)
    
    def __eq__(self, other) -> bool:
        """Orders are equal if they have the same ID"""
        if not isinstance(other, Order):
            return False
        return self.id == other.id