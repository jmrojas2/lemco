from django.conf.urls import url
from django.contrib import admin
from dashboard import views as views_dashboard

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^dashboard/check', views_dashboard.check_number, name='dashboard_check_number'),
    #url(r'^dashboard/check', views_dashboard.check_number, name='dashboard_check_number'),
    url(r'^dashboard/file_check2/(\d+)/$', views_dashboard.file_check2, name='dashboard_file_check2'),
    url(r'^dashboard/file_check', views_dashboard.file_check, name='dashboard_file_check'),
    url(r'^dashboard/file_filter', views_dashboard.file_filter, name='dashboard_file_filter'),
    url(r'^dashboard', views_dashboard.files_list, name='dashboard_files_list'),
]
