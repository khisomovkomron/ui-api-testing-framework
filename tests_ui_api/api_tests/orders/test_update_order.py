from base_helpers.api_helpers.helpers.orders_helper import OrdersHelper
from base_helpers.api_helpers.utilities.wooAPIUtility import WooAPIUtility
from base_helpers.api_helpers.utilities.genericUtilities import generate_random_string
import pdb
import pytest

pytestmark = [pytest.mark.orders, pytest.mark.regression, pytest.mark.regression]

@pytest.mark.parametrize("new_status", [
    pytest.param('cancelled', marks=[pytest.mark.tcid55, pytest.mark.smoke]),
    pytest.param('completed', marks=pytest.mark.tcid56),
    pytest.param('on-hold', marks=pytest.mark.tcid57),
])
def test_update_order_status(new_status):

    # new_status = 'cancelled'
    # new_status = 'completed'

    # create new order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    cur_status = order_json['status']
    assert cur_status != new_status, f"Current status of order is already {new_status}." \

    # update the status
    order_id = order_json['id']
    payload = {"status": new_status}
    rs_update = order_helper.call_update_an_order(order_id, payload)

    # get order information
    new_order_info = order_helper.call_retrieve_an_order(order_id)

    # verify the new order status is what was updated
    assert new_order_info['status'] == new_status, f"Updated order status to '{new_status}'," \
                                                   f" but order is still '{new_order_info['status']}'"


@pytest.mark.tcid58
def test_update_order_status_to_random_string():

    new_status = 'acdefg'

    # create new order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    order_id = order_json['id']

    # update the status

    payload = {"status": new_status}
    rs_api = WooAPIUtility().put(f'orders/{order_id}', params=payload, expected_status_code=400)

    assert rs_api['code'] == 'rest_invalid_param', "Update order status to random string did not have" \
           f"correct code in response. Expected 'rest_invalid_param' Actual: {rs_api['code']}"

    assert rs_api['message'] == 'Неверный параметр: status', f"Update order status to random string did not have" \
         f"correct message in response. Expected 'Неверный параметр: status' Actual: {rs_api['message']}"
    pdb.set_trace()



@pytest.mark.tcid59
def test_update_order_customer_note():

    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    order_id = order_json['id']

    rand_string = generate_random_string(40)
    payload = {"customer_note": rand_string}
    rs_update = order_helper.call_update_an_order(order_id, payload)

    # get order information
    new_order_info = order_helper.call_retrieve_an_order(order_id)
    assert new_order_info['customer_note'] == rand_string, f"Update order's customer_note field" \
                                                           f"failed. Expected {rand_string}, actual {new_order_info['customer_note']}"
