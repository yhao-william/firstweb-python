from django.db import models
from myapp.models import TouHou

th1 = TouHou(name='Touhou 1', release_date='1996-05-05', game_id='001', game_type='Shooter')
th1.save()

