from BartendingRefresher.models import Ingredient

a1 = Ingredient(Ingredient = 'Vokda', Type = 'Al')
a2 = Ingredient(Ingredient = 'Tequila', Type = 'Al')
l1 = Ingredient(Ingredient = 'Kahlua', Type = 'Li')

a1.save()
a2.save()
l1.save()
