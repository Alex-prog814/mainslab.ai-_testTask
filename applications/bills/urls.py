from django.urls import path

from applications.bills.views import BillCreateView, BillListView, BillDocCreateView

urlpatterns = [
    # for create with xlsx
    path('create_doc/', BillDocCreateView.as_view()),
    # for single bill create
    path('create/', BillCreateView.as_view()),
    path('', BillListView.as_view()),
]