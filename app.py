from flask import Flask, request, render_template
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form.get('test_string')
    regex_pattern = request.form.get('regex_pattern')
    print(f'test_string:{test_string}')
    print(f'regex_pattern:{regex_pattern}')

    if not test_string or not regex_pattern:
        return render_template('index.html', message="Please provide both a test string and a regex pattern.")

    try:
        regex = re.compile(regex_pattern)
        matches = regex.findall(test_string)

        print(f"Matches: {matches}")

        if not matches:
            return render_template('index.html', message="No matches found.", matches=matches)

        return render_template('results.html', test_string=test_string, regex_pattern=regex_pattern, matches=matches)
    
    except re.error:
        return render_template('index.html', message="Invalid regular expression pattern.")

@app.route("/email-validation", methods=["GET", "POST"])
def email_validation():
    if request.method == "POST":
        email = request.form.get("email")
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(email_regex, email):
            result = "Valid Email"
        else:
            result = "Invalid Email"
        return render_template("email_validation.html", result=result)
    return render_template("email_validation.html")


if __name__ == '__main__':
    app.run(debug = True)