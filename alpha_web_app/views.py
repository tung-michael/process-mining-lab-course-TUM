from flask import request, render_template, send_file
import os
from alpha_web_app.process_mining_alg.xes_importer import parseXes

from alpha_web_app.process_mining_alg.alphaAlg import Alpha_alg

from . import app


@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")


app.config["UPLOAD_FOLDER"] = "uploads"
app.config["RESULTS_FOLDER"] = "static/pm_output"


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":

        uploaded_file = request.files["filename"]
        if uploaded_file.filename != '':
            path = os.path.join(app.config["UPLOAD_FOLDER"], uploaded_file.filename)
            uploaded_file.save(path)
            print(uploaded_file.filename+" saved!")
            
            result_file = 'alpha_' + os.path.splitext(uploaded_file.filename)[0] # set name for result file
            full_result_name = os.path.join(app.config["RESULTS_FOLDER"], result_file)
            ptn = Alpha_alg(parseXes(path)).generate_petri_net() 
            ptn.render(full_result_name, format = 'pdf')
            ptn.render(full_result_name, format = 'png')
            
            return render_template("result-home.html", result_png = full_result_name + '.png', uploaded = uploaded_file.filename ,filename = result_file)
    return render_template("home.html")

@app.route('/download-result/<result_file>')
def download_result(result_file):
    filepath = app.config['RESULTS_FOLDER'] + "/" + result_file
    return send_file(filepath, as_attachment=True)
