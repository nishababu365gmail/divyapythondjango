from django import template
register = template.Library()
def modify_name(value):
    sum=0
    for item in value:
        sum=sum+int(item['population'])
        
    return sum
    
register.filter('modify_name', modify_name)