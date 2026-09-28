from django.urls import path

from main.views import (
    register,
    login_user,
    logout_user,
    show_main, 
    show_experience, 
    show_education, 
    create_education, 
    create_experience,
    edit_experience,
    edit_education,
    get_education_json,
    get_experience_json,
    delete_education,
    delete_experience,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    path("experience/add/", create_experience, name="create_experience"),
    path("education/add/", create_education, name="create_education"),
    path("experience/<uuid:experience_id>/edit/", edit_experience, name="edit_experience"),
    path("education/<uuid:education_id>/edit/", edit_education, name="edit_education"),
    path("api/experience", get_experience_json, name="get_experience_json"),
    path("api/education", get_education_json, name="get_education_json"),
    path("experience/<uuid:experience_id>/delete/",delete_experience,name="delete_experience"),
    path("education/<uuid:education_id>/delete/",delete_education,name="delete_education"),
]