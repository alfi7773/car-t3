from django import template

register = template.Library()

@register.filter
def unique_years(cars):
    years = set()
    for car in cars:
        if car.year and car.year != 0:
            years.add(car.year)
    return sorted(years, reverse=True)