from django.contrib import admin
from django.urls import path, include

from leads.views import home_page, SignUp
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetConfirmView, PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView
# url patterns holds the forwarding for the pages the user is going to visit. For example if we types in /home in the browser
# it will present the information that we have set the path for /home. empty path is going to handle the path when no forwardinng / is added to url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home-page'),
    # pointing to new urls file to handle specific path requests 
    path('leads/', include('leads.urls', namespace="leads")),
    path('signup/', SignUp.as_view(), name='signup'),
    path('reset_password/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='confirm-reset'),
    path('password_reset_complete/',  PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


]

 