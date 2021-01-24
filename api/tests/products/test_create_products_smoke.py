import pytest
from apitest.src.utilities.genericUtilities import generate_random_string
from apitest.src.helpers.products_helper import ProductsHelper
from apitest.src.dao.products_dao import ProductsDAO

pytestmark = [pytest.mark.products, pytest.mark.smoke]

@pytest.mark.tcid26
def test_create_1_simple_product():

    # generate some data
    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = "simple"
    payload['regular_price'] = "10.99"

    # make the call
    product_rs = ProductsHelper().call_create_product(payload)

    # verify the response is not empty
    assert product_rs, f"Create product api response is empty. Payload: {payload}"
    assert product_rs['name'] == payload['name'], f"Create product api call response has" \
           f"unexpected name. Expected: {product_rs['name']}, Actual: {payload['name']}"

    # verify the product exists in db
    product_id = product_rs['id']
    db_product = ProductsDAO().get_product_by_id(product_id)

    assert payload['name'] == db_product[0]['post_title'], f"Create product, title in db does not match" \
                  f"Title in api. DB: {db_product['post_title']}, API: {payload['name']}"
