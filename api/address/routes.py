from flask_restplus import Namespace, Resource
from mongoengine.errors import DoesNotExist

from .serializers import *
from .models import *

np = Namespace("address")

class AddressRoutes(Resource):
    def get(self, id = None):
        try:
            if id:
                try:
                    address = Address.objects.get(id = id)
                    return address.payload()
                except DoesNotExist:
                    return {'msg': "Address not found"}, 404
            else:
                addresses = Address.objects.all()
                response = list()
                for address in addresses:
                    response.append(address.payload())
                return response
        except Exception as e:
            return {'msg': 'Server Error'}, 500

    @np.expect(add_address)
    def post(self):
        try:
            # adding new address to database
            address = Address(**np.payload)
            address.save()
            return {"id" : str(address.id)}, 201
        except Exception as e:
            print(e)
            return {"msg": "Server Error"}, 500

    @np.expect(updated_address)
    def put(self, id):
        try: 
            address = Address.objects.get(id = id)

            # removing null values from payload
            data = dict(np.payload)
            for key, value in np.payload.items():
                if value is None:
                    del data[key]

            address.update(**data)
            return {"msg": "Success"}
        except DoesNotExist:
            return {'msg': "Address not found"}, 404
        except Exception as e:
            return {"msg": "Server Error"}, 500

    def delete(self, id):
        try:
            address = Address.objects.get(id = id)
            address.delete()
            return {"msg": "Success"}
        except DoesNotExist:
            return {'msg': "Address not found"}, 404
        except Exception as e:
            return {"msg": "Server Error"}, 500
    
np.add_resource(AddressRoutes, "", methods = ['GET', 'POST'])
np.add_resource(AddressRoutes,'/<id>', methods = ['GET', 'PUT', 'DELETE'])