from config import vuln_app
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ui/')
def ui():
    return render_template('index.html')
'''
 Decide if you want to server a vulnerable version or not!
 DO NOTE: some functionalities will still be vulnerable even if the value is set to 0
          as it is a matter of bad practice. Such an example is the debug endpoint.
'''
vuln = int(os.getenv('vulnerable', 1))
# vuln=1
# token alive for how many seconds?
alive = int(os.getenv('tokentimetolive', 60))


# start the app with port 5001 and debug on!
if __name__ == '__main__':
    vuln_app.run(host='0.0.0.0', port=5001, debug=True)
