import pytest
from base_helpers.api_helpers.helpers.coupon_helper import CouponsHelper
from base_helpers.api_helpers.utilities.genericUtilities import generate_random_string, generate_random_coupon_code
from base_helpers.api_helpers.utilities.wooAPIUtility import WooAPIUtility
import random
import logging as logger

pytestmark = [pytest.mark.coupons, pytest.mark.smoke, pytest.mark.regression]

@pytest.fixture(scope='module')
def my_setup():
    info = {}
    info['coupon_helper'] = CouponsHelper()

    return info


@pytest.mark.parametrize("discount_type",
                         [
                             pytest.param(None, marks=[pytest.mark.tcid36, pytest.mark.smoke]),
                             pytest.param('percent', marks=[pytest.mark.tcid37, pytest.mark.smoke]),
                             pytest.param('fixed_product', marks=pytest.mark.tcid38),
                             pytest.param('fixed_cart', marks=pytest.mark.tcid39),
                         ])
def test_create_coupon_percent_discount_type(my_setup, discount_type):
    """
    Creates a coupon with given 'discount type' verify the coupon is created.
    """

    logger.info("Testing create coupon api for 50% off coupon.")

    # one of the tests is for not sending dicount type and verify the defualt is used, is if None is given check for default
    expected_discount_type = discount_type if discount_type else 'fixed_cart'

    pct_off = str(random.randint(50, 90)) + ".00"
    coupon_code = generate_random_coupon_code(sufix="tcid37", lenght=10)

    # get the helper object
    coupon_helper = my_setup['coupon_helper']

    # prepare data and call api
    payload = dict()
    payload['code'] = coupon_code
    payload['amount'] = pct_off
    if discount_type:
        payload['discount_type'] = discount_type
    rs_coupon = coupon_helper.call_create_coupon(payload=payload)
    coupon_id = rs_coupon['id']

    # verify coupon is actually created by doing a retrieve
    rs_coupon_2 = coupon_helper.call_retrieve_coupon(coupon_id)

    # verify the response
    assert rs_coupon_2['amount'] == pct_off, f"Create coupon with 50% off responded {rs_coupon_2['amount']} for amount." \
                                             f"Expected: {pct_off}, Actual: {rs_coupon_2['amount']}."
    assert rs_coupon_2['code'] == coupon_code.lower(), f"Create coupon response has wrong 'code'. " \
                                                       f"Expected: {coupon_code.lower()}, Actual: {rs_coupon_2['code']}."
    assert rs_coupon_2[
               'discount_type'] == expected_discount_type, f"Create coupon responded with wrong 'discount_type'." \
                                                           f"Expected: {expected_discount_type}, Actual: {rs_coupon_2['discount_type']}."

@pytest.mark.tcid40
def test_create_coupon_with_invalid_discount_type():

    logger.info("Testing create coupon api with invalis 'discount_type")

    payload = dict()
    payload['code'] = generate_random_coupon_code(sufix='tcid40', lenght=10)
    payload['amount'] = str(random.randint(50, 90)) +"0.00"
    payload['discount_type'] = generate_random_string()
    rs_coupon = WooAPIUtility().post('coupons', params=payload, expected_status_code=400)

    assert rs_coupon['code'] == 'rest_invalid_param',f"Create coupon with invalid 'discount_type'," \
           f"returned 'code' = {rs_coupon['code']}, Expected code: 'rest_invalid_param'."
    assert rs_coupon['message'] == 'Неверный параметр: discount_type', f"Crete coupon with invalid 'discount_type' " \
            f"returned 'message={rs_coupon['message']}', Expected message = 'Неверный параметр: discount_type',"
