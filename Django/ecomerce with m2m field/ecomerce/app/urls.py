from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm,MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm
urlpatterns = [
    # path('', views.home), For The Home Page
    path('', views.HomeView.as_view(),name='home'),


    # 1. for login we used django login functionality
    # path('login/', views.login, name='login'),
    path('accounts/login', auth_views.LoginView.as_view(template_name='app\login.html', authentication_form=LoginForm), name='login'),
    #2. for logout we used django login functionality
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), 
    #3. password change url.1
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app\passwordchange.html', 
    form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    #4. password change url.2
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='app\passwordchangedone.html'), name='passwordchangedone'),
    #5. password reset url . 1(password-reset)
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app\password_reset.html', form_class=MyPasswordResetForm),
     name='password_reset'),
    #6. password reset url . 2(password_reset_done)
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app\password_reset_done.html'),
     name='password_reset_done'),
    #7. password reset url . 3(password_reset_confirm)
    # (Format-> accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm'])
    path('password-reset-confirm//<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app\password_reset_confirm.html',
     form_class=MySetPasswordForm), name='password_reset_confirm'),
    #8. password reset url . 4(password_reset_complete)
     path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app\password_reset_complete.html'),
     name='password_reset_complete'),


    # for customer registration 
    path('registration/', views.customerRegistrationView.as_view(), name='customerregistration'),


    # path('profile/', views.profile, name='profile'),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('address/', views.address, name='address'),


    # for product details we take id for a particular product id and pass it to the productdetail.view through <int:pk>
    path('product-detail/<int:pk>', views.ProductDetailsView.as_view(), name='product-detail'),


    #1.1  For mobile and to show mobile data on webpage
    path('mobile/', views.mobile, name='mobile'),
    #1.1  we take data from template and send it to the view to show data accordingly for that we used slug here <slug:data> (For Mobile)
    path('mobiledata/<slug:data>', views.mobile, name='mobiledata'),
    #2.1  For top-wear and to show top-wear data on webpage
    path('top-wear/', views.top_wear, name='top_wear'),
    #2.2  we take data from template and send it to the view to show data accordingly for that we used slug here <slug:data> (For topwear)
    path('topweardata/<slug:data>', views.top_wear, name='topweardata'),
    #3.1  For bottom-wear and to show bottom-wear data on webpage
    path('bottom-wear/', views.bottom_wear, name='bottom_wear'),
    #3.3  we take data from template and send it to the view to show data accordingly for that we used slug here <slug:data> (For bottomwear)
    path('bottomweardata/<slug:data>', views.bottom_wear, name='bottomweardata'),


    # url for cart
    #1  To Add The Product To The Url
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    #2  For Showing Product in cart and other details in the cart
    path('cart/', views.show_cart, name='show_cart'),
    #3  Plus button without refreshing again when we Plus product quantity using json(ajax)
    path('pluscart/', views.plus_cart, name='pluscart'),
    #4  Minus button without refreshing again when we minus product quantity using json(ajax)
    path('minuscart/', views.minus_cart, name='minuscart'),
    #5 For Removing product from Cart With help of Json(ajax)
    path('removecart/', views.remove_cart, name='removecart'),


    path('buy/', views.buy_now, name='buy-now'),


    # for checkout after selcting products to cart and then selecting address and to show last details before payment
    path('checkout/', views.checkout, name='checkout'),
    # For Payment Done
    path('paymentdone/', views.payment_done, name='paymentdone'),


    path('orders/', views.orders, name='orders'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # this url is used to get or save photos(data) of product upload by admin