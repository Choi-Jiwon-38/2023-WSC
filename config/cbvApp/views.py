from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIVieew           # APIView import
from fbvApp.models import Student                   # 이전에 만든 Student 모델 재사용
from fbvApp.serializers import StudentSerializer    # 이전에 만든 StudentSerializer 재사용

# StudentList
class StudentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many='True')
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data) # request.data = id= '1', name='hong', score = '80.000'
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# StudentDetail
class StudnetDetail(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        student = self.get_object(pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk=pk)
        serializer = StudentSerializer(student, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student =self.get_object(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)