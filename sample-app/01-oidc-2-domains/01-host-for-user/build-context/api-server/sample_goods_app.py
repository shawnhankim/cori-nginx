"""Sample Goods Management API

This code provide the API to CRUD (Create/Read/Update/Delete) goods.

Attributes:
    GoodsDAO (...)   : Goods data access object for sample goods management API

    GoodsListManager : API for reading list of goods and creating a goods
    
    GoodsRUDManager  : API for reading/updating/deleting goods using goods ID
    
Misc.:
    How to run : FLASK_APP=sample_goods_app.py flask run -h 0.0.0.0 -p 9002
"""

from flask          import Flask, request
from flask_restplus import Api, Resource, fields

# Create Flask App
app = Flask(__name__) 

# Create API
api = Api(app, version='1.0', title='NGINX DevPortal : Sample Goods Management API', 
          description='APIs for creating/reading/updating/deleting goods')

# Create namespace
ns  = api.namespace('goods', 
          description='Creating/Reading/Updating/Deleting Goods')


# Create data model for REST API
model_goods = api.model('row_goods', {
    'goods_id'  : fields.Integer(readOnly    = True, 
                                 required    = True, 
                                 description = 'Goods ID', 
                                 help        = 'Goods ID must be entered'),
    'goods_name': fields.String (required    = True, 
                                 description = 'Goods Name',
                                 help        = 'Goods name must be entered')
})

class GoodsDAO(object):
    '''Goods Data Access Object'''
    def __init__(self):
        self.counter = 0
        self.rows    = []

    def get(self, goods_id):
        '''Read goods information using goods goods ID'''
        for row in self.rows:
            if row['goods_id'] == goods_id:
                return row
        api.abort(404, "{} doesn't exist".format(goods_id))

    def create(self, data):
        '''Create new goods'''
        row = data
        # row['goods_id'] = self.counter = self.counter + 1
        self.rows.append(row)
        return row

    def update(self, goods_id, data):
        '''Update goods' information'''
        row = self.get(goods_id)
        row.update(data)
        return row

    def delete(self, goods_id):
        '''Delete one of goods information using goods ID'''
        row = self.get(goods_id)
        self.rows.remove(row)

# Create data access object with sample data
DAO = GoodsDAO() 
DAO.create({'goods_id': 1, 'goods_name': 'Samsung Laptop'})
DAO.create({'goods_id': 2, 'goods_name': 'MacBook Pro'   })
DAO.create({'goods_id': 3, 'goods_name': 'DELL Laptop'   })

# Routing under the 'x.x.x.x/goods' of namespace 
@ns.route('/') 
class GoodsListManager(Resource):
    @ns.marshal_list_with(model_goods)
    def get(self):
        '''Read all of goods list'''
        return DAO.rows

    @ns.expect(model_goods)
    @ns.marshal_with(model_goods, code=201)
    def post(self):
        '''Create new good using goods ID'''
        print('input goods_name is', request.json['goods_name'])
        return DAO.create(api.payload), 201

# Routing under the 'x.x.x.x/goods/{goods_id}' of namespace 
@ns.route   ('/<int:goods_id>') 
@ns.response(404, 'Unable to find goods ID')
@ns.param   ('goods_id', 'Please enter the goods ID')
class GoodsRUDManager(Resource):
    @ns.marshal_with(model_goods)
    def get(self, goods_id):
        '''Read the goods information using goods ID'''
        return DAO.get(goods_id)

    def delete(self, goods_id):
        '''Delete the goods using goods ID'''
        DAO.delete(goods_id)
        return '', 200

    @ns.expect(model_goods)
    @ns.marshal_with(model_goods)
    def put(self, goods_id):
        '''Update the goods information for goods ID'''
        return DAO.update(goods_id, api.payload)
