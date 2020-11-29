from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd


app = Flask(__name__)

data_df = pd.read_csv("Resources/cities.csv")


@app.route('/', methods=("POST", "GET"))
def html_table():

    return render_template('data_page.html',  tables=[data_df.to_html(classes='data')], titles=data_df.columns.values)



if __name__ == '__main__':
    app.run(debug=True)