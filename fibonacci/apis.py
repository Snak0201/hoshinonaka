from rest_framework.views import APIView
from rest_framework.response import Response

class FibonacciAPIView(APIView):
    def get_fibonacci_number(self, n):
        if n <= 1:
            return n
        return self.get_fibonacci_number(n-1)+self.get_fibonacci_number(n-2)
    
    def get(self, request):
        n = int(request.GET.get("n"))
        fn = self.get_fibonacci_number(n)
        return Response({"result":fn}, status=200)
    
    def post(self, request):
        """POSTリクエストは許されない"""
        return Response({"status":405, "message":"Method Not Allowed."}, status=405)
