
import pytest
from base_helpers.api_helpers.utilities.requestsUtility import RequestsUtility
import logging as logger

pytestmark = [pytest.mark.customers, pytest.mark.smoke, pytest.mark.regression]


@pytest.mark.tcid30
def test_get_all_customers():
    req_helper = RequestsUtility()
    rs_api = req_helper.get('customers')
    logger.debug(f"Response of list customers: {rs_api}")

    assert rs_api, f"Response of list all customers is empty"


