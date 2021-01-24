import pytest
from apitest.src.utilities.requestsUtility import RequestsUtility
import logging as logger
from apitest.src.dao.products_dao import ProductsDAO
from apitest.src.helpers.products_helper import ProductsHelper

pytestmark = [pytest.mark.products, pytest.mark.smoke]

@pytest.mark.tcid24
def test_get_all_products():
    req_helper = RequestsUtility()
    rs_api = req_helper.get("products")

    logger.debug(f"Response of list products:{rs_api}")
    assert rs_api, f"Response of list all customers is empty"


@pytest.mark.tcid25
def test_get_product_by_id():
    # get a product (test data) from db
    rand_product = ProductsDAO().get_random_product_from_db(1)
    rand_product_id = rand_product[0]['ID']
    db_name = rand_product[0]['post_title']

    # make the call
    product_helper = ProductsHelper()
    rs_api = product_helper.get_product_by_id(rand_product_id)
    api_name = rs_api['name']

    # verify the response
    assert db_name == api_name, f"Get product by id returned wrong product." \
                                f"ID: {rand_product_id}," \
                                f"DB name: {db_name}," \
                                f"API name: {api_name}."
