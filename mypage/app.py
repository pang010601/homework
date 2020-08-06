from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    # title_receive로 클라이언트가 준 title 가져오기
    name_receive = request.form['name_give']
    # author_receive로 클라이언트가 준 author 가져오기
    number_receive = request.form['number_give']
    # review_receive로 클라이언트가 준 review 가져오기
    address_receive = request.form['address_give']
    # review_receive로 클라이언트가 준 review 가져오기
    phone_receive = request.form['phone_give']

    ord = {
        'name': name_receive,
        'number': number_receive,
        'address': address_receive,
        'phone': phone_receive
    }
    # reviews에 review 저장하기
    db.orders.insert_one(ord)

    return jsonify({'result': 'success', 'msg': '주문이 정상적으로 완료되었습니다. 감사합니다'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    # 1. DB에서 리뷰 정보 모두 가져오기
    orders = list(db.orders.find({}, {'_id':0}))
    # 여길 채워나가세요!
    return jsonify({'result': 'success', 'orders': orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
