--- mysite01（基本的请求和响应流程）
django-admin.py startproject mysite01
cd mysite01
django-admin.py startapp polls | python manage.py startapp polls

python manage.py runserver
python manage.py runserver 8080
把自己主机的IP添加到setting中ALLOWED_HOSTS，其他电脑可以通过你的IP访问Django项目。然后python manage.py runserver 0:8080

函数 include('polls.urls') 允许引用其它 URLconfs

--- mysite02（数据库 API ）
python manage.py migrate: 检查 INSTALLED_APPS 设置，为其中的每个应用创建需要的数据表
Django 支持所有常用的数据库关系：多对一、多对多和一对一。
python manage.py makemigrations polls: 检测你对模型文件的修改
python manage.py migrate
python manage.py createsuperuser

q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
q.id
q.question_text = "What's up?"
q.save()
Question.objects.all()
q=Question.objects.get(id=1)
q.choice_set.all()
q.choice_set.create(choice_text='Not much', votes=0)
c=q.choice_set.create(choice_text='Not much', votes=0)
c.question
q.choice_set.all()
q.choice_set.count()
更新 删除

--- mysite03（视图） 
1、每个视图必须要做的只有两件事：返回一个包含被请求页面内容的 HttpResponse 对象，或者抛出一个异常，比如 Http404 。
2、项目的 TEMPLATES 配置项描述了 Django 如何载入和渲染模板。默认的设置文件设置了 DjangoTemplates 后端，并将 APP_DIRS 设置成了 True。这一选项将会让 DjangoTemplates 在每个 INSTALLED_APPS 文件夹中寻找 "templates" 子目录。
3、Django 将会选择第一个匹配的模板文件，如果你有一个模板文件正好和另一个应用中的某个模板文件重名，Django 没有办法 区分 它们。我们需要帮助 Django 选择正确的模板，最简单的方法就是把他们放入各自的 命名空间 中，也就是把这些模板放入一个和 自身 应用重名的子文件夹里。
4、polls.urls 的 url() 函数中通过 name 参数为 URL 定义了名字，你可以使用 {% url %} 标签代替它。
5、在一个真实的 Django 项目中，可能会有五个，十个，二十个，甚至更多应用。Django 如何分辨重名的 URL 呢？在根 URLconf 中添加命名空间。在 polls/urls.py 文件中稍作修改，加上 app_name 设置命名空间。

--- mysite04 （表单）
Django 已经拥有一个用来防御它的非常容易使用的系统。 简而言之，所有针对内部 URL 的 POST 表单都应该使用 {% csrf_token %} 模板标签。
