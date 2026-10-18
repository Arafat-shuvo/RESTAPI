from apiapp.models import StudentModel
from apiapp.serializers import StudentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def student_view(request):
    if request.method == 'GET':
        students = StudentModel.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response({
            'success': True,
            'message': 'Student data fetched successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'success': True,
            'message': 'Student data saved successfully',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    return Response({
        'success': False,
        'message': 'Student data not saved',
        'data': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def student_details(request, student_id):
    try:
        student = StudentModel.objects.get(id=student_id)
    except StudentModel.DoesNotExist:
        return Response({
            'success': False,
            'message': 'Student data not found',
            'data': {}
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response({
            'success': True,
            'message': 'Student data fetched successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'success': True,
            'message': 'Student data updated successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    return Response({
        'success': False,
        'message': 'Student data not updated',
        'data': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)
