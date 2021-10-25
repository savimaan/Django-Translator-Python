import request
data=request.get("https://reqres.in/api/users")
print(data.text)