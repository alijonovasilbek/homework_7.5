from django.urls import path
from .views import (base,prize,
                    add_prize,prize_edit,
                    prize_detail,prize_delete,
                    physics,literature,chemistry,

                    )


urlpatterns=[
    path('',base,name="base"),
    path('prizes/',prize,name="prizes"),
    path('<int:pk>/',prize_detail,name="prize_info"),
    path('add/',add_prize,name="add_prize"),
    path('edit/<int:pk>',prize_edit,name='edit_prize'),
    path('delete/<int:pk>',prize_delete,name='delete_prize'),
    path('physics/',physics,name='physics'),
    path("literature/",literature,name="liter"),
    path("chemistry/", chemistry, name="chemis"),


]

LOGIN_REDIRECT_URL = '/prizes/'