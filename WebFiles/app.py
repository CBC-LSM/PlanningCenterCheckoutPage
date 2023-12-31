from flask import Flask, render_template, jsonify
import requests
import simplejson
import json
from requests.auth import HTTPBasicAuth
import config
from datetime import date



app = Flask(__name__)


@app.route('/checkout')
def checkout():
    checkinData = {}
    checkinsuri = "https://api.planningcenteronline.com/check-ins/v2/check_ins?where[created_at]=" + date.today().strftime("%Y-%m-%d") + "&order=-checked_out_at&include=location&per_page=" + str(config.listLength)
    try:
        uResponse = requests.get(checkinsuri, auth = HTTPBasicAuth(config.APIUser, config.APIPass), headers={'X-PCO-API-Version': '2023-04-05'})
    except requests.ConnectionError:
        return "Connection Error"

    responseData = uResponse.json()['data']

    for i in responseData:
        if i['attributes']['checked_out_at'] is not None:
            if i['relationships']['locations']['data'][0]['id'] in config.locations:
                checkinData[i['id']] = {"checked_out_at": i['attributes']['checked_out_at'], "first_name": i['attributes']['first_name'], "last_name": i['attributes']['last_name']}

    return render_template('checkout.html', students=list(checkinData.values()))


if __name__ == "__main__":
    app.run(port=8005)
