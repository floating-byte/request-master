import requests
import concurrent
import asyncio
import aiohttp

class request_master():
	def __init__(self):
		pass  
	def sync_request_one(self,method,url,headers=""):
		if type(url) != str:raise Exception("sync_request_one works only with lists if u want to request one time use sync_request_many()") 
		if headers != "":response = requests.request(method,url,headers=headers)
		else:            response = requests.request(method,url)
		return response
	def sync_request_many(self,method,urls:list,workers=10):
		async def request(loop,urls,length):
			with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
				futures = [
					loop.run_in_executor
					(
						executor, 
						self.sync_request_one,
						method,
						urls[i],
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
	async def async_request(self,method,url):
			async with aiohttp.ClientSession() as session:
				async with session.request(method,url) as resp:
					status_code = resp.status
					response = await resp.text()
					return {"status":status_code,"content":response}
	def async_request_one(self,method,url):
		if type(url) != str:raise Exception("async_request_one works only with lists if u want to request one time use async_request_many()") 
		loop = asyncio.get_event_loop()
		return loop.run_until_complete(self.async_request(method,url))
	def async_request_many(self,method,urls:list):
		async def task_collector():
			tasks = []
			for i in urls:
				tasks.append(asyncio.create_task(self.async_request(method,i)))
			return await asyncio.gather(*tasks)
		if type(urls) != list:raise Exception("async_request_many works only with lists if u want to request one time use async_request_one()")
		loop = asyncio.get_event_loop()
		return loop.run_until_complete(task_collector())
