# Sync Requesting:

<code>
   	import request_master as rm
</code>

1. ### sync_request_one(method,url,headers="")

    **method (str):            [get, post , head, ...].**
    <br>
    **url    (str):             page url.**
    <br>
    **headers (str)[optional]: request headers.**
    * use this to request one web page.
    * return a request obj 
	<code>
	response = rm.sync_request_one("get","http://example.com")
	</code>

2. ### sync_request_many(method,urls:list,headers="",workers=10)
<code>
	urls = ["http://example.com","http://example.com","http://example.com","http://example.com","http://example.com"]
</code>
    <br>
<code>
   	response = rm.sync_request_one("get",urls,workers=20)
</code>
    <br>
    **urls (list): list of urls**
    **[more about Threading](https://realpython.com/intro-to-python-threading/)**
    * this def uses Threading , use this to send more then a request.
    * more workers , more cpu power ,faster responses.     

# Async Requesting:
1. ### async_request_one(method,url,headers="",content=True)
<code>
   	response = rm.sync_request_one("get","http://example.com")  	
</code>
    <br>
    **method (str):            [get, post , head, ...].**
    **url    (str):             page url.**
    **headers (str)[optional]: request headers.**
    * if content == False : return a aihttp obj
    * if content == True : return a json ```{"status":xxx,"content":page html}```
2.  ### content(response)
<code>
   	response = rm.sync_request_one("get","http://example.com",content=False)  	
</code>
    <br>    
<code>
   	content = rm.content(response)  	
</code>
    <br>
    **response (aihttp response obj): response**
    * if u have response as aihttp obj this will return the content of the page
3. ### async_request_many(method,urls:list,headers="",content=True)
<code>
   	urls = ["http://example.com","http://example.com","http://example.com","http://example.com","http://example.com"]
</code>
    <br>
<code>
   	response = rm.async_request_many("get",urls)  	
</code>
    <br>    
    **urls (list): list of urls**
    **[more about asyncio](https://docs.python.org/3/library/asyncio-task.html)**
    * faster responses
    * uses the asyncio methods and retrun response
