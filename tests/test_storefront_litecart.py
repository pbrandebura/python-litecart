def test_verify_number_of_sale_label(app):
    # test to verify if no more than 1 sale label per product is displayed
    app.store_front.navigate_to_litecart_shop()
    app.store_front.sale_label_qty_checker(list_name="box-most-popular")
    app.store_front.sale_label_qty_checker(list_name="box-campaigns")
    app.store_front.sale_label_qty_checker(list_name="box-latest-products")


def test_confirm_pdp_opens_with_correct_details(app):
    app.store_front.navigate_to_litecart_shop()
    product_details_front = app.store_front.get_first_campaign_product_details_store_front()
    app.store_front.open_pdp_for_first_product()
    product_details_pdp = app.store_front.get_product_details_from_pdp()
    assert product_details_front==product_details_pdp
