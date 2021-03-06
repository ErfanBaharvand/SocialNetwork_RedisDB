from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.enterPage, name="enterPage"),
    url(r'^Login$', views.Login, name="Login"),
    url(r'^Register$', views.Register, name="Register"),
    url(r'^RecoveryPassword$', views.RecoveryPassword, name="RecoveryPassword"),
    url(r'^UserHomePage/(\d+)$', views.UserHomePage, name="Home"),
    url(r'^UserHomePage/(?P<UserId>[0-9]+)/getNewPostWithAjax/(?P<countPost>[0-9]+)/$', views.getNewPostWithAjax,
        name='getNewPostWithAjax'),
    url(r'^UserPost/(\d+)$', views.UserPost, name="UserPost"),
    url(r'^EditUserPost/(\d+)$', views.EditUserPost, name="EditUserPost"),
    url(r'^DeleteUserPost/(\d+)$', views.DeleteUserPost, name="DeleteUserPost"),
    url(r'^Comment/(\d+)$', views.UserComment, name="UserComment"),
    url(r'^Search/(\d+)$', views.Search, name="Search"),
    url(r'^UserDashboard/(\d+)$', views.UserDashBoard, name="DashBoard"),
    url(r'^ChangeInformationOfUser/(\d+)$', views.UpdateUserInfo, name="UpdateUserInfo"),
    url(r'^Profile/(?P<UserId>[0-9]+)/GotoProfile/$', views.MyProfile, name="MyProfile"),
    url(r'^Profile/(?P<UserId>[0-9]+)/GotoProfile/(?P<DestinationUserId>[0-9]+)/$', views.Profile, name="Profile"),
    url(r'^Block/(?P<UserId>[0-9]+)/BlockUser/(?P<DestinationUserId>[0-9]+)/$', views.BlockUser, name="BlockUser"),
    url(r'^Follow/(?P<UserId>[0-9]+)/Follow/(?P<DestinationUserId>[0-9]+)/$', views.FollowUser, name="FollowUser"),
    url(r'^UnFollow/(?P<UserId>[0-9]+)/UnFollow/(?P<DestinationUserId>[0-9]+)/$', views.UnFollowUser,
        name="UnFollowUser"),
]
