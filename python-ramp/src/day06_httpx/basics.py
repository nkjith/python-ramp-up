"""
HTTPX is a fully featured HTTP client for Python 3, which provides sync and async APIs,
"""

import httpx

print("\n\nMaking requests\n\n")
r = httpx.get("https://jsonplaceholder.typicode.com/posts/1")
# .text is the raw body, .json() parses it.
print(f"status code - {r.status_code} \nresponse text - {r.text} \nresponse json - {r.json()}")

# POST 
print("\n\nMaking POST requests\n\n")

r = httpx.post('https://httpbin.org/post', data={'key': 'value'})
print(f"status code - {r.status_code} \nresponse text - {r.text} \nresponse json - {r.json()}")


# If we do this plainly, Every call to httpx.get() opens a new TCP connection, 
# does a TLS handshake, sends the request, and closes it. 
# That handshake costs real time — often more than the request itself

# A Client keeps connections open and reuses them

with httpx.Client() as client:
    # Three requests, one connection
    r1 = client.get("https://jsonplaceholder.typicode.com/posts/1")
    r2 = client.get("https://jsonplaceholder.typicode.com/posts/2")
    r3 = client.get("https://jsonplaceholder.typicode.com/posts/3")

    print(r2.status_code)

# timeouts
url = "https://jsonplaceholder.typicode.com/posts/1"
with httpx.Client(timeout=10.0) as client:
    response = client.get(url)

# finer controls
timeout = httpx.Timeout(
    connect=5.0,    # establishing the connection
    read=30.0,      # waiting for the response body
    write=5.0,
    pool=5.0,
)
with httpx.Client(timeout=timeout) as client:
    ...

# catching a timeout
with httpx.Client(timeout=10.0) as client:
    try:
        response = client.get(url=url)
    except httpx.TimeoutException as e:
        print(f'timed out {e}')

# raise_for_status() — turns a 4xx/5xx into an exception instead of silently returning an error page
# if no exception, continue

"""
Two different failure kinds. HTTPStatusError — the server responded, with an error. 
RequestError — you never reached the server (DNS failure, connection refused, timeout). 
"""

new_client = httpx.Client(timeout=1.0)

try:
    response = new_client.get(url=url)
    response.raise_for_status()
except httpx.HTTPStatusError as status_err:
    print(f"status error : {status_err.response.status_code}")
except httpx.RequestError as e :
    print(f"network problem: {e}")
except TimeoutError as time_err:
    print(f'timed out {time_err}')
finally:
    new_client.close() # if we use with, there is no need to explicitly close as httpx.Client() is context manager protocol

print("\n\nHere we are\n\n")

