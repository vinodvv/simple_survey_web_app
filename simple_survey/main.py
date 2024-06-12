from flask import Flask, render_template, request, redirect, url_for
import csv


app = Flask(__name__)


# Renders the survey from page
@app.route('/')
def home():
    return render_template('survey.html')


# Handles the submission of the survey form.
# Saves the data to a CSV file and redirects to the thank you page.
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        feedback = request.form['feedback']

        # Save the data to CSV file
        with open('survey_results.csv', 'a', newline='') as csvfile:
            fieldnames = ['Name', 'Email', 'Feedback']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header only if file is empty
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow({'Name': name, 'Email': email, 'Feedback': feedback})

        return redirect(url_for('thank_you'))


# Renders the thank you page after form submission.
@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')


if __name__ == "__main__":
    app.run(debug=True)
