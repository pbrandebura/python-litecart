from model.product import Product
import pytest

testdata = Product(product_name="nnnnaczka", product_code="feee", quantity="44",
                   short_description="short_description short_description",
                   full_description="Full description, Full descriptionFull descriptionFull description")


@pytest.mark.parametrize("product", [testdata])
def test_add_new_product(app, product):
    app.admin_panel.login_to_admin_panel('admin', 'admin')
    app.admin_panel.navigate_to_catalog_tab()
    app.product.add_new_product(product)
