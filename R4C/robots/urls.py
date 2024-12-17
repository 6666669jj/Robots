from django.urls import path

from robots.views import AddRobotView, RobotsExcelView

urlpatterns = [
    path('add_robot/', AddRobotView.as_view(), name='add_robot'),
    path('robots_to_xl/', RobotsExcelView.as_view(), name='to_xl'),

]
