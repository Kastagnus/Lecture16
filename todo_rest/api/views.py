from rest_framework import generics, permissions
from .serializers import TodoSerializer
from todo.models import Todo
from .permissions import IsOwnerOnly
from rest_framework.permissions import IsAuthenticated


class TodoList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOnly, IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def filter_queryset(self, queryset):
        queryset = queryset.filter(user=self.request.user.id)
        return super().filter_queryset(queryset)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOnly, IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


