from home.models import SocialNetworks
from blog.models import Category

def SocialNetwork(request):
    result = SocialNetworks.objects.all()
    return {"Network": result}

def Categorys(request):
    categories = Category.objects.all()
    return {"categories": categories}