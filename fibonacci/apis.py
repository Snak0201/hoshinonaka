from rest_framework.views import APIView
from rest_framework.response import Response

class FibonacciAPIView(APIView):
    def get_fibonacci_number(self, n):
        """FIXME: この方法は遅い"""
        if n == 0 or n == 1:
            return n
        return self.get_fibonacci_number(n - 1) + self.get_fibonacci_number(n - 2)
    
    def get(self, request):
        try:
            n = int(request.GET.get("n"))
            print(n)
        except ValueError:
            """
            n が整数でないとき、フィボナッチ数列の定義外
            """
            return Response({"status":400, "message":"Request is not integer."}, status=400)
        
        if n < 0:
            """
            n が負のとき、フィボナッチ数列の定義外
            """
            return Response({"status":400, "message":"Request is not positive integer."}, status=400)
        
        fn = self.get_fibonacci_number(n)
        return Response({"result": fn}, status=200)
    
    def post(self, request):
        """POSTリクエストは許されない"""
        return Response({"status":405, "message":"Method Not Allowed."}, status=405)
