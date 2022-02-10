from django.urls import path
from .views import say_hello, say_bye

# urlpatters
urlpatterns = [
    # trailing slash
    # SEO
    # hello/ 
    #      hello  -> hello/ 
    #      hello/ -> hello/ 
    # http://127.0.0.1:8000/ homepage

    # just http://127.0.0.1:8000/playground/hello/
    # just http://127.0.0.1:8000/playground/hello/ 
    path('hello/', say_hello),
    # just http://127.0.0.1:8000/playground/hello1
    path('hello1', say_hello),
    path('hello2/', say_hello),
    path('bye/', say_bye)
]