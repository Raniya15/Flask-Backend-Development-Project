*Regex Web App*

A web application built using Flask to simplify regular expression (regex) testing and pattern matching. This app helps users test and visualize regex patterns against any given input, providing a clear understanding of the matched and unmatched parts of the text.

* Features
1. Real-time Regex Testing: Enter regex patterns and see matches in real time.
2. User-Friendly Interface: Simple and intuitive UI for beginners and advanced users.
3. Highlighting of Matched Text: Visual representation of matches found in the input.
4. Flask Backend: Built using Python Flask to handle regex logic and routing.

* Installation
To run this project locally, follow these steps:

Prerequisites
1. Python 3.x
2. Flask

Step-by-step Guide

1. Clone the repository:

git clone https://github.com/your-username/regex-web-app.git
cd regex-web-app

2. Create a virtual environment:

python3 -m venv env
source env/bin/activate  or For Windows  env\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt

4. Run the Flask app:
   
python app.py

* Usage
1. Input the string you want to test against in the text area.
2. Enter your regex pattern in the provided field.
3. The app will highlight the matches and provide additional details on captured groups and regex syntax errors if present.
   
* Example:
Input: Hello, World!
Pattern: [A-Za-z]+
Matches: Hello, World
