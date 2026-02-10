from abc import ABC, abstractmethod
from typing import List
from enum import Enum

# ============= BASE INTERFACES =============

class Item(ABC):
    """Base interface for all items"""
    
    @abstractmethod
    def get_price(self) -> float:
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        pass

class Pizza(Item):
    """Pizza interface extending Item"""
    
    def __init__(self, multiplier: float = 1.0):
        self.multiplier = multiplier

class Dessert(Item):
    """Dessert interface extending Item"""
    pass

# ============= CONCRETE PIZZA IMPLEMENTATIONS =============

class SmallPizza(Pizza):
    def __init__(self, multiplier: float = 1.0):
        super().__init__(multiplier)
        self.base_price = 100
    
    def get_price(self) -> float:
        return self.multiplier * self.base_price
    
    def get_description(self) -> str:
        return f"Small Pizza (Tier multiplier: {self.multiplier})"

class MediumPizza(Pizza):
    def __init__(self, multiplier: float = 1.0):
        super().__init__(multiplier)
        self.base_price = 150
    
    def get_price(self) -> float:
        return self.multiplier * self.base_price
    
    def get_description(self) -> str:
        return f"Medium Pizza (Tier multiplier: {self.multiplier})"

class LargePizza(Pizza):
    def __init__(self, multiplier: float = 1.0):
        super().__init__(multiplier)
        self.base_price = 200
    
    def get_price(self) -> float:
        return self.multiplier * self.base_price
    
    def get_description(self) -> str:
        return f"Large Pizza (Tier multiplier: {self.multiplier})"

# ============= DECORATOR PATTERN FOR TOPPINGS =============

class PizzaDecorator(Pizza):
    """Base decorator for pizza toppings"""
    
    def __init__(self, pizza: Pizza):
        super().__init__(pizza.multiplier)
        self.pizza = pizza

class ChickenPizzaDecorator(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)
        self.chicken_price = 50
    
    def get_price(self) -> float:
        return self.pizza.get_price() + self.chicken_price
    
    def get_description(self) -> str:
        return self.pizza.get_description() + " + Chicken"

class CheeseDecorator(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)
        self.cheese_price = 30
    
    def get_price(self) -> float:
        return self.pizza.get_price() + self.cheese_price
    
    def get_description(self) -> str:
        return self.pizza.get_description() + " + Extra Cheese"

class PepperoniDecorator(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)
        self.pepperoni_price = 40
    
    def get_price(self) -> float:
        return self.pizza.get_price() + self.pepperoni_price
    
    def get_description(self) -> str:
        return self.pizza.get_description() + " + Pepperoni"

# ============= COUPON DECORATOR PATTERN =============

class ItemCouponDecorator(Item):
    """Base coupon decorator"""
    
    def __init__(self, item: Item):
        self.item = item

class PizzaCouponDecorator(ItemCouponDecorator):
    def __init__(self, item: Item, discount_percent: float = 10):
        super().__init__(item)
        self.discount_percent = discount_percent
    
    def get_price(self) -> float:
        original_price = self.item.get_price()
        discount = original_price * (self.discount_percent / 100)
        return original_price - discount
    
    def get_description(self) -> str:
        return f"{self.item.get_description()} [{self.discount_percent}% OFF]"

class NthPizzaDecorator(ItemCouponDecorator):
    """Special decorator for nth pizza free/discount"""
    
    def __init__(self, item: Item, discount_percent: float = 50):
        super().__init__(item)
        self.discount_percent = discount_percent
    
    def get_price(self) -> float:
        original_price = self.item.get_price()
        discount = original_price * (self.discount_percent / 100)
        return original_price - discount
    
    def get_description(self) -> str:
        return f"{self.item.get_description()} [Nth Pizza {self.discount_percent}% OFF]"

# ============= STRATEGY PATTERN FOR COUPONS =============

class ItemCouponStrategy(ABC):
    """Strategy interface for applying coupons"""
    
    @abstractmethod
    def apply_coupon(self, item: Item, cart_items: List[Item]) -> Item:
        pass

class PizzaCouponStrategy(ItemCouponStrategy):
    def apply_coupon(self, item: Item, cart_items: List[Item]) -> Item:
        # Count existing pizzas in cart
        pizza_count = sum(1 for cart_item in cart_items if isinstance(cart_item, Pizza))
        
        # Every 3rd pizza gets 50% off
        if (pizza_count + 1) % 3 == 0:
            return NthPizzaDecorator(item, 50)
        # Regular pizza discount
        elif pizza_count >= 1:
            return PizzaCouponDecorator(item, 10)
        
        return item

class DessertCouponStrategy(ItemCouponStrategy):
    def apply_coupon(self, item: Item, cart_items: List[Item]) -> Item:
        # Simple dessert discount if cart has pizza
        has_pizza = any(isinstance(cart_item, Pizza) for cart_item in cart_items)
        if has_pizza:
            return ItemCouponDecorator(item)  # Could implement DessertCouponDecorator
        return item

# ============= FACTORY PATTERN =============

class PizzaSize(Enum):
    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"

class PizzaFactoryInterface(ABC):
    """Abstract factory interface for creating pizzas"""
    
    def __init__(self, multiplier: float):
        self.multiplier = multiplier
    
    @abstractmethod
    def get_pizza(self, size: PizzaSize) -> Pizza:
        pass

class Tier1Factory(PizzaFactoryInterface):
    def __init__(self):
        super().__init__(multiplier=1.25)
    
    def get_pizza(self, size: PizzaSize) -> Pizza:
        if size == PizzaSize.SMALL:
            return SmallPizza(self.multiplier)
        elif size == PizzaSize.MEDIUM:
            return MediumPizza(self.multiplier)
        elif size == PizzaSize.LARGE:
            return LargePizza(self.multiplier)
        else:
            raise ValueError(f"Unknown pizza size: {size}")

class Tier2Factory(PizzaFactoryInterface):
    def __init__(self):
        super().__init__(multiplier=1.5)  # Premium tier
    
    def get_pizza(self, size: PizzaSize) -> Pizza:
        if size == PizzaSize.SMALL:
            return SmallPizza(self.multiplier)
        elif size == PizzaSize.MEDIUM:
            return MediumPizza(self.multiplier)
        elif size == PizzaSize.LARGE:
            return LargePizza(self.multiplier)
        else:
            raise ValueError(f"Unknown pizza size: {size}")

# ============= ABSTRACT FACTORY =============

class PizzaFactoryFactory:
    """Factory for creating pizza factories"""
    
    @staticmethod
    def get_pizza_factory(tier: str) -> PizzaFactoryInterface:
        if tier.upper() == "TIER1":
            return Tier1Factory()
        elif tier.upper() == "TIER2":
            return Tier2Factory()
        else:
            raise ValueError(f"Unknown tier: {tier}")

# ============= CART SYSTEM =============

class CouponStrategyFactory:
    """Factory for getting appropriate coupon strategy"""
    
    @staticmethod
    def get_strategy(item: Item) -> ItemCouponStrategy:
        if isinstance(item, Pizza):
            return PizzaCouponStrategy()
        elif isinstance(item, Dessert):
            return DessertCouponStrategy()
        else:
            # Default strategy - no coupon
            return type('NoStrategy', (ItemCouponStrategy,), {
                'apply_coupon': lambda self, item, cart_items: item
            })()

class Cart:
    def __init__(self):
        self.items: List[Item] = []
    
    def add_item(self, item: Item):
        # Apply coupon strategy based on item type
        strategy = CouponStrategyFactory.get_strategy(item)
        item_with_coupon = strategy.apply_coupon(item, self.items)
        self.items.append(item_with_coupon)
    
    def get_total(self) -> float:
        return sum(item.get_price() for item in self.items)
    
    def get_receipt(self) -> str:
        receipt = "=== PIZZA SHOP RECEIPT ===\n"
        for i, item in enumerate(self.items, 1):
            receipt += f"{i}. {item.get_description()} - ${item.get_price():.2f}\n"
        receipt += f"\nTOTAL: ${self.get_total():.2f}"
        return receipt

# ============= APPLICATION DEMO =============

def demo_pizza_shop():
    print("🍕 Welcome to the Pizza Shop Billing System Demo!\n")
    
    # Create cart
    cart = Cart()
    
    # Create pizza factory
    pff = PizzaFactoryFactory()
    tier1_factory = pff.get_pizza_factory("TIER1")
    
    # Order 1: Small pizza with chicken
    pizza1 = tier1_factory.get_pizza(PizzaSize.SMALL)
    pizza1_with_chicken = ChickenPizzaDecorator(pizza1)
    cart.add_item(pizza1_with_chicken)
    
    # Order 2: Medium pizza with cheese and pepperoni
    pizza2 = tier1_factory.get_pizza(PizzaSize.MEDIUM)
    pizza2_with_cheese = CheeseDecorator(pizza2)
    pizza2_with_cheese_and_pepperoni = PepperoniDecorator(pizza2_with_cheese)
    cart.add_item(pizza2_with_cheese_and_pepperoni)
    
    # Order 3: Large pizza (this should get nth pizza discount)
    pizza3 = tier1_factory.get_pizza(PizzaSize.LARGE)
    cart.add_item(pizza3)
    
    # Order 4: Another small pizza to test regular discount
    pizza4 = tier1_factory.get_pizza(PizzaSize.SMALL)
    pizza4_with_cheese = CheeseDecorator(pizza4)
    cart.add_item(pizza4_with_cheese)
    
    # Print receipt
    print(cart.get_receipt())

if __name__ == "__main__":
    demo_pizza_shop()