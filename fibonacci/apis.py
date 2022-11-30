from rest_framework.response import Response
from rest_framework.views import APIView


class FibonacciAPIView(APIView):
    def get_fibonacci_number(self, n):
        """
        フィボナッチ数を返す関数
        
        Parameter
        -----
        n: int
            何番目のフィボナッチ数を返すか
        
        Return
        -----
        f: int
            n 番目のフィボナッチ数列
                
        """
        
        # フィボナッチ数列の初項は0
        if n == 1:
            return 1
        
        # 2項め以降は以下のプログラム
        f_1, f = 1, 1
        for _ in range(n-2):
            f_1, f = f, f_1 + f
        
        return f
       

    def get(self, request):
        try:
            n = int(request.GET.get("n"))
        except (ValueError, TypeError):
            """
            n が整数でないとき、フィボナッチ数列の定義外
            （n が指定されていない場合も含む）
            """
            return Response(
                {"status": 400, "message": "Bad Request: n is not integer."}, status=400
            )

        if n <= 0:
            """
            n が0以下のとき、フィボナッチ数列の定義外
            """
            return Response(
                {"status": 400, "message": "Bad Request: n is not positive integer."},
                status=400,
            )

        ans = self.get_fibonacci_number(n)
        return Response({"result": ans}, status=200)

    def post(self, request):
        """POSTリクエストは許されない"""
        return Response({"status": 405, "message": "Method Not Allowed: POST request is not allowed."}, status=405)
