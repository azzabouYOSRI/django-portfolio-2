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
    path('delete-mission/<str:pk>/', views.deletemission, name="delete-mission"),
    path('add-refrence/', views.addrefrence, name="add-refrence"),
    path('edit-refrence/<str:pk>/', views.editrefrence, name="edit-refrence"),
    path('delete-refrence/<str:pk>/', views.deleterefrence, name="delete-refrence"),
    path('add-personalinfomation/', views.addPersonalinfomation, name="add-personalinfomation"),
    path('edit-personalinfomation/<str:pk>/', views.editPersonalinfomation, name="edit-personalinfomation"),
    path('delete-personalinfomation/<str:pk>/', views.deletePersonalinfomation, name="delete-personalinfomation"),
    path('add-transcript/', views.addTranscript, name="add-transcript"),
    path('edit-transcript/<str:pk>/', views.editTranscript, name="edit-transcript"),
    path('delete-transcript/<str:pk>/', views.deleteTranscript, name="delete-transcript"),
    path('add-award/', views.addAwardsandhonors, name="add-award"),
    path('edit-award/<str:pk>/', views.editAwardsandhonors, name="edit-award"),
    path('delete-award/<str:pk>/', views.deleteAwardsandhonors, name="delete-award"),
    path('add-community/', views.Addcommunityservice, name="add-community"),
    path('edit-community/<str:pk>/', views.editCommunityservice, name="edit-community"),
    path('delete-community/<str:pk>/', views.deleteAwardsandhonors, name="delete-community"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('update/<str:pk>', views.updateUser, name="update-user"),
    path('add/', views.addUser, name="add-user"),
]
