from flask import Blueprint, render_template, request

mainsail_bp = Blueprint('mainsail', __name__)

@mainsail_bp.route('/sailarea', methods=['GET', 'POST'])
def sailarea():
    area = None
    if request.method == 'POST':
        try:
            P = float(request.form['P'])
            E = float(request.form['E'])
            MQW = float(request.form['MQW'])
            MHW = float(request.form['MHW'])
            MTW = float(request.form['MTW'])
            MUW = float(request.form['MUW'])
            MHB = float(request.form['MHB'])
            area = (P / 8) * (E + 2*MQW + 2*MHW + 1.5*MTW + MUW + 0.5*MHB)
            area = round(area, 2)
        except ValueError:
            area = "Invalid input"
    return render_template('sailarea.html', area=area)
