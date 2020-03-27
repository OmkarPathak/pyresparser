### Dependencies
from flask import Flask, request, jsonify
import traceback
import pandas as pd
import numpy as np
import json
from utils import *
import requests

# Your API definition
app = Flask(__name__)

@app.route('/fit_score', methods=['POST'])
def fit_score():
    try:
        resume_url = request.form['url']
        JD = request.form['JD']
        #print(JD)
        print(resume_url)
        JD = JD.replace("\\","")
        #print('\n\n\n',JD)
        JD_dataframe = pd.read_json(JD)
        
        scores, report = get_results(resume_url, JD_dataframe)

        
##        b_data = request.data
##        b_data = b_data.decode()
##        print(b_data)
##        data = b_data.split('\n')
##        
##        a, b = data[0], data[1]
##        a = a.replace("\\","")
##        b = b.replace("\\","")
##        print(a)
##        print('\n\n\n')
##        print(b)
##        a = a[2:len(a)-2]
##        b = b[1:len(b)-2]
##        print(a)

        
##        print(b)
##        with open('JD_data.json', 'w') as f:
##            f.write(b)
##        jd = open('JD_data.json')
        #print(json.loads(b))
##          a = a[2:len(a)-2]
##        b = b[1:len(b)-2]

##        candidate_dataframe = pd.read_json(a)
        #JD_dataframe = pd.read_json(b)
        #resume_url = a
##
##        flag = 0
##        try:
        #scores, report = get_results(resume_url, JD_dataframe)
##            print(scores,'\n\n\n',report)
##
##        except:
##            flag = 1
##
##        if flag == 0:
        return jsonify({'Results': scores, 'Report': report})
        #return jsonify({'url': url, 'JD': JD})
##        else:
##            return jsonify({'Error': str(flag})
##
    except:

        return jsonify({'trace': traceback.format_exc()})
    
if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345

    
    app.run(port=port, debug=True)

