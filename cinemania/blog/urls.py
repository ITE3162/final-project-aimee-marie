from django.urls import path
from .views import home,register,login,dashboard,logout_func,new_blog,blogs,blog_details,new_team,about_us,what_we_do


urlpatterns = [
    path("", home, name="home"),
    path("register", register, name="register"),
    path("login", login, name="login"),
    path("logout", logout_func, name="logout"),

    # user dasboard paths
    path("dashboard", dashboard, name="dashboard"),
    path("create-blog", new_blog, name="create-blog"),
    path("new-team", new_team, name="new-team"),
    path("about-us", about_us, name="about-us"),
    path("what-we-do", what_we_do, name="what-we-do"),

    # Client view paths
    path("blogs", blogs, name="blogs"),
    path("blog_details/<int:by>", blog_details, name="blog_details"),

]
