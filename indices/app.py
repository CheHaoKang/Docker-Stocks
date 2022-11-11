from flask import Flask
import json
import pymysql
import sys

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/indices/<string:stock_name>/<int:limit>')
def get_indices(stock_name, limit):
    try:
        with open('cred.json') as json_file:
            cred = json.load(json_file)
        print(cred)
        conn = pymysql.connect(host=cred['mysql']['ip'], port=cred['mysql']['port'], user=cred['mysql']['username'], passwd=cred['mysql']['password'], db=cred['mysql']['database'], charset="utf8")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    except:
        sys.exit("Error: unable to create database connection.")

    select_stock_id_sql = 'SELECT id FROM stock_list WHERE stock_name = %s'
    cursor.execute(select_stock_id_sql, (stock_name))
    stock_id = cursor.fetchone()
    if stock_id and 'id' in stock_id:
        stock_id = stock_id['id']
    else:
        return 'Invalid stock_name'

    cursor.execute('''
        SELECT      stock_id, date, `index`
        FROM        index_volume
        WHERE       stock_id = {}
        ORDER BY    date DESC
        LIMIT       {}
    '''.format(conn.escape(stock_id), conn.escape(limit)))

    results = cursor.fetchall()
    json_data = []
    for result in results:
        json_data.append(dict(result))

    cursor.close()

    return json.dumps(json_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')