from flask import Blueprint, render_template, request
import requests

lookup_bp = Blueprint('lookup', __name__)

@lookup_bp.route('/lookup', methods=['GET', 'POST'])
def lookup():
    result = None
    if request.method == 'POST':
        q = request.form['query'].strip()
        params = {
            'action': 'DownBoatRMS',
            'SailNo': q,
            'ext': 'json'
        }
        url = "https://data.orc.org/public/WPub.dll"
        resp = requests.get(url, params=params, timeout=10)
        if resp.ok:
            data = resp.json()
            if data:
                result = data[0]  # take first match
    return render_template('lookup.html', result=result, query=q if request.method=='POST' else '')
