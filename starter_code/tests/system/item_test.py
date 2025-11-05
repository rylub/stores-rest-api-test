from starter_code.models.store import StoreModel
from starter_code.models.user import UserModel
from starter_code.models.item import ItemModel
from starter_code.tests.base_test import BaseTest
import json


class ItemTest(BaseTest):
    def setUp(self):
        super(ItemTest, self).setUp()
        with self.app() as client:
            with self.app_context():
                UserModel('test', '12345').save_to_db()

                auth_request = client.post(
                    '/auth',
                    data=json.dumps({'username': 'test', 'password': '12345'}),
                    headers={'Content-Type': 'application/json'})

                auth_data = json.loads(auth_request.data)
                access_token = auth_data['access_token']

                self.headers = {'Authorization': f"Bearer {access_token}"}


    def test_get_item_no_auth(self):
        with self.app() as client:
            with self.app_context():
                resp = client.get('item/test')
                self.assertEqual(resp.status_code, 401)


    def test_get_item_not_found(self):
        with self.app() as client:
            with self.app_context():
                response = client.get('/item/test', headers=self.headers)

                self.assertEqual(response.status_code, 404)
                self.assertDictEqual({'message': 'Item not found'}, json.loads(response.data))


    def test_get_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 19.99, 1).save_to_db()
                response = client.get('/item/test', headers=self.headers)

                self.assertEqual(response.status_code, 200)


    def test_delete_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 19.99, 1).save_to_db()
                response = client.delete('/item/test')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({"message": "Item deleted"}, json.loads(response.data))


    def test_create_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                response = client.post('/item/test', json = {'price': 17.99, 'store_id': 1})

                self.assertEqual(response.status_code, 201)

                expected = {
                    'name': 'test',
                    'price': 17.99,
                    'store_id': 1,
                }
                self.assertDictEqual(expected, json.loads(response.data))


    def test_create_duplicate_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 17.99, 1).save_to_db()
                response = client.post('/item/test', json={'price': 17.99, 'store_id': 1})

                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({"message": f"An item with name 'test' already exists."}, json.loads(response.data))


    def test_put_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                resp = client.put('/item/test', json={'price': 17.99, 'store_id': 1})

                self.assertEqual(resp.status_code, 200)
                self.assertEqual(ItemModel.find_by_name('test').price, 17.99)
                self.assertDictEqual({'name': 'test', "price": 17.99, "store_id": 1}, json.loads(resp.data))


    def test_put_update_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 12.99, 1).save_to_db()

                self.assertEqual(ItemModel.find_by_name('test').price, 12.99)

                resp = client.put('/item/test', json={'price': 17.99, 'store_id': 1})

                self.assertEqual(resp.status_code, 200)
                self.assertEqual(ItemModel.find_by_name('test').price, 17.99)
                self.assertDictEqual({'name': 'test', "price": 17.99, "store_id": 1}, json.loads(resp.data))


    def test_item_list(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 12.99, 1).save_to_db()

                resp = client.get('/items')

                self.assertDictEqual({'items': [{'name': 'test', "price": 12.99, "store_id": 1}]}, json.loads(resp.data))


