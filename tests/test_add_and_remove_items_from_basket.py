
def test_add_and_remove_items_from_basket(app):
    app.store_front.navigate_to_litecart_shop()
    app.basket.add_product_from_most_popular()
    app.basket.add_product_from_campaigns()
    app.basket.add_product_from_latest_products()
    app.basket.open_basket()
    app.basket.clear_basket()