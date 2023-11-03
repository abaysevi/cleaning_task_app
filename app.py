from flask import Flask, render_template, request, url_for,redirect
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime,timedelta
from datetime import datetime
from dateutil import parser


app = Flask(__name__)

# Configure MongoDB connection
client = MongoClient('mongodb+srv://abaysevi:2012123958@cluster0.klirftq.mongodb.net/?retryWrites=true&w=majority')
db = client['cleaningtaks_app']
res_collection = db['res_data']
cleaining_tasks_collection=db["cleaning-tasks"]


@app.route('/add_res', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_dict = request.form.to_dict()
        restaurant_data = {
            "name": form_dict['name'],
            "location": form_dict['location']
        }

        cleaning_data = []
        for key, value in form_dict.items():
            if key.startswith("cleaning_"):
                cleaning_area = key.replace("cleaning_", "")
                cleaning_data.append({
                    "cleaning_area": cleaning_area,
                    "frequency": value,
                    "last_cleaned": datetime.utcnow(),
                })

        # Insert into restaurant_collection
        restaurant_id = res_collection.insert_one(restaurant_data).inserted_id

        # Insert into cleaning_tasks_collection
        for task in cleaning_data:
            task["restaurant_id"] = restaurant_id
            cleaining_tasks_collection.insert_one(task)

        return redirect(url_for('success'))
    
    return render_template("add_res.html")

@app.route('/success')
def success():
    return render_template("res_added.html")

@app.route('/select_restaurant', methods=['GET'])
def select_restaurant():
    restaurant_names = [restaurant['name'] for restaurant in res_collection.find({}, {'name': 1})]
    return render_template('select_res.html', restaurant_names=restaurant_names)


# @app.route('/process_selected_restaurant', methods=['POST'])
# def process_selected_restaurant():
#     selected_restaurant = request.form['restaurant']
#     # Do something with the selected restaurant, like displaying details or processing it further
#     return f'Selected Restaurant: {selected_restaurant}'

@app.route('/cleaning_tasks', methods=['GET',"POST"])
def cleaning_tasks():
    # Get the current date and format it
    current_date = datetime.now()
    formatted_date = current_date.strftime("%B %d %A %Y")
    selected_restaurant = request.form['restaurant']
    print(selected_restaurant)
    restaurant_document_id = res_collection.find_one({"name": selected_restaurant})["_id"]
    cleaning_data=[cleaning_areas  for cleaning_areas in cleaining_tasks_collection.find({"restaurant_id":restaurant_document_id})]
    formatted_cleaning_data = []
    for task in cleaning_data:
        # last_cleaned_timestamp = task['last_cleaned']['$date']['$numberLong'] / 1000  # Convert to seconds
        last_cleaned_date = task['last_cleaned']
        if task["frequency"]=="Daily":
            next_cleaning_date = last_cleaned_date + timedelta(days=1)  # Replace with the actual calculation
        if task["frequency"]=="Monthly":
            next_cleaning_date = last_cleaned_date + timedelta(days=30)  # Replace with the actual calculation
        if task["frequency"]=="Weekly":
            next_cleaning_date = last_cleaned_date + timedelta(days=7)  # Replace with the actual calculation
        if task["frequency"]=="Every 2 Days":
            next_cleaning_date = last_cleaned_date + timedelta(days=2)  # Replace with the actual calculation
 
        days_remaining = (next_cleaning_date - current_date).days
        formatted_cleaning_data.append({
            "area": task["cleaning_area"],
            "frequency": task["frequency"],
            "last_cleaned_date": last_cleaned_date.strftime("%B %d %Y"),
            "next_cleaning_date": next_cleaning_date.strftime("%B %d %Y"),
            "days_remaining": days_remaining,
        })

    return render_template("cleaning_tasks.html", today=current_date, restaurant_name=selected_restaurant, cleaning_data=formatted_cleaning_data)



@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
