import requests
import concurrent
import asyncio
import aiohttp

class request_master():
	def __init__(self):
		pass  
	def sync_request_one(self,method,url,headers=""):
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
						self.request_one,
						method,
						urls[i],
					)
					for i in range(length)
				]
				response_list = []
				for response in await asyncio.gather(*futures):
					response_list.append(response)
				return response_list
		if type(urls) != list:raise Exception("request_many works only with lists if u want to request one time use request_one")
		loop = asyncio.get_event_loop()
		result = loop.run_until_complete(request(loop,urls,len(urls)))			
		return result
 
