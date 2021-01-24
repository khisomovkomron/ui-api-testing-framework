from base_helpers.api_helpers.helpers.products_helper import ProductsHelper
from base_helpers.api_helpers.utilities.genericUtilities import generate_random_string
from base_helpers.api_helpers.dao.products_dao import ProductsDAO
import pytest
import random

@pytest.mark.tcid61
def test_update_product_status():

    product_helper = ProductsHelper()
    product_dao = ProductsDAO()

    rand_products = product_dao.get_random_product_from_db(30)

    for product in rand_products:
        product_id = product['ID']
        product_data = product_helper.call_retrieve_product(product_id)
        if product_data['on_sale']:
            continue
        else:
            break
    else:
        test_product = random.choices(rand_products)
        product_id = test_product['ID']
        product_helper.call_update_product(product_id, {'sale_price': ''})

    new_price = str(random.randint(10, 100)) + '.' + str(random.randint(10, 99))
    payload = dict()
    payload['regular_price'] = new_price

    rs_update = product_helper.call_update_product(product_id, payload)

    assert rs_update['price'] == new_price, f"Update product api call response. Updating the 'regular_price' did not " \
                                            f"update the 'price' field. price field actual {rs_update['price']}, " \
                                            f"price field expected {new_price}"

    assert rs_update['regular_price'] == new_price, f"Update product api call response. Updating the 'regular_price' did not" \
                                            f"update the 'price' field. price field actual {rs_update['regular_price']}, " \
                                            f"price field expected {new_price}"

    rs_product = product_helper.call_retrieve_product(product_id)

    assert rs_product['price'] == new_price, f"Update product api call response. Updating the 'regular_price' did not " \
                                             f"update the 'price' field. Price field actual value {rs_product['price']}," \
                                             f"but expected: {new_price}"

    assert rs_product['regular_price'] == new_price, f"Update product api call response. Updating the 'regular_price' did not " \
                                             f"update the 'price' field. Price field actual value {rs_product['regular_price']}," \
                                             f"but expected: {new_price}"



@pytest.mark.tcid63
@pytest.mark.tcid64
def test_update_on_sale_field_buy_updating_sale_price():

    product_helper = ProductsHelper()

    regular_price = str(random.randint(10,100)) + '.' + str(random.randint(10,99))
    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = 'simple'
    payload['regular_price'] = regular_price

    product_info = product_helper.call_create_product(payload)
    product_id = product_info['id']
    assert not product_info['on_sale'], f"Newly created product should not have 'on_sale = True', Product id: {product_id}"
    assert not product_info['sale_price'], f"Newly created product should not have value for'sale_price' field"

    sale_price = float(regular_price) * 0.75
    product_helper.call_update_product(product_id, {"sale_price": str(sale_price)})
    product_after_update = product_helper.call_retrieve_product(product_id)
    assert product_after_update['on_sale'], f"Updated 'sale_price' of product, but the 'on_sale' did not set tot 'True'." \
                                            f"Product id: {product_id}"

    product_helper.call_update_product(product_id, {"sale_price": ''})
    product_after_update = product_helper.call_retrieve_product(product_id)
    assert not product_after_update['on_sale'], f"Updated 'sale_price=''' of product, but the 'on_sale' did not set tot 'False'." \
                                            f"Product id: {product_id}"


@pytest.mark.tcid65
def test_adding_sale_price_should_set_on_sale_flag_true():

    product_helper = ProductsHelper()
    product_dao = ProductsDAO()
    rand_product = product_dao.get_random_products_that_are_not_on_sale(qty=1)
    product_id = rand_product[0]['ID']

    original_info = product_helper.call_retrieve_product(product_id)
    assert not original_info['on_sale'], f"Getting test data with 'on_sale=False' but got 'True'." \
                                         f"Unable to use this product for test."

    sale_price = float(original_info['regular_price']) * 0.75

    payload = dict()
    payload['sale_price'] = str(sale_price)
    product_helper.call_update_product(product_id, payload=payload)

    after_info =product_helper.call_retrieve_product(product_id)
    assert after_info['sale_price'] == str(sale_price), f"Update product 'sale_price' but value did not update." \
                                                        f"Product id: {product_id}, Expected sale price: {sale_price}," \
                                                        f"Actual sale price: {after_info['sale_price']} "
