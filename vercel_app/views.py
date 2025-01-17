from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

class LoginAPI(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Username and password are required."}, status=HTTP_400_BAD_REQUEST)

        user, created = User.objects.get_or_create(username=username)

        if created:
            user.set_password(password)  # Correct way to set password
            user.save()
            return Response({"message": "User created successfully."}, status=HTTP_201_CREATED)

        # Optional: Check password if user already exists
        if not user.check_password(password):
            return Response({"error": "Invalid credentials."}, status=HTTP_400_BAD_REQUEST)

        return Response({"message": "Login successful."}, status=HTTP_200_OK)
