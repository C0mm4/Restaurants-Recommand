from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
import sql
from graphcopy import Graph
from datetime import datetime
from konlpy.tag import Kkma

app = Flask(__name__)

#jsonify 한글화 오류 고치는 코드
app.config['JSON_AS_ASCII'] = False
CORS(app)

testIndex = [1,2,3,4,5]

@app.route("/test", methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        print('POST')
        
        data = request.get_json()
        
        #client에서 post하려고 요청 온 데이터를 해당 방식으로 추출
        #post 방식의 경우에는 데이터뿐 아니라 다양한 값들이 필요한 데이터와 섞여서 오기 때문에 
        #우선 데이터 추출하는 과정이 필요
        
        print(data)

        # 데이터 딕셔너리형태로 추출
        
        print(data['keyword'])
        print(data['region'])
        
        # 그러면 서버에서 데이터 처리에 필요한 데이터 기준으로 키값으로 데이터 저장


    if request.method == 'GET':
        print('GET')
        
        # get 방식의 경우는 post 코드와는 달리 키값으로 데이터를 추출

        #keyword , region은 str
        keyword = request.args.get('keyword' , type = str)
        region = request.args.get('gu', type = str)
        kkma = Kkma()
        keywords = kkma.nouns(keyword)
        print(keywords)
        

        print(keyword)
        print(region)
        t = datetime.now()
        ret = g.search(keywords, cur, '*', 'restaurant', wherea = region)
        print((datetime.now() - t).seconds)
    return make_response(jsonify(ret), 200)
 
 
if __name__ == '__main__':
    t = datetime.now()
    g = Graph()
    con = sql.connect('localhost', 'test', 'test', 'restaurants')
    cur = con.cursor()
    print((datetime.now() - t). seconds)
    app.run(host="0.0.0.0", port="5000", debug=True)


