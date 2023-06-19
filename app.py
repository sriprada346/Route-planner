from flask import Flask, render_template,request
from dijkstra import my_function

app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def index():
    return render_template("index.html")

"""@app.route("/")
def index():
    return render_template("index.html")"""

@app.route("/mainpage",methods=['POST','GET'])
def ndex():
    return render_template("mainpage.html")



@app.route('/submit', methods=['POST'])
def submit():
    
    source = request.form['drop_source']
    destination = request.form['drop_destination']
    graphs = {
    'bank': {'maingate':2,'mech':5,'temple':2,'apj':1},
    'canteen': {'vishweshwarayya':2,'mech':1,'polytechnic':1},
    'cvraman': {'ramanujan':3,'apj':3,'vishweshwarayya':3,'mech':2},
    'ramanujan': {'temple':2,'polytechnic':3,'cops':3,'canteen':2,'cvraman':3,'apj':1},
    'sanmathi':{'sadananda':8,'bcalva':4},
    'busstand':{'mech':1,'maingate':7},
    'sadananda':{'sanmathi':8,'bcalva':10,'atal':2,'polytechnic':2},
    'temple':{'maingate':3,'bank':2,'apj':1,'ramanujan':2,'polytechnic':4},
    'bcalva':{'atal':9,'sadananda':10,'sanmathi':4,'canteen':10},
    'maingate':{'busstand':7,'temple':3,'bank':1},
    'apj':{'temple':2,'bank':1,'ramanujan':1,'cvraman':3},
    'atal':{'bcalva':3,'sadananda':2,'cops':2},
    'cops':{'atal':2,'canteen':3,'ramanujan':3,'polytechnic':3},
    'vishweshwarayya':{'canteen':2,'cvraman':2,'mech':1},
    'mech':{'vishweshwarayya':1,'bank':5,'cvraman':3,'busstand':1},
    'polytechnic':{'sadananda':2,'cops':3,'ramanujan':3,'temple':4}


    }

    start = source
    end = destination




    #result = my_function(graphs,source,destination)
    result = my_function(graphs,start,end)
    return render_template('output.html',result=result) 
    #return(result)
    


if __name__ == "__main__":
    app.run(debug=True)