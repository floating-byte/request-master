import requests
import concurrent
import asyncio
import aiohttp
 
def sync_request_one(method,url,headers=""):
	if type(url) != str:raise Exception("sync_request_one works only with lists if u want to request one time use sync_request_many()") 
	if headers != "":response = requests.request(method,url,headers=headers)
	else:            response = requests.request(method,url)
	return response
	
def sync_request_many(method,urls:list,workers=10,headers=""):
	async def request(loop,urls,length):
		with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
			futures = [
				loop.run_in_executor
				(
					executor, 
					sync_request_one,
					method,
					urls[i],
					headers
				)
				for i in range(length)
			]
			response_list = []
			for response in await asyncio.gather(*futures):
				response_list.append(response)
			return response_list
	if type(urls) != list:raise Exception("sync_request_many works only with lists if u want to request one time use sync_request_one()")
	loop = asyncio.get_event_loop()
	result = loop.run_until_complete(request(loop,urls,len(urls)))			
	return result

async def async_request(method,url,headers="",content=True):
		async with aiohttp.ClientSession() as session:
			if headers == "":
				headers = {}
			async with session.request(method,url,headers=headers) as resp:
				if content:
					status_code = resp.status
					response = await resp.read()
					return {"status":status_code,"content":response,"url":url}
				return resp
def content(response):
	async def get_content():
		return await response.read()
	loop = asyncio.get_event_loop()
	return loop.run_until_complete(get_content())	
def async_request_one(method,url,headers="",content=True):
	if type(url) != str:raise Exception("async_request_one works only with lists if u want to request one time use async_request_many()") 
	loop = asyncio.get_event_loop()
	return loop.run_until_complete(async_request(method,url,headers,content))
def async_request_many(method,urls:list,headers="",content=True):
	async def task_collector():
		tasks = []
		for i in urls:
			tasks.append(asyncio.create_task(async_request(method,i,headers,content)))
		return await asyncio.gather(*tasks)
		if type(urls) != list:raise Exception("async_request_many works only with lists if u want to request one time use async_request_one()")
	loop = asyncio.get_event_loop()
	return loop.run_until_complete(task_collector())
