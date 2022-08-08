from adminapp.views import exam_list
from django.urls import path 
from .views import *



urlpatterns = [
    path('', home , name='student-home'),
    # path('upload_details/<int:id>/',upload_details,name ='upload_details'),
    path('StudentLogin/',StudentLogin,name='StudentLogin'),
    path('register/',register,name='register'),
    # path('subject_view/',subject_view,name='subject'),
    # path('views_score',views_score,name='student_views_score'),
]
'''path('exam-list', exam_list , name='student-exam-list'),
    path('answer-upload/<str:n>/', answer_upload , name='student-answer-upload'),'''