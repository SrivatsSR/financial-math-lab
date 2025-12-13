"""
Basic usage example for the order book.
"""

import sys
from pathlib import Path
import time
from src import Order, OrderBook

sys.path.insert(0, str(Path(__file__).parent.parent))

def main():
    """Demonstrate basic order book functionality"""
    print("=" * 60)
    print("HIGH-PERFORMANCE ORDER BOOK - BASIC EXAMPLE")
    print("=" * 60)
    
    # Create order book
    book = OrderBook()
    print(f"\n Order book initialized")
    
    # Add some orders
    print("\n Adding orders...")
    
    orders = [
        Order(1, 100.0, 10, True, time.time()),   # Buy 10 @ $100
        Order(2, 101.0, 5, True, time.time()),    # Buy 5 @ $101
        Order(3, 102.0, 15, False, time.time()),  # Sell 15 @ $102
        Order(4, 103.0, 8, False, time.time()),   # Sell 8 @ $103
    ]
    
    for order in orders:
        book.add_order(order)
        print(f"  Added: {order}")
    
    # Show book state
    print(f"\n Current State:")
    print(f"  {book}")
    print(f"  Best Bid: ${book.get_best_bid():.2f}")
    print(f"  Best Ask: ${book.get_best_ask():.2f}")
    print(f"  Spread: ${book.get_spread():.2f}")
    print(f"  Mid Price: ${book.get_mid_price():.2f}")
    
    # Cancel an order
    print(f"\n Cancelling order 2...")
    success = book.cancel_order(2)
    print(f"  Success: {success}")
    print(f"  New best bid: ${book.get_best_bid():.2f}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()