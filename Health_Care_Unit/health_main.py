from flask import Flask, render_template, Blueprint, url_for, request, redirect
from flask_login import login_required, current_user
from . import symptomsuggestion as symp

main = Blueprint("health_main", __name__)
itr = 1
found_symptoms = list()
dict_symp_tup = list()
final_symp = list()
topk_index_mapping = dict()
diseases = list()

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/health', methods=['GET', 'POST'])
@login_required
def health():
    global itr
    ph = "List all your symptoms with comma(',')-separated"
    value = None
    if request.method == 'GET':
        itr = 1
    if request.method == 'POST':
        symptoms = request.form.get('symptoms')
        if itr == 1:
            itr += 1
            global found_symptoms
            value, found_symptoms = symp.take_input(symptoms)
            ph = "Please select the relevant symptoms. Enter indices (separated-space)"

        elif itr == 2:
            itr += 1
            global dict_symp_tup
            global final_symp
            value, dict_symp_tup, final_symp = symp.co_occur(symptoms, found_symptoms)
            ph = "Do you have have of these symptoms? If Yes, enter the indices (space-separated), 'no' to stop, '-1' to skip"

        elif itr == 3:
            itr += 1
            global topk_index_mapping
            global diseases
            value, topk_index_mapping, diseases = symp.final_pred(symptoms, dict_symp_tup, final_symp)
            ph = "More details about the disease? Enter index of disease or '-1' to discontinue and close the system"

        elif itr == 4:
            itr = 1
            value = symp.more_dat(symptoms, topk_index_mapping, diseases)
            ph = ""

    return render_template("health.html", name=current_user.name, value=value, ph=ph)


