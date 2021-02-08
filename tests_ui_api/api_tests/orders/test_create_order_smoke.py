from base_helpers.api_helpers.dao.products_dao import ProductsDAO
from base_helpers.api_helpers.helpers.orders_helper import OrdersHelper
from base_helpers.api_helpers.helpers.customers_helper import CustomerHelper
import pytest

pytestmark = [pytest.mark.orders, pytest.mark.smoke, pytest.mark.regression]

@pytest.fixture(scope='module')
def my_order_smoke_setup():
    product_dao = ProductsDAO()
    order_helper = OrdersHelper()

    rand_product = product_dao.get_random_product_from_db(1)
    product_id = rand_product[0]['ID']

    info = {'product_id': product_id,
            'order_helper': order_helper}
    return info


@pytest.mark.tcid48
def test_create_paid_order_guest_user(my_order_smoke_setup):

    product_id = my_order_smoke_setup['product_id']
    order_helper = my_order_smoke_setup['order_helper']
    customer_id = 0

    # make the call
    info = {"line_items": [
                    {
                      "product_id": product_id,
                      "quantity": 1
                   }
                    ]}
    order_json = order_helper.create_order(additional_args=info)

    # verify response
    expected_products = [{'product_id': product_id}]
    order_helper.verify_order_is_created(order_json, customer_id, expected_products)


@pytest.mark.tcid49
def test_create_paid_order_new_created_customer(my_order_smoke_setup):
    #create helper objects

    order_helper = my_order_smoke_setup['order_helper']
    customer_helper = CustomerHelper()


    # make the call
    cust_info = customer_helper.create_a_customer()
    customer_id = cust_info['id']
    product_id = my_order_smoke_setup['product_id']

    info = {"line_items": [
                    {
                      "product_id": product_id,
                      "quantity": 1
                   }
                    ],
    "customer_id" : customer_id
    }
    order_json = order_helper.create_order(additional_args=info)

    # verify response
    expected_products = [{'product_id': product_id}]
    order_helper.verify_order_is_created(order_json, customer_id, expected_products)