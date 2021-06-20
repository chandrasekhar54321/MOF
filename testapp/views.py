from django.shortcuts import render,redirect
from testapp.models import User,Normal_User,Whole_Seller,Products,Bank_Detail,WishListss,Review,Blogs,Contact,Query,Scientist_Register,Farming_Technique
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.models import auth
from django.http import JsonResponse
import datetime
from django.core.mail import send_mail 
from django.core.mail import EmailMultiAlternatives 
from django.template.loader import get_template 
from django.template import Context 
from django.http import HttpResponse
# import sweetify
# Create your views here.


def home(request):
    try:
        role=request.user.role
        print("Role Of User",role)
        return render(request,"index.html",{'role':role})
    except:
        role="no"
        print("Role Of User",role)
        param={'role':role}
        return render(request,'index.html',param)
def about(request):
    try:
        role=request.user.role
        print("Role Of User",role)
        return render(request,"about.html",{'role':role})
    except:
        role="no"
        print("Role Of User",role)
        param={'role':role}
        return render(request,'about.html',param)
@csrf_exempt
def registerwithnormaluser(request):
    errmessage=""
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        first_name=request.POST['f_name']
        last_name=request.POST['l_name']
        password=request.POST['pwd']
        cnf_password=request.POST['cnf_password']
        role="farmer"
        mobile=request.POST['mobile']
        if User.objects.filter(username=username).exists():
            errmessage=errmessage+"UserName Taken"
            param={"errmessage":errmessage}
            return render(request,"farmer_register.html",param)
        elif User.objects.filter(email=email).exists():
            errmessage=errmessage+"Email Already Taken"
            param={"errmessage":errmessage}
            return render(request,"farmer_register.html",param)
        elif password!=cnf_password:
            errmessage=errmessage+"Password not Match"
            param={"errmessage":errmessage}
            return render(request,"farmer_register.html",param)
        else:
            result=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password,role=role)
            result.save() 
            user_id=result.id
            data=Normal_User(user_id=user_id,mobile=mobile)   
            data.save()
            messages.info(request,"You Register Successfully")
            # name=username
            # htmly = get_template('farmer_email.html') 
            # d = { 'name':name } 
            # subject, from_email, to = 'Team MOF', 'teams.mof@gmail.com', email 
            # html_content = htmly.render(d) 
            # msg = EmailMultiAlternatives(subject, html_content, from_email, [to]) 
            # msg.attach_alternative(html_content, "text/html") 
            # msg.send()
            return render(request,"farmer_register.html")
    else:
        return render(request,'farmer_register.html')
@csrf_exempt
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            if user.role=='farmer':
                return redirect('/product')
            elif user.role=='wholeseller':
                return redirect('/dashboard')
            elif user.role=='admin':
                return redirect('/')
            elif user.role=='scientist':
                return redirect('/')
            else:
                return redirect("/login")
        else:
            messages.info(request,'Invalid credential')  
            return redirect('/login')  
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/login')
def register(request):
    try:
        role=request.user.role
        print("Role Of User",role)
        return render(request,"register.html",{'role':role})
    except:
        role="no"
        print("Role Of User",role)
        param={'role':role}
        return render(request,'register.html',param)
@csrf_exempt
def registerwithwholeseller(request):
    errmessage=""
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        first_name=request.POST['f_name']
        last_name=request.POST['l_name']
        password=request.POST['pwd']
        cnf_password=request.POST['cnf_password']
        role="wholeseller"
        mobile=request.POST['mobile']
        gst_no=request.POST['gst']
        city=request.POST['city']
        zip_code=request.POST['zip_code']
        if User.objects.filter(username=username).exists():
            errmessage=errmessage+"UserName Already Taken"
            param={'errmessage':errmessage}
            return render(request,'whole_seller_register.html',param)
        elif User.objects.filter(email=email).exists():
            errmessage=errmessage+"Email Already Taken"
            param={'errmessage':errmessage}
            return render(request,'whole_seller_register.html',param)
        elif password!=cnf_password:
            errmessage=errmessage+"Password Not Match"
            param={'errmessage':errmessage}
            return render(request,'whole_seller_register.html',param)
        elif gst_no==15:
            errmessage=errmessage+"GST Number Should be 15 digit only"
            param={'errmessage':errmessage}
            return render(request,'whole_seller_register.html',param)
        elif mobile==10:
            errmessage=errmessage+"Mobile Number Should be 10 digit only"
            param={'errmessage':errmessage}
            return render(request,'whole_seller_register.html',param)
        elif zip_code==6:
            errmessage=errmessage+"Zip Code Must be 6 digit only"
            param={'errmessage':errmessage}
            return render(request,'whole_seller_register.html',param)
        else:
            result=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password,role=role)
            result.save() 
            user_id=result.id
            data=Whole_Seller(user_id=user_id,city=city,mobile=mobile,zip_code=zip_code,gst_no=gst_no)   
            data.save()
            # name=username
            # htmly = get_template('wholeseller_email.html') 
            # d = { 'name':name } 
            # subject, from_email, to = 'Team MOF', 'teams.mof@gmail.com', email 
            # html_content = htmly.render(d) 
            # msg = EmailMultiAlternatives(subject, html_content, from_email, [to]) 
            # msg.attach_alternative(html_content, "text/html") 
            # msg.send()
            messages.info(request,"Data Saved Successfully")
            return redirect("/registerwithwholeseller")
    else:
        return render(request,'whole_seller_register.html')
def product(request):
    try:
        role=request.user.role
        print("Role Of User",role)
        all_data=Products.objects.all()
        param={'role':role,'all_data':all_data}
        return render(request,"product.html",param)
    except:
        role="no"
        print("Role Of User",role)
        all_data=Products.objects.all()
        param={'role':role,'all_data':all_data}
        return render(request,'product.html',param)
    # all_data=Products.objects.all()
    # param={'all_data':all_data}
    # return render(request,'product.html',param)
def search_product(request):
    try:
        role=request.user.role
        print("Role Of User",role)
        queryString=request.GET['q']
        all_data=Products.objects.filter(product_name__contains=queryString)
        param={'role':role,'all_data':all_data}
        return render(request,"product.html",param)
    except:
        role="no"
        print("Role Of User",role)
        queryString=request.GET['q']
        all_data=Products.objects.filter(product_name__contains=queryString)
        param={'role':role,'all_data':all_data}
        return render(request,'product.html',param)
    # queryString=request.GET['q']
    # all_data=Products.objects.filter(product_name__contains=queryString)
    # param={'all_data':all_data}
    # return render(request,'product.html',param)
def dashboard(request):
    if request.user.role=="wholeseller":
        return render(request,'dashboard.html')
    else:
        return redirect("/")

def add_product(request):
    if request.user.role=="wholeseller":
        if request.method=='POST':
            product_name=request.POST['product_name']
            product_price=request.POST['product_price']
            product_quantity=request.POST['product_quantity']
            product_description=request.POST['product_description']
            product_image=request.FILES['product_image']
            product_image1=request.FILES['product_image1']
            product_image2=request.FILES['product_image2']
            user_id=request.user.id
            name=request.user.username
            email=request.user.email
            data=Products(user_id=user_id,product_name=product_name,product_price=product_price,product_quantity=product_quantity,product_description=product_description,product_image=product_image,product_image1=product_image1,product_image2=product_image2)
            data.save()
            # htmly = get_template('add_product_email.html') 
            # d = { 'name':name } 
            # subject, from_email, to = 'Team MOF', 'teams.mof@gmail.com', email 
            # html_content = htmly.render(d) 
            # msg = EmailMultiAlternatives(subject, html_content, from_email, [to]) 
            # msg.attach_alternative(html_content, "text/html") 
            # msg.send()
            return redirect('/add_product')
        else:
            return render(request,'product_add.html')
        return render(request,"product_add.html")
    else:
        return redirect("/")
def show_all_product(request):
    if request.user.role=="wholeseller":
        user_data=request.user.id
        data=Products.objects.filter(user_id__in=[user_data])
        print("All Product Data",data)
        param={'data':data}
        return render(request,'show_all_product.html',param)
    else:
        return redirect('/')
def delete_product(request,id):
    data=Products.objects.get(id=id)
    data.delete()
    return redirect('/show_all_product')
def update_product(request,id):
    if request.method=='POST':
        product_name=request.POST['product_name']
        product_price=request.POST['product_price']
        product_quantity=request.POST['product_quantity']
        product_description=request.POST['product_description']
        product_image=request.FILES['product_image']
        product_image1=request.FILES['product_image1']
        product_image2=request.FILES['product_image2']
        data=Products.objects.get(id=id)
        data.product_name=product_name
        data.product_price=product_price
        data.product_quantity=product_quantity
        data.product_description=product_description
        data.product_image=product_image
        data.product_image1=product_image1
        data.product_image2=product_image2
        data.save()
        return redirect('/show_all_product')
    else:
        data=Products.objects.get(id=id)
        param={'data':data}
        return render(request,"update_product.html",param)

def add_bank_details(request):
    if request.user.role=="wholeseller":
        if request.method=="POST":
            name=request.POST['name']
            acc_no=request.POST['acc_no']
            ifcs_code=request.POST['ifcs_code']
            branch_name=request.POST['branch_name']
            bank_name=request.POST['bank_name']
            user_id=request.user.id
            data=Bank_Detail(user_id=user_id,name=name,acc_no=acc_no,ifcs_code=ifcs_code,branch_name=branch_name,bank_name=bank_name)
            data.save()
            messages.info(request,"Bank Details Save Successfully")
            return redirect('/add_bank_details')
        else:
            return render(request,"add_bank_detail.html")
        return render(request,"add_bank_detail.html")
    else:
        return redirect("/")
def detail_product(request,id):
    data=Products.objects.get(id=id)
    param={'data':data}
    return render(request,'detail_product.html',param)
def add_wishlist(request):
    if request.method=='POST':
        product_id=request.POST['product_id']
        user_id=request.user.id
        data=WishListss(user_id=user_id,product_id=product_id)
        data.save()
        dict_data={'success':'Data Save Successfully'}
        return JsonResponse(dict_data)
    else:
        dict_data={'success':'Data not Successfully'}
        return JsonResponse(dict_data)
def show_wishlist(request):
    try:
        role=request.user.role
        print("Role Of User",role)
        user_id=request.user.id
        data=WishListss.objects.filter(user_id__in=[user_id]).values('product_id')
        for id in data:
            print("Product Id",id)
        print(id['product_id'])
        p_id=id['product_id']
        data=Products.objects.filter(id__in=[p_id])
        param={'role':role,'data':data}
        return render(request,"show_wishlist.html",param)
    except:
        role="no"
        print("Role Of User",role)
        # user_id=request.user.id
        # data=WishListss.objects.filter(user_id__in=[user_id]).values('product_id')
        # for id in data:
        #     print("Product Id",id)
        # print(id['product_id'])
        # p_id=id['product_id']
        # data=Products.objects.filter(id__in=[p_id])
        param={'role':role}
        return render(request,'show_wishlist.html',param)
def product_details(request,id):
    try:
        role=request.user.role
        print("Role Of User",role)
        user_id=request.user.id
        data=Products.objects.get(id=id)
        print(data.product_name)
        reviewdata=Review.objects.filter(p_id__in=[id])
        param={'role':role,'data':data,'reviewdata':reviewdata}
        return render(request,'product_details.html',param)
    except:
        role="no"
        print("Role Of User",role)
        data=Products.objects.get(id=id)
        print(data.product_name)
        reviewdata=Review.objects.filter(p_id__in=[id])
        param={'data':data,'reviewdata':reviewdata}
        return render(request,'product_details.html',param)

# def reviews(request):
#     if request.method=='POST':
def write_reviews(request):
    if request.method=='POST':
        headline=request.POST['headline']
        description=request.POST['description']
        p_id=request.POST['p_id']
        user_id=request.user.id
        name=request.user.username
        email=request.user.email
        data=Review(user_id=user_id,p_id=p_id,headline=headline,description=description)
        data.save()
        # htmly = get_template('write_reviews_email.html') 
        # d = { 'name':name } 
        # subject, from_email, to = 'Team MOF', 'teams.mof@gmail.com', email 
        # html_content = htmly.render(d) 
        # msg = EmailMultiAlternatives(subject, html_content, from_email, [to]) 
        # msg.attach_alternative(html_content, "text/html") 
        # msg.send()
        dict_data={'success':'Data Save Successfully'}
        return JsonResponse(dict_data)
    else:
        dict_data={'success':'Data not Successfully'}
        return JsonResponse(dict_data)


def create_blog(request):
    if request.method=='POST':
        blog_title=request.POST['blog_title']
        blog_name=request.POST['blog_name']
        description=request.POST['description']
        blog_image=request.FILES['blog_image']
        create_date = datetime.datetime.now()
        print(create_date)
        data=Blogs(blog_title=blog_title,blog_name=blog_name,description=description,create_date=create_date,blog_image=blog_image)
        data.save()
        messages.info(request,"Data Save Successfully")
        return redirect('/create_blog')
    else:
        return render(request,'create_blog.html')
def all_blog(request):
    try:
        role=request.user.role
        print("Role Of User",role)
        data=Blogs.objects.all()
        param={'role':role,'data':data}
        return render(request,'all_blog.html',param)
    except:
        role="no"
        print("Role Of User",role)
        data=Blogs.objects.all()
        param={'data':data}
        return render(request,'all_blog.html',param)
def blog_details(request,id):
    try:
        role=request.user.role
        print("Role Of User",role)
        data=Blogs.objects.get(id=id)
        param={'role':role,'data':data}
        return render(request,'blog_detail.html',param)
    except:
        role="no"
        print("Role Of User",role)
        data=Blogs.objects.get(id=id)
        param={'data':data}
        return render(request,'blog_detail.html',param)
def why(request):
    return render(request,'why.html')
def contact(request):
    try:
        role=request.user.role
        print("Role Of User",role)
        param={'role':role}
        return render(request,'contact.html',param)
    except:
        role="no"
        print("Role Of User",role)
        return render(request,'contact.html')
# def contact(request):
#     return render(request,'contact.html')
def contact_save(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        data=Contact(name=name,email=email,subject=subject,message=message)
        data.save()
        # htmly = get_template('contact_email.html') 
        # d = { 'name':name } 
        # subject, from_email, to = 'Team MOF', 'teams.mof@gmail.com', email 
        # html_content = htmly.render(d) 
        # msg = EmailMultiAlternatives(subject, html_content, from_email, [to]) 
        # msg.attach_alternative(html_content, "text/html") 
        # msg.send()
        messages.info(request,"Data Saved Successfully")
        return redirect('/contact')
    else:
        return redirect('/contact')
def faq(request):
    try:
        role=request.user.role
        print("Role Of User",role)
        param={'role':role}
        return render(request,'faq.html',param)
    except:
        role="no"
        print("Role Of User",role)
        return render(request,'faq.html')
# def admin_show_all_farmer_user(request):
#     try:
#         id=request.user.id
#         role=request.user.role
#         print(role)
#         data=User.objects.filter(role__in=['farmer'])
#         print(data)
#         print(data.first_name)
#         result=Normal_User.objects.aLL()
#         print(result)
#         print(result.mobile)
#         param={'role':role,'data':data,'result':result}
#         return render(request,'admin_show_farmer.html',param)
#     except:
#         role="no"
#         param={'role':role}
#         return render(request,'admin_show_farmer.html',param)

def admin_show_all_farmer_user(request):
    try:
        role=request.user.role
        data=User.objects.filter(role__in=['farmer'])
        result=Normal_User.objects.all()
        param={'role':role,'data':data,'result':result}
        print("Role Of User",role)
        return render(request,"admin_show_farmer.html",param)
    except:
        role="no"
        print("Role Of User",role)
        param={'role':role}
        return render(request,'admin_show_farmer.html',param)
def admin_show_all_wholeseller_user(request):
    try:
        role=request.user.role
        data=User.objects.filter(role__in=['wholeseller'])
        result=Whole_Seller.objects.all()
        param={'role':role,'data':data,'result':result}
        print("Role Of User",role)
        return render(request,"admin_show_all_wholeseller.html",param)
    except:
        role="no"
        print("Role Of User",role)
        param={'role':role}
        return render(request,'admin_show_all_wholeseller.html',param)
# def admin_wholeseller_user_detail(request,id):
#     try:
#         role=request.user.role
#         data=User.objects.get(id=id)
#         result=Whole_Seller.objects.get(user_id=id)
#         param={'role':role,'data':data,'result':result}
#         print("Role Of User",role)
#         return render(request,"admin_wholeseller_user_detail.html",param)
#     except:
#         role="no"
#         print("Role Of User",role)
#         param={'role':role}
#         return render(request,'admin_wholeseller_user_detail.html',param)




def admin_wholeseller_user_detail(request,id):
    try:
        role=request.user.role
        # data=User.objects.filter(role__in=['wholeseller'])
        # result=Whole_Seller.objects.all()
        data=User.objects.filter(id=id)
        result=Whole_Seller.objects.filter(user_id=id)
        product=Products.objects.filter(user_id__in=[id])
        print(product)
        print(result)
        param={'role':role,'data':data,'result':result,'product':product}
        print("Role Of User",role)
        return render(request,"admin_wholeseller_user_detail.html",param)
    except:
        role="no"
        print("Role Of User",role)
        param={'role':role}
        return render(request,'admin_wholeseller_user_detail.html',param)



def post_query(request):
    try:
        role=request.user.role
        print("Role Of User",role)
        param={'role':role}
        return render(request,'post_query.html',param)
    except:
        role="no"
        print("Role Of User",role)
        return render(request,'post_query.html')

def post_query_data(request):
    if request.method=='POST':
        name=request.POST['name']
        question=request.POST['question']
        query_image=request.FILES['query_image']
        data=Query(name=name,question=question,query_image=query_image)
        data.save()
        messages.info(request,"Data Save Successfully")
        return render(request,"post_query.html")
    else:
        return redirect('/post_query')
def query_list(request):
    try:
        role=request.user.role
        data=Query.objects.all()
        print("Role Of User",role)
        print(data)
        param={'role':role,'data':data}
        return render(request,'query_list.html',param)
    except:
        role="no"
        data=Query.objects.all()
        print("Role Of User",role)
        param={'role':role,'data':data}
        return render(request,'query_list.html',param)

def search_query(request):
    try:
        role=request.user.role
        print("Role Of User",role)
        queryString=request.GET['q']
        data=Query.objects.filter(question__contains=queryString)
        param={'role':role,'data':data}
        return render(request,"query_list.html",param)
    except:
        role="no"
        print("Role Of User",role)
        queryString=request.GET['q']
        data=Query.objects.filter(question__contains=queryString)
        param={'role':role,'data':data}
        return render(request,'query_list.html',param)

def query_detail(request,id):
    try:
        role=request.user.role
        print("Role Of User",role)
        data=Query.objects.get(id=id)
        param={'role':role,'data':data}
        return render(request,"query_detail.html",param)
    except:
        role="no"
        print("Role Of User",role)
        queryString=request.GET['q']
        data=Query.objects.get(id=id)
        param={'role':role,'data':data}
        return render(request,'query_detail.html',param)

# def farming_technique(request):
#     return render(request,"farming_technique.html")


# Agriculture Scientist Register

@csrf_exempt
def scientist_register(request):
    errmessage=""
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        first_name=request.POST['f_name']
        last_name=request.POST['l_name']
        password=request.POST['pwd']
        cnf_password=request.POST['cnf_password']
        role="scientist"
        mobile=request.POST['mobile']
        designation=request.POST['designation']
        description=request.POST['description']
        if User.objects.filter(username=username).exists():
            errmessage=errmessage+"UserName Taken"
            param={"errmessage":errmessage}
            return render(request,"scientist_register.html",param)
        elif User.objects.filter(email=email).exists():
            errmessage=errmessage+"Email Already Taken"
            param={"errmessage":errmessage}
            return render(request,"scientist_register.html",param)
        elif password!=cnf_password:
            errmessage=errmessage+"Password not Match"
            param={"errmessage":errmessage}
            return render(request,"scientist_register.html",param)
        else:
            result=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password,role=role)
            result.save() 
            user_id=result.id
            data=Scientist_Register(user_id=user_id,mobile=mobile,designation=designation,description=description)   
            data.save()
            messages.info(request,"You Register Successfully")
            # name=username
            # htmly = get_template('scientist_email.html') 
            # d = { 'name':name } 
            # subject, from_email, to = 'Team MOF', 'teams.mof@gmail.com', email 
            # html_content = htmly.render(d) 
            # msg = EmailMultiAlternatives(subject, html_content, from_email, [to]) 
            # msg.attach_alternative(html_content, "text/html") 
            # msg.send()
            return render(request,"scientist_register.html")
    else:
        return render(request,'scientist_register.html')


def farming_technique(request):
    try:
        role=request.user.role
        print("Role Of User",role)
        param={'role':role}
        return render(request,'farming_technique.html',param)
    except:
        role="no"
        print("Role Of User",role)
        return render(request,'farming_technique.html')
def farming_technique_save_data(request):
    if request.method=="POST":
        heading=request.POST['heading']
        youtube_link=request.POST['youtube_link']
        farming_description=request.POST['farming_description']
        farm_image=request.FILES['farm_image']
        user_id=request.user.id
        name=request.user.username
        email=request.user.email
        data=Farming_Technique(user_id=user_id,heading=heading,youtube_link=youtube_link,farming_description=farming_description,farm_image=farm_image)
        data.save()
        # messages.info(request,"You Register Successfully")
        # htmly = get_template('farming_technique_email.html') 
        # d = { 'name':name } 
        # subject, from_email, to = 'Team MOF', 'teams.mof@gmail.com', email 
        # html_content = htmly.render(d) 
        # msg = EmailMultiAlternatives(subject, html_content, from_email, [to]) 
        # msg.attach_alternative(html_content, "text/html") 
        # msg.send()
        messages.info(request,"Data Save Successfully")
        return redirect("/farming_technique")
    else:
        return redirect("/farming_technique")

# listing farming technique

def farming_technique_listing(request):
    try:
        role=request.user.role
        print("Role Of User",role)
        data=Farming_Technique.objects.all()
        param={'role':role,'data':data}
        return render(request,'farming_technique_listing.html',param)
    except:
        role="no"
        print("Role Of User",role)
        data=Farming_Technique.objects.all()
        param={'role':role,'data':data}
        return render(request,'farming_technique_listing.html',param)

# Search Farming Technique
def search_technique(request):
    try:
        role=request.user.role
        print("Role Of User",role)
        queryString=request.GET['q']
        data=Farming_Technique.objects.filter(heading__contains=queryString)
        param={'role':role,'data':data}
        return render(request,"farming_technique_listing.html",param)
    except:
        role="no"
        print("Role Of User",role)
        queryString=request.GET['q']
        data=Farming_Technique.objects.filter(heading__contains=queryString)
        param={'role':role,'data':data}
        return render(request,'farming_technique_listing.html',param)

# Farming Technique Detail

def farming_technique_details(request,id):
    try:
        role=request.user.role
        print("Role Of User",role)
        data=Farming_Technique.objects.get(id=id)
        print(data.user_id)
        print(data.user_id)
        user=data.user_id
        result=User.objects.get(id=user)
        print(result.first_name)
        print(result.last_name)
        scientist_data=Scientist_Register.objects.get(user_id=user)
        print(scientist_data)
        param={'role':role,'data':data,'result':result,'scientist_data':scientist_data}
        return render(request,'farming_technique_details.html',param)
    except:
        role="no"
        print("Role Of User",role)
        data=Farming_Technique.objects.get(id=id)
        print(data.user_id)
        user=data.user_id
        result=User.objects.get(id=user)
        print(result.first_name)
        print(result.last_name)
        scientist_data=Scientist_Register.objects.get(user_id=user)
        print(scientist_data)
        param={'role':role,'data':data,'result':result,'scientist_data':scientist_data}
        return render(request,'farming_technique_details.html',param)



def admin_show_all_scientist_user(request):
    try:
        role=request.user.role
        data=User.objects.filter(role__in=['scientist'])
        param={'role':role,'data':data}
        print("Role Of User",role)
        return render(request,"admin_show_scientist.html",param)
    except:
        role="no"
        print("Role Of User",role)
        param={'role':role}
        return render(request,'admin_show_scientist.html',param)

def admin_scientist_user_detail(request,id):
    try:
        role=request.user.role
        # data=User.objects.get(id=id)
        result=Scientist_Register.objects.get(user_id=id)
        param={'role':role,'result':result}
        print("Role Of User",role)
        print(result)
        return render(request,"admin_show_scientist_details.html",param)
    except:
        role="no"
        print("Role Of User",role)
        param={'role':role}
        return render(request,'admin_show_scientist_details.html',param)




