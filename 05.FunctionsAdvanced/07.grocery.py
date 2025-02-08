def grocery_store(**products):
    sorted_products = sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    return "\n".join(f"{name}: {qty}" for name, qty in sorted_products)
