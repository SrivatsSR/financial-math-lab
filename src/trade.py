"""
Trade representation for executed orders.
"""

from dataclasses import dataclass


@dataclass
class Trade:
    """
    Represents an executed trade between two orders.
    
    Attributes:
        buy_order_id: ID of the buy order
        sell_order_id: ID of the sell order
        price: Execution price
        quantity: Number of shares traded
        timestamp: Unix timestamp of execution
    """
    buy_order_id: int
    sell_order_id: int
    price: float
    quantity: int
    timestamp: float
    
    def __repr__(self) -> str:
        return f"Trade({self.quantity}@${self.price:.2f})"
    
    @property
    def notional_value(self) -> float:
        """Total dollar value of the trade"""
        return self.price * self.quantity