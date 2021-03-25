from django.urls import path
from django.conf.urls.static import static

from EShop import settings
from .views2 import home,signup,login,cart,checkout,orders,profile,edit_profile,change_password,product_details,reset_password_by_email,reset_password_link
urlpatterns = [
    path('',home.Index.as_view(),name="homepage"),
    path('signup',signup.Signup.as_view()),
    path('login',login.Login.as_view(),name="login"),
    path('logout',login.logout,name="logout"),
    path('cart',cart.Cart_View.as_view(),name="cart"),
    path('check-out',checkout.CheckOut.as_view(),name="checkout"),
    path('orders',orders.OrderView.as_view(),name="orders"),
    path('profile',profile.Profile.as_view(),name="profile"),
    path('edit_profile',edit_profile.EditProfile.as_view(),name="edit_profile"),
    path('change_password', change_password.ChangePassword.as_view(), name="change_password"),
    path('reset_password', reset_password_by_email.ResetPassword.as_view(), name="reset_password"),
    path('reset_password_link/<uidb64>/<token>',reset_password_link.ResetPasswordLink.as_view(),name="set_new_password"),
    path('product_details',product_details.ProductDetails.as_view(),name="product_details")
]