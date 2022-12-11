import os
from flask_mysqldb import MySQL
from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
mysql = MySQL(app)


app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "bj531park"
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_DB'] = "python"



@app.route('/', methods=['GET', 'POST'])
def visit():
    if request.method == 'GET':
        
        # MySQL 서버에 접속하기
        cur = mysql.connection.cursor()
        
        # MySQL 명령어 실행하기
        cur.execute("SELECT * FROM food_keyword")
        cur.execute("SELECT * FROM food_db")
        
        # 전체 row 가져오기
        res = cur.fetchall()
        
        # Flask에서 제공하는 json변환 함수
        return jsonify(res)
    
    if request.method == 'POST':
        
        #json 변환할 변수들

        #String
        keyword = request.json['keyword']
        region = request.json['region']


        #boolean(TINYINT)
        index = request.json['index']
        adress = request.json['adress']
        place_name = request.json['place_name']
        place_url = request.json['place_url']
        road_adress_name = request.json['road_adress_name']
        x = request.json['x']
        y = request.json['y']
        
        # mysql 접속 후 cursor 생성하기
        cur = mysql.connection.cursor()
        
        # DB 데이터 삽입하기 
        cur.execute("INSERT INTO food_keyword (keyword) VALUES(%s)", [keyword])
        cur.execute("INSERT INTO food_keyword (region) VALUES(%s)", [region])
        cur.execute("INSERT INTO food_db ([index],[adress],[place_name],[place_url],[road_adress_name],[x],[y]) VALUES([%TINYINT],[%TINYINT],[%TINYINT],[%TINYINT],[%TINYINT],[%TINYINT],[%TINYINT])", [index],[adress],[place_name],[place_url],[road_adress_name],[x],[y])

        # boollist로 하나로 묶기
        cur.execute("SELECT GROUP_CONCAT(index,adress,place_name,road_adress_name,x,y) as bool_list FROM food_db")

        # DB에 수정사항 반영하기
        mysql.connection.commit()
        
        # mysql cursor 종료하기
        cur.close()
        
        return 


if __name__ == '__main__':
    app.run(debug=True) #코드 수정 시 자동 반영


    
