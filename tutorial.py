import request_master as rm
from pprint import pprint 
url = "http://example.com"
urls = [url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url,url]


def sync_request_one():
	response = rm.sync_request_one("get",url)
	pprint(response)
	print("the type is",type(response))


def sync_request_many():
	responses = rm.sync_request_many("get",urls)
	pprint(responses)
	print("the type is",type(responses))

def async_request_one_content():
	response = rm.async_request_one("get",url)
	pprint(response)
	print("the type is",type(response))

def async_request_one_no_content():
	response = rm.async_request_one("get",url,content=False)
	pprint(response)
	print("the type is",type(response))



def	async_request_many_content():
	responses = rm.async_request_many("get",urls)
	pprint(responses)	
	print("the type is",type(responses))

def	async_request_many_no_content():
	responses = rm.async_request_many("get",urls,content= False)
	pprint(responses)
	print("the type is",type(responses))

#sync_request_one()
#sync_request_many()

#async_request_one_content()

#async_request_one_no_content()

#async_request_many_no_content()
async_request_many_content()
