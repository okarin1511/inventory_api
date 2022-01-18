from django.urls import path
from .views import AllBoxesView, CreateBoxesView, UpdateBoxDetails, MyBoxesView, DeleteBox

urlpatterns = [
    # path('box_list/', box_list),
    path('box_list/', AllBoxesView.as_view()),
    path('create_box/', CreateBoxesView.as_view()),
    path('details/<int:id>/', UpdateBoxDetails.as_view()),
    path('my_boxes/', MyBoxesView.as_view()),
    path('delete/<int:id>/', DeleteBox.as_view())

]