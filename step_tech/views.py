from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import connection
from myapp.models import User
from django.http import Http404

# def hello(request):
#     return HttpResponse('Hello, World!')

def hello(request):
    response = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello, World!</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        
        header {
            background-color: #333;
            color: #fff;
            padding: 10px;
        }
        
        nav ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
        }
        
        nav ul li {
            display: inline;
            margin-right: 10px;
        }
        
        nav ul li a {
            color: #fff;
            text-decoration: none;
        }
        
        h1 {
            color: #333;
        }
        
        footer {
            background-color: #333;
            color: white;
            padding: 1em;
            text-align: center;
        }   
    </style>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/hello/">Hello</a></li>
                <li><a href="/users/">Users</a></li>
                <li><a href="/new_user/">New User</a></li>
            </ul>
        </nav>
    </header>

    <h1>Hello, World!</h1>

    <footer>
        Step Tech
    </footer>
</body>
</html>
"""
    return HttpResponse(response)



def homePage(request):
    return HttpResponse('Step Tech')

def index(request):
    return render(request, 'index.html')

def users(request):
    users = User.objects.all()
    context = {'users': users}
    print(context)
    return render(request, 'users.html', context)


def new_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        user = User(first_name=first_name, last_name=last_name, email=email)
        user.save()
        return redirect('users')
    return render(request, 'new_user.html')



def user(request, user_id):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM users WHERE id=%s', [user_id])
        data = cursor.fetchone()
    if data:
        return HttpResponse(f'User: {data[1]}<br>Email: {data[2]}')
    else:
        return HttpResponse('User not found')
    
    
    


def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404("Sorry, that User not found")
    context = {'user': user}
    return render(request, 'user_details.html', context)




