from flask import Flask, render_template, Blueprint, url_for, request, redirect
from flask_login import login_required, current_user
from . import symptomsuggestion as symp

main = Blueprint("health_main", __name__)

found_symptoms = list()
dict_symp_tup = list()
final_symp = list()
topk_index_mapping = dict()
diseases = list()

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/health')
@login_required
def health():
    ph = "List all your symptoms with comma(',')-separated"
    value = None
    return render_template("health.html", name=current_user.name, value=value, ph=ph, site="health1")

@main.route('/health1', methods=['POST'])
@login_required
def health1():
    
    symptoms = request.form.get('symptoms')

    global found_symptoms
    value, found_symptoms = symp.take_input(symptoms)
    ph = "Please select the relevant symptoms. Enter indices (separated-space)"

    return render_template("health.html", name=current_user.name, value=value, ph=ph, site="health2")

@main.route('/health2', methods=['POST'])
@login_required
def health2():
    
    symptoms = request.form.get('symptoms')

    global dict_symp_tup
    global final_symp
    global found_symptoms
    value, dict_symp_tup, final_symp = symp.co_occur(symptoms, found_symptoms)
    ph = "Do you have have of these symptoms? If Yes, enter the indices (space-separated), 'no' to stop, '-1' to skip"

    return render_template("health.html", name=current_user.name, value=value, ph=ph, site="health3")

@main.route('/health3', methods=['POST'])
@login_required
def health3():
    
    symptoms = request.form.get('symptoms')

    global topk_index_mapping
    global diseases
    global dict_symp_tup
    global final_symp
    value, topk_index_mapping, diseases = symp.final_pred(symptoms, dict_symp_tup, final_symp)
    ph = "More details about the disease? Enter index of disease or '-1' to discontinue and close the system"

    return render_template("health.html", name=current_user.name, value=value, ph=ph, site="health4")

@main.route('/health4', methods=['POST'])
@login_required
def health4():
    
    symptoms = request.form.get('symptoms')

    global topk_index_mapping
    global diseases
    value = symp.more_dat(symptoms, topk_index_mapping, diseases)
    ph = ""

    return render_template("health.html", name=current_user.name, value=value, ph=ph)
