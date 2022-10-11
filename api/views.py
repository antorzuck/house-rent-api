from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from django.shortcuts import render

def home(request):
	return render(request, 'docx.html')



@api_view(['GET', 'POST'])
def get_homes(request):
    houses = House.objects.all()
    s = HouseS(houses, many=True, context={'request': request})

    return Response(s.data)
@api_view(['GET', 'POST'])
def get_thumbnail(request, id):
    house = House.objects.get(id=id)
    image = Img.objects.filter(house=house)
    s = ImgS(image, many=True)
    return Response(s.data)
    
    
@api_view(['GET', 'POST'])
def create_house(request):
	if request.method == 'POST':
		name = request.data.get('house_name')
		price = request.data.get('rent_price')
		size = request.data.get('house_size')
		loc = request.data.get('location')
		bed = request.data.get('bedroom')
		bath = request.data.get('bathroom')
		img = request.FILES.getlist('image')
		
		c = House.objects.create(house_name=name, rent_price=price, house_size=size, location=loc, bedroom=bed, bathroom=bath, image=img[0])
		c.save()
		
		for i in img:
			cc = Img.objects.create(images=i, house=c)
		
		return Response({'msg': "house added.."})


@api_view(['GET', 'POST'])
def delete_house(request, id):
	if request.method == "POST":
		dh = House.objects.get(id=id)
		dh.delete()
		return Response({"msg" : "data deleted"})
	return Response({'msg':'method not allowed'})

@api_view(['GET', 'POST'])
def details(request, id):
    d = House.objects.get(id=id)
    sr = HouseS(d, many=False,context={'request': request})
    return Response(sr.data)


@api_view(['POST'])
def update(request, id):
    gh = House.objects.get(id=id)
    if request.data.get('house_name'):
    	gh.house_name = request.data.get('house_name')
    if request.data.get('rent_price'):
    	gh.rent_price = request.data.get('rent_price')
    if request.data.get('house_size'):
    	gh.house_size = request.data.get('house_size')
    if request.data.get('location'):
    	gh.location = request.data.get('location')
    if request.data.get('bedroom'):
    	gh.bedroom = request.data.get('bedrooom')
    if request.data.get('bathroom'):
    	gh.bathroom = request.data.get('bathroom')
    
    if request.FILES.get('image'):
    	gh.image = request.FILES.get('image')
    gh.save()
    return Response({'msg':'data uodated'})


