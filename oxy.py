from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    global data
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            #print(data["name"], data["email"])
            write_to_csv(data)
            return 'Thanks for submitting!!'

        except:
            return 'Your data was not saved to database!!!'

    else:
        return 'Something Went Wrong!!!'




def write_to_csv(data):
    with open('./database.csv','a', newline='') as dbfile2:
        name=data["name"]
        email= data["email"]
        dist= data["dist"]
        location= data["location"]
        csvWriter = csv.writer(dbfile2, delimiter=',',
                            quotechar='|' ,quoting=csv.QUOTE_MINIMAL)
        csvWriter.writerow([name,email,dist,location])


if __name__ == '__main__':
    app.run()