from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("home2", views.home2, name="home2"),
    path("login", views.login, name="login"),
    path("approved_sector", views.approved_sector, name="approved-sector"),
    path("investor", views.investor, name="investor"),
    path("startup", views.startup, name="startup"),
    path("contact", views.contact, name="contact"),
    path("snippest", views.snippest_details, name="snippest"),
    # path("inline_format", views.inlineformat, name="inlineformat"),
    path("inlineformat", views.inlineformatview.as_view(), name="inlineformat"),
    path("approvedsector", views.ApprovedSectorview.as_view(), name="approvedsector"),
    path("profile-registeration", views.Register_Profilesview.as_view(), name="profile-registeration"),
    path("index2", views.index2, name="index2"),
    path("index3", views.index3, name="index3"),
    path("index4", views.index4, name="index4"),

    







]
