from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        name = request.form["name"]
        cgpa = float(request.form["cgpa"])
        aptitude = int(request.form["aptitude"])
        communication = int(request.form["communication"])
        internships = int(request.form["internships"])
        skills = request.form["skills"]

        # Placement Prediction
        if cgpa >= 7.0 and aptitude >= 70 and communication >= 70:
            placement_status = "Placed"

            result = """
Placed

Career Guidance:
✔ Apply for Software Developer Roles
✔ Practice Data Structures and Algorithms
✔ Build More Projects
✔ Improve Resume and LinkedIn Profile
"""
        else:
            placement_status = "Not Placed"

            result = """
Not Placed

Career Guidance:
✔ Improve Aptitude Skills
✔ Improve Communication Skills
✔ Complete Internships
✔ Practice Mock Interviews
"""

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="YOUR_PASSWORD"
            database="placement_db"
        )

        cursor = conn.cursor()

        query = """
        INSERT INTO students
        (name, cgpa, aptitude_score, communication_score,
         internships, placement_status, skills)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            name,
            cgpa,
            aptitude,
            communication,
            internships,
            placement_status,
            skills
        )

        cursor.execute(query, values)

        conn.commit()

        cursor.close()
        conn.close()

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)