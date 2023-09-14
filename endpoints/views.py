from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from endpoints.serializers import MaintenanceSerializer


class MaintenanceRequest(APIView):
    """
    As we are keeping this endpoints open we will not add any permission or
    authentication classes.
    And as to accept header thingy is not specified here, I would assume
    json response would be fine here
    """
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        try:
            request.data["MessageId"] = int(request.data["MessageId"]) + 1
            serializer = MaintenanceSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            return Response({"success": serializer.data})
        except Exception as e:
            print(e)
            return Response({'msg': f"the request could not be proceed. error: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class HundredsLongestLines(APIView):
#     """
#     As we are keeping this endpoints open we will not add any permission or
#     authentication classes.
#     And as to accept header thingy is not specified here, I would assume
#     json response would be fine here
#     """
#     permission_classes = []
#     authentication_classes = []
#
#     @staticmethod
#     def get(request):
#         try:
#             longest_100_lines = gxl(100)
#             if longest_100_lines:
#                 return Response(longest_100_lines)
#             return Response({'msg': NO_LINE_MSG})
#         except Exception as e:
#             print(e)
#             return Response({'msg': ERROR_MSG}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#
# class TwentyLongestLinesOfLastFile(APIView):
#     """
#     As we are keeping this endpoints open we will not add any permission or
#     authentication classes.
#     And as to accept header thingy is not specified here, I would assume
#     json response would be fine here
#     """
#     permission_classes = []
#     authentication_classes = []
#
#     @staticmethod
#     def get(request):
#         try:
#             twenty_lines = gxl(20)
#             if twenty_lines:
#                 return Response(twenty_lines)
#             return Response({'msg': NO_LINE_MSG})
#         except Exception as e:
#             print(e)
#             return Response({'msg': ERROR_MSG}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#
# one_random_line_backwards = OneRandomLineBackwards.as_view()
# twenty_longest_line_of_last_file = TwentyLongestLinesOfLastFile.as_view()
# hundreds_longest_line = HundredsLongestLines.as_view()