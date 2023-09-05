from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('notes/',views.notes,name='notes'),
    path('delete_notes/<int:pk>',views.delete_notes,name='delete_notes'),
    path('detail_notes/<int:pk>',views.details_notes,name='details_notes'),
    path('homework/',views.homework,name='homework'),
    path('homework/<int:pk>',views.homework_update,name='homework_update'),
    path('delete-homework/<int:pk>',views.delete_homework,name='delete_homework'),
    path('youtube/',views.youtube,name='youtube'),
    path('todo/',views.todo,name='todo'),
    path('todo_update/<int:pk>/',views.todo_update,name='todo_update'),
    path('todo_delete/<int:pk>/',views.todo_delete,name='todo_delete'),
    path('books/',views.books,name='books')
]