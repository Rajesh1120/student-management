from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from student import serializer
from .serializer import StudentSerializer

@api_view(['POST'])
def add_student(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get(request):
    detailsObj=Student.objects.all()
    print(request)
    dlSerializeObj=StudentSerializer(detailsObj,many=True)
    return Response(dlSerializeObj.data)

@api_view(['PUT'])
def edit_student(request, roll_no):
    try:
        student = Student.objects.get(student_roll_no=roll_no)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_student(request,roll_no):
    try:
        student=Student.objects.get(student_roll_no=roll_no)
        print(student)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="DELETE":
        student.delete()
        return Response(data="successfully deleted",status=status.HTTP_200_OK)
    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            


