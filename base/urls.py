from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name="home"),
    path('profile/', views.profilpage, name="profile"),

    path('project/<str:pk>/', views.projectPage, name="project"),

    path('add-project/', views.addProject, name="add-project"),
    path('edit-project/<str:pk>/', views.editProject, name="edit-project"),
    path('delete-project/<str:pk>/', views.deleteproject, name="delete-project"),

    path('inbox/', views.inboxPage, name="inbox"),
    path('message/<str:pk>/', views.messagePage, name="message"),

    path('add-skill/', views.addSkill, name="add-skill"),
    path('edit-skills/<str:pk>/', views.editskills, name="edit-skills"),
    path('delete-skills/<str:pk>/', views.deletemission, name="delete-skills"),

    path('add-mission/', views.addmission_statment, name="add-mission"),
    path('edit-mission/<str:pk>/', views.editmission, name="edit-mission"),
    path('delete-mission/<str:pk>/', views.deletemission, name="delete-mission")

    #
    # path('add-endorsement/', views.addEndorsement, name="add-endorsement"),
    #
    # path('donation/', views.donationPage, name="donation"),
    #
    # path('chart/', views.chartPage, name="chart"),
]
