from django.conf.urls import url, include
import hello_app.views

urlpatterns = [
    url(r'^hello$', hello_app.views.hello),
    url(r'^db_test$', hello_app.views.test_db),
    url(r'^json_test$', hello_app.views.test_json),
]