from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sailarea', methods=['GET', 'POST'])
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
            area = "Invalid input. Please use numbers."
    return render_template('sailarea.html', area=area)

@app.route('/spinnaker', methods=['GET', 'POST'])
def spinnaker():
    area = None
    if request.method == 'POST':
        try:
            SLU = float(request.form['SLU'])
            SLE = float(request.form['SLE'])
            SHW = float(request.form['SHW'])
            SFL = float(request.form['SFL'])
            ASL = (SLU + SLE) / 2
            area = round(ASL * (SFL + 4 * SHW) / 6, 2)
        except ValueError:
            area = "Invalid input"
    return render_template('spinnaker.html', area=area)


if __name__ == '__main__':
    import os
port = int(os.environ.get("PORT", 5000))
app.run(debug=False, host='0.0.0.0', port=port)

