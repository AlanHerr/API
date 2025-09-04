from model.products_models import Product
from config.database import get_db_session

def get_all_products():
    session = get_db_session()
    products = session.query(Product).all()
    session.close()
    return products

def get_product_by_id(product_id):
    session = get_db_session()
    product = session.query(Product).filter_by(id=product_id).first()
    session.close()
    return product

def create_product(data):
    session = get_db_session()
    product = Product(**data)
    session.add(product)
    session.commit()
    session.refresh(product)
    session.close()
    return product

def update_product(product_id, data):
    session = get_db_session()
    product = session.query(Product).filter_by(id=product_id).first()
    if product:
        for key, value in data.items():
            setattr(product, key, value)
        session.commit()
        session.refresh(product)
    session.close()
    return product

def delete_product(product_id):
    session = get_db_session()
    product = session.query(Product).filter_by(id=product_id).first()
    if product:
        session.delete(product)
        session.commit()
    session.close()
    return product