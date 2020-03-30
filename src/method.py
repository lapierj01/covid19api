import flask
import json
import loaddb as db
import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine('mssql+pyodbc://sa:pwd@192.168.1.2/covid19?driver=ODBC Driver 17 for SQL Server')

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#Initialize and Load Cases
db.initializeDB()
db.loadDB()
            
class DTOCases:
    number = 0
    Date = 0

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

#Define base route
@app.route('/', methods=['GET'])
def home():
    return "<h1>Covid-19 cases</h1><p>This API will list the covid-19 cases.</p>"


#Define Cases route
@app.route('/cases', methods=['GET'])
def cases():
    with engine.connect() as con:
        rs = con.execute('SELECT sum(cases) as nbCases, cast(max(convert(datetime, daterep,103)) as varchar) as lastDate FROM covid19cases')
        dtoOut = DTOCases()
        for row in rs:
            dtoOut.number = row['nbCases']
            dtoOut.Date = row['lastDate']
            print dtoOut.number

    return dtoOut.toJSON()


app.run(host='192.168.1.4', port=8080)

