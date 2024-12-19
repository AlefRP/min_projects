from typing import List, Dict
from time import sleep

from models.product import Product
from utils.helper import format_float_str_currency

products: List[Product] = []
cart: List[Dict[Product, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('=====================')
    print('======= Welcome to the Market =======')
    print('======== Some Shopping =============')
    print('=====================')

    print('Select an option below:')
    print('1 - Register Product')
    print('2 - List Products')
    print('3 - Buy Product')
    print('4 - View Cart')
    print('5 - Close Order')
    print('6 - Exit')

    option: int = int(input())

    match option:
        case 1:
            register_product()
        case 2:
            show_products()
        case 3:
            by_product()
        case 4:
            view_cart()
        case 5:
            close_order()
        case 6:
            print('Thank you for shopping with us!')
            sleep(2)
            exit(0)
        case _:
            print('Invalid Option')
            sleep(1)
            menu()

def register_product() -> None:
    print('Register Product')
    print('=====================')

    name: str = input('Enter the name of the product: ')
    price: float = float(input('Enter the price of the product: '))

    product: Product = Product(name, price)
    products.append(product)

    print(f'The product {product.name} was registered successfully!')
    sleep(2)
    menu()

def show_products() -> None:
    if len(products) > 0:
        print('List Products')
        print('=====================')

        for product in products:
            print(product)
            print('=====================')
            sleep(1)
    else: 
        print('There are no products registered.')
    
    sleep(2)
    menu()

def by_product() -> None:
    pass

def view_cart() -> None:
    pass

def close_order() -> None:
    if len(cart) > 0:
        total: float = 0

        print('Cart')
        print('=====================')

        for item in cart:
            for key in item:
                print(key)
                total += key.price * item[key]
                print(f'Quantity: {item[key]}')
                print('=====================')
                sleep(1)
        
        print(f'Your total is: {format_float_str_currency(total)}')
        print('Thanks for your purchase!')
        cart.clear()
        sleep(5)
    else:
        print('The cart is empty.')
    
    sleep(2)
    menu()

def take_product_by_code(code: int) -> Product:
    p: Product = None

    for product in products:
        if product.code == code:
            p = product
    return p


if __name__ == '__main__':
    main()