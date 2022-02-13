#Credits:GFG
# Import dependencies
from subprocess import Popen, PIPE
import requests
import webbrowser


def execute_return(cmd):
	args = cmd.split()
	proc = Popen(args, stdout=PIPE, stderr=PIPE)
	out, err = proc.communicate()
	return out, err


def mak_req(error):
	resp = requests.get("https://api.stackexchange.com/" +
						"/2.2/search?order=desc&tagged=python&sort=activity&intitle={}&site=stackoverflow".format(error))
	return resp.json()

def get_urls(json_dict):
	url_list = []
	count = 0
	
	for i in json_dict['items']:
		if i['is_answered']:
			url_list.append(i["link"])
		count += 1
		if count == 3 or count == len(i):
			break
	
	for i in url_list:
		webbrowser.open(i)


out, err = execute_return("python C:/Users/Piyush/Desktop/test.py")

error = err.decode("utf-8").strip().split("\r\n")[-1]
print(error)


# A simple if condition, if error is found then execute 2nd and
# 3rd function, otherwise print "No error".
if error:
	filter_error = error.split(":")
	json1 = mak_req(filter_error[0])
	json2 = mak_req(filter_error[1])
	json = mak_req(error)
	get_urls(json1)
	get_urls(json2)
	get_urls(json)
	
else:
	print("No error")
