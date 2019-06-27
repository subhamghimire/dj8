from django.urls import path
from dj8_app import views
#template url
app_name = 'dj8_app'

urlpatterns=[
    path('',views.SchoolListView.as_view(),name='list'),
    path('<int:pk>/',views.SchoolDetailView.as_view(),name='detail'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    path('<int:pk>/update/',views.SchoolUpdateView.as_view(),name='update'),
    path('<int:pk>/delete/',views.SchoolDeleteView.as_view(),name='delete')
]
