from flask import Flask, render_template
import csv
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html") # You can have a homepage if needed. for now directed to career_timeline

@app.route("/timeline")
def career_timeline():
    csv_path = r"C:\Users\Fawaz\Documents\GitHub\workexp\workexp.csv"
    work_experiences = []
    with open(csv_path, newline="", encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            work_experiences.append(row)
    return render_template("timeline.html", work_experiences=work_experiences)

if __name__ == "__main__":
    app.run(debug=True)
