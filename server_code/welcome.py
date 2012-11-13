from bottle import route, run, request, get, post
import smtplib
import sys
import string
import json

@route('/hello/', method=['POST','GET'])
def index():
    reqstr = request.POST.get('jqGridData')    
    reqstring = json.loads(reqstr)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login('prasadkpai@gmail.com','Casual10')
    server.sendmail('prasadkpai@gmail.com', 'kppai85@gmail.com', str(reqstr))
    server.quit()
    print str(reqstr)
    return "%s" % (reqstr)


run(host='192.168.1.145', port=8080)
