import csv
from flask import Flask
from flask import jsonify

# Data serialization is the process of converting structured data (return_list) to a format that allows sharing or storage of the data in a form that allows recovery of its original structure.
# JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write.
app = Flask(__name__)

@app.route('/state/<state>/<pop_sq_mile>')
def add_genus(state, pop_sq_mile):
    return_list = []
    with open("county_demographics.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["State"] == state:
                if float(row["Population.Population per Square Mile"]) > int(pop_sq_mile):
                    return_list.append(row)
    return jsonify(return_list)

# to get the error message on the url
if __name__ == '__main__':
    app.run(debug=True)