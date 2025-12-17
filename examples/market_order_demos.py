"""
Demonstrate market order functionality.
"""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src import Order, OrderBook


def main():
    """Test market orders"""
    print("=" * 70)
    print(" " * 20 + "MARKET ORDERS DEMO")
    print("=" * 70)
    
    book = OrderBook()
    order_id = 1
    
    # Build the book with limit orders
    print("\n📝 Step 1: Build order book with limit orders")
    print("-" * 70)
    
    limit_orders = [
        Order(order_id, 10, True, time.time(), 99.0, "limit"),
        Order(order_id+1, 15, True, time.time(), 100.0, "limit"),
        Order(order_id+2, 20, True, time.time(), 101.0, "limit"),
        Order(order_id+3, 25, False, time.time(), 103.0, "limit"),
        Order(order_id+4, 30, False, time.time(), 104.0, "limit"),
    ]
    order_id += 5
    
    for order in limit_orders:
        book.add_order(order)
        print(f"  Added: {order}")
    
    print(f"\n  {book}")
    book.print_depth(levels=5)
    
    # Test 1: Market buy order (takes from asks)
    print("\n📈 Step 2: Market BUY order (takes liquidity)")
    print("-" * 70)
    
    market_buy = Order(order_id, 40, True, time.time(), None, "market")
    order_id += 1
    print(f"  Incoming: {market_buy}")
    print(f"  This will match with best asks (lowest prices first)")
    
    trades = book.add_order(market_buy)
    
    print(f"\n  ✅ Generated {len(trades)} trade(s):")
    for i, trade in enumerate(trades, 1):
        print(f"     Trade {i}: {trade}")
    
    if market_buy.quantity > 0:
        print(f"\n  ⚠️  Unfilled quantity: {market_buy.quantity} (not enough liquidity)")
    
    print(f"\n  {book}")
    book.print_depth(levels=5)
    
    # Test 2: Market sell order (takes from bids)
    print("\n📉 Step 3: Market SELL order (takes liquidity)")
    print("-" * 70)
    
    market_sell = Order(order_id, 30, False, time.time(), None, "market")
    order_id += 1
    print(f"  Incoming: {market_sell}")
    print(f"  This will match with best bids (highest prices first)")
    
    trades = book.add_order(market_sell)
    
    print(f"\n  ✅ Generated {len(trades)} trade(s):")
    for i, trade in enumerate(trades, 1):
        print(f"     Trade {i}: {trade}")
    
    print(f"\n  {book}")
    book.print_depth(levels=5)
    
    print("\n" + "=" * 70)
    print("✅ MARKET ORDERS WORKING!")
    print("=" * 70)
    
    print("\n💡 Key Differences:")
    print("  • Limit orders: Join the book if not matched")
    print("  • Market orders: Execute immediately or get rejected")
    print("  • Market orders: Take whatever price is available")
    print("  • Market orders: Used when speed > price")


if __name__ == "__main__":
    main()