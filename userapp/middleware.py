

class CustomMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print(f"Incoming request: {request.method} {request.path}")
        response=self.get_response(request)
        print(f"Outgoing response: {response.status_code}")
        return response
    


