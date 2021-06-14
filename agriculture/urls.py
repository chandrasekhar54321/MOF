"""agriculture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url 
from testapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',admin.site.urls),
    path('delete_product/<int:id>',views.delete_product),
    path('update_product/<int:id>',views.update_product),
    path('detail_product/<int:id>',views.detail_product),
    path('product_details/<int:id>',views.product_details),
    path('admin_scientist_user_detail/<int:id>',views.admin_scientist_user_detail),
    path('blog_details/<int:id>',views.blog_details),
    path('farming_technique_details/<int:id>',views.farming_technique_details),
    path('admin_wholeseller_user_detail/<int:id>',views.admin_wholeseller_user_detail),
    url(r'^$',views.home),
    url(r'^registerwithnormaluser/',views.registerwithnormaluser),
    url(r'^login/',views.login),
    url(r'^logout/',views.logout),
    url(r'^register/',views.register),
    url(r'^registerwithwholeseller/',views.registerwithwholeseller),
    url(r'^product/',views.product),
    url(r'^dashboard/',views.dashboard),
    url(r'^add_product/',views.add_product),
    url(r'^show_all_product/',views.show_all_product),
    url(r'^add_bank_details/',views.add_bank_details),
    url(r'^search/',views.search_product),
    url(r'^about/',views.about),
    url(r'^add_wishlist/',views.add_wishlist),
    url(r'^show_wishlist/',views.show_wishlist),
    url(r'^write_reviews/',views.write_reviews),
    url(r'^create_blog/',views.create_blog),
    url(r'^all_blog/',views.all_blog),
    url(r'^why/',views.why),
    url(r'^contact/',views.contact),
    url(r'^contact_save/',views.contact_save),
    url(r'^faq/',views.faq),
    url(r'^post_query/',views.post_query),
    url(r'^post_query_data/',views.post_query_data),
    url(r'^query_list/',views.query_list),
    url(r'^scientist_register/',views.scientist_register),
    url(r'^farming_technique/',views.farming_technique),
    url(r'^search_query/',views.search_query),
    url(r'^admin_show_all_scientist_user/',views.admin_show_all_scientist_user),
    url(r'^search_technique/',views.search_technique),
    url(r'^farming_technique_listing/',views.farming_technique_listing),
    url(r'^farming_technique_save_data/',views.farming_technique_save_data),
    url(r'^admin_show_all_farmer_user/',views.admin_show_all_farmer_user),
    url(r'^admin_show_all_wholeseller_user/',views.admin_show_all_wholeseller_user),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
