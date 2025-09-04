from repository.products_repository import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product
)

def list_products():
    return get_all_products()

def get_product(product_id):
    return get_product_by_id(product_id)

def add_product(data):
    return create_product(data)

def modify_product(product_id, data):
    return update_product(product_id, data)

def remove_product(product_id):
    return delete_product(product_id)