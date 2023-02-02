from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('employeapi/',views.info),
    path('messageapi/',views.messagess),
    path('employeapi/<int:pk>',views.sendmoneydetail),
    path('',views.login,name="login"),
    path('',views.logout,name="logout"),
    path('home/',views.home,name="home"),
    path('payment/',views.payment,name="payment"),
    path('view/<int:id>',views.view,name="view"),
    path('addemployees/',views.addemployee,name="addemployee"),
    path('employees/',views.employees,name="employees"),
    path('delete/<int:id>',views.delete_employee,name="delete"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('message/',views.message,name="message"),
    path('setting/',views.setting,name="setting"),
    path('sendmessage/',views.sendmessage,name="sendmessage"),
    path('composemessage/',views.composemessage,name="composemessage"),
    path('paydate/',views.paydate,name="paydate"), 
    path('payemployee/',views.payemployee,name="payemployee"),
    path('adddepartment/',views.adddepartment,name="adddepartment"),
    path('departments/',views.departments,name="departments"),
    path('addbranch/',views.addbranch,name="addbranch"),
    path('branches/',views.branches,name="branches"), 
    path('changepassword/',views.changepassword,name="changepassword"),
    path('about/',views.about,name="about"), 

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
