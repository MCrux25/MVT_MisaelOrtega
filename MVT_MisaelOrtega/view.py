from django.http import HttpResponse
from django.template import loader



def homie(self):
    data = {'name': 'Julia', 'age': '28', 'zodiac':'piscis'}
    plantilla = loader.get_template('static/index.html')
    documento = plantilla.render(data)
    return HttpResponse (documento)

