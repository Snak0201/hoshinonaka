from rest_framework.views import APIView
from rest_framework.response import Response

class FibonacciAPIView(APIView):
    def get_fibonacci_number(self, n):
        return n
    
    def get(self, request):
        return Response("OK", status=200)
    
    def post(self, request):
        return Response({"status":405, "message":"Method Not Allowed."}, status=405)
