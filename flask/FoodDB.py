from flask import request
from flask_restx import Resource, Api, Namespace, fields
import data

FoodDBs = {}
count = 1


print("TEST")
FoodDB = Namespace(
    name="FoodDB",
    description="Food DataBase Rest API.",
)

FoodDB_fields = FoodDB.model('식당 인덱스(INDEX)', {  # Model 객체 생성
    'data': fields.String(required=True, example="식당 이름")
})

FoodDB_fields_with_id = FoodDB.inherit('식당 이름', FoodDB_fields, {
    'FoodDB_id': fields.Integer(description='식당 번호')
})

@FoodDB.route('')
class FoodDBGet(Resource):
    @FoodDB.response(200, 'Success', FoodDB_fields_with_id) 
    def get(self, FoodDB_id):
        "식당 리스트 데이터 가져오기"
        return {
            'FoodDB_id': FoodDB_id,
            'data': FoodDBs[FoodDB_id]
        }


@FoodDB.route('/<int:FoodDB_id>')
@FoodDB.doc(params={'FoodDB_id': 'An ID'})


class FoodDBSimple(Resource):
    @FoodDB.response(202, 'Success', FoodDB_fields_with_id)
    @FoodDB.response(500, 'Failed')
    def put(self, FoodDB_id):
        "FoodDB 리스트에 FoodDB_id와 일치하는 식당을 수정"
        FoodDBs[FoodDB_id] = request.json.get('data')
        return {
            'FoodDB_id': FoodDB_id,
            'data': FoodDBs[FoodDB_id]
        }, 202

@FoodDB.route('/search/<params>')
class GetDatas(Resource):
    
