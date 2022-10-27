from flask import Flask
from flask_cors import CORS
import pymysql
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})



@app.route("/hello")
def hello():
    result = {
        host = "mysql-svc"
        user = "root"
        password = "qwer1234"
        db = "lth_db"
        corn = pymysql.connect(host=host, user=user, db=db, password=password, charset='utf8')
        curs = corn.cursor()
        sql = "select * from student";
        curs.execute(sql)
        rows = curs.fetchall()
        print(rows)
        corn.commit()
        corn.close()

    }

    return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)
