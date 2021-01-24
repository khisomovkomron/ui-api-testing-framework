
import pytest
from datetime import datetime, timedelta
import pdb
from apitest.src.helpers.products_helper import ProductsHelper
from apitest.src.dao.products_dao import ProductsDAO

@pytest.mark.regression
class TestListProductsWithFilter(object):

    @pytest.mark.tcid51
    def test_list_products_with_filter_after(self):

        # create data
        x_days_from_today = 300
        _after_created_date = datetime.now().replace(microsecond=0) - timedelta(days=x_days_from_today)
        after_created_date = _after_created_date.isoformat()

        payload = dict()
        payload['after'] = after_created_date

        # make the call
        rs_api = ProductsHelper().call_list_products(payload)
        assert rs_api, f"Empty response for list products with filter"

        #get data from db
        db_products = ProductsDAO().get_products_created_after_given_date(after_created_date)

        #verify response match db
        assert len(rs_api) == len(db_products), f"List products with filter 'after' returned unexpected number " \
                                                f"of products. Expected: {len(db_products)}, Actual:{len(rs_api)}"

        ids_in_api = [i['id']for i in rs_api]
        ids_in_db = [i['ID']for i in db_products]

        idf_diff = list(set(ids_in_api) - set(ids_in_db))
        assert not idf_diff, f"List products with filter. Product ids in response mismatch in db."
        pdb.set_trace()
