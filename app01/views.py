from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse,render,redirect
from app01 import models
from django.urls import reverse

def index(request):
    # with open('templates/yimi.html',encoding='utf-8') as f:
    #     data = f.read()
    # return HttpResponse(data)
    return render(request,'index.html')


# 展示所有出版社
def publisher_list(request):
    publishers = models.Publisher.objects.all()
    return render(request,'new_publisher_list.html',locals())

# 新增出版社
def add_publisher(request):
    publisher_name = request.POST.get('publisher_name',None)
    publisher_addr = request.POST.get('publisher_addr',None)
    if publisher_addr and publisher_name:
        models.Publisher.objects.create(name=publisher_name,addr=publisher_addr)
        return redirect('/publisher_list')
    return HttpResponse('新增失败')

# CBV版 类视图
from django.views import View

class AddPublisher(View):
    def post(self,request):
        print(request.body)
        print(request.POST)
        publisher_name = request.POST.get('publisher_name', None)
        publisher_addr = request.POST.get('publisher_addr', None)
        if publisher_addr and publisher_name:
            models.Publisher.objects.create(name=publisher_name, addr=publisher_addr)
            return redirect('/publisher_list')
        return HttpResponse('新增失败')


# 删除出版社
def del_publisher(request):
    publisher_id = request.GET.get('id',None)
    models.Publisher.objects.get(id=publisher_id).delete()
    return redirect('/publisher_list')

# 编辑出版社
def edit_publisher(request):
    print(request.POST)
    publisher_id = request.POST.get('publisher_id',None)
    publisher_name = request.POST.get('publisher_name',None)
    publisher_addr = request.POST.get('publisher_addr',None)

    if publisher_id and publisher_name and publisher_addr:
        edit_publisher = models.Publisher.objects.get(id=publisher_id)
        edit_publisher.name = publisher_name
        edit_publisher.addr = publisher_addr
        edit_publisher.save()
        return redirect('/publisher_list')
    return HttpResponse('编辑失败')
# 查询所有书籍
def book_list(request):
    all_books = models.Book.objects.all()
    for book in all_books:
        book.author_set.all()
    publishers = models.Publisher.objects.all()
    return render(request,'new_book_list.html',locals())

# 删除书籍
def del_book(request):
    del_book_id = request.GET.get('id',None)
    # 删除对象
    del_book = models.Book.objects.get(id=del_book_id)
    if del_book:
        del_book.delete()
        return redirect('/book_list')

    return HttpResponse('书籍删除失败！')
# 新增书籍
def add_book(request):
    book_title = request.POST.get('title',None).strip()
    publisher_id = request.POST.get('publisher_id',None)
    print(publisher_id)
    # 查询出publisher对象
    try:
        publisher = models.Publisher.objects.get(id=publisher_id)
        # 判断对象是否存在
        if publisher and book_title:
            # models.Book.objects.create(title=book_title, publisher=publisher)
            models.Book.objects.create(title=book_title, publisher_id=publisher_id)
            # return  HttpResponse('新增成功')
            return redirect('/book_list')
    except Exception as e:
        print(e)
        return HttpResponse('新增失败！')


# 编辑书籍
def edit_book(request):
    if request.method =='POST':
        edit_book_id = request.POST.get('id',None)
        title = request.POST.get('title',None)
        publisher_id = request.POST.get('publisher_id',None)
        # 根据id查询书籍
        edit_book = models.Book.objects.get(id=edit_book_id)
        edit_book.title = title
        # 查询publiser对象
        edit_book_publisher = models.Publisher.objects.get(id=publisher_id)
        print(edit_book_publisher)
        # edit_book.publisher = edit_book_publisher
        edit_book.publisher_id = publisher_id
        edit_book.save()
        return redirect('/book_list')
    edit_book_id = request.GET.get('id',None)
    # 查询该book的信息
    edit_book_info = models.Book.objects.get(id=edit_book_id)
    publishers = models.Publisher.objects.all()
    if edit_book_info:
        return render(request,'edit_book.html',{'edit_book':edit_book_info,'publishers':publishers})
    else:
        return HttpResponse('不存在该书籍！')


# 展示所有用户
def user_list(request):
    # 返回的是查询的所有结果的对象的集合
    author_list = models.Author.objects.all()
    books = models.Book.objects.all()
    # 获取author_list[0]对象所关联的所有book对象
    book_list = author_list[0].book.all()
    return render(request,'new_user_list.html',{'user_list':author_list,'books':books})

def add_user(request):
    error_message = ''
    # 如果是post，则获取name，然后添加
    if request.method == 'POST':
        username = request.POST.get('username',None).strip()
        books_id = request.POST.getlist('book',None)
        # print(username)
        # 新增记录,判断用户名是否为空
        if username and books_id:
            author = models.Author(name=username)
            author.save()
            author.book.set(books_id)
            # for book_id in books_id:
            #     book = models.Book.objects.get(id=book_id)
            #     author.book.add(book)
            #     author.save()
            # return HttpResponse('添加成功！')
            return redirect('/user_list')
        else:
            error_message = "名称不能为空"
    # 如果是get，则跳转到添加用户页面
    return render(request,'user_list.html',{'error_message':error_message})

# 修改用户名
def change_user(request):

    username = request.POST.get('username',None)
    id = request.POST.get('id',None)
    print(request.POST)
    # 查询数据库是否有这个id
    ret = models.Author.objects.get(id=id)
    if ret:
        ret.name = username  # 修改实例对象的属性值
        ret.save() # 把修改提交到数据库
        return redirect('/user_list')
    else:
        HttpResponse('修改的用户不存在')

# 删除用户
def del_user(request):
    if request.method == 'GET':
        # 查询是否有这条数据
        id = request.GET.get('id',None)
        if id:
            # 删除该id值的数据行
            # 1.根据id值查找到要删除的对象
            del_obj = models.Author.objects.get(id=id)
            # 2.删除查找到的对象
            del_obj.delete()
        return  redirect('/user_list')
    else:
        return HttpResponse('要删除的数据不存在！')

def login(request):
    error_message = ''
    if request.method == 'POST':
        # request.POST获取用户提交的数据
        username = request.POST.get('userName',None)
        password = request.POST.get('password',None)
        print(username,password)
        if username == 'robert' and password =='robert':
            # 登录成功
            # return HttpResponse('登录成功！')
            return redirect("http://testlink.robertzwj.com")
        else:
            error_message = '账号或密码错误'
            # return render(request,'login.html',{'error_message':error_message})

    return render(request,'login.html',{'error_message':error_message})

def upload_file(request):
    file = request.FILES.get('upload_file')
    # 获取文件对象的名称
    file_name = file.name
    print(file_name)
    # 将接收的文件写入到本地，本地文件名称为接收的文件名称
    with open(file_name,'wb') as f:
        # 循环读取上传的文件的chunks(),相当于是分块读取然后写入
        for chunk in request.FILES['upload_file'].chunks():
            f.write(chunk)
    return render(request,'test.html')
