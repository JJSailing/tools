from flask import Blueprint, render_template, request

gennaker_bp = Blueprint('gennaker', __name__)

@gennaker_bp.route('/gennaker', methods=['GET', 'POST'])
def gennaker():
    area = None
    if request.method == 'POST':
        try:
            SLU = float(request.form['SLU'])  # luff
            SLE = float(request.form['SLE'])  # leech
            SHW = float(request.form['SHW'])  # half-width
            SFL = float(request.form['SFL'])  # foot

            ASL = (SLU + SLE) / 2
            area = round(ASL * (SFL + 4 * SHW) / 6, 2)
        except ValueError:
            area = "Invalid input"
    return render_template('gennaker.html', area=area)
