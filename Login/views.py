from django.shortcuts import render,redirect
from .models import card
from django.views.decorators.cache import never_cache


#Create your views here.

@never_cache 
def index(request):

        if request.method=='POST':
            username = request.POST['username']
            password = request.POST['password']

            if username=='muhammedshiyas' and password=='1':

                request.session['name']=username
                item1 = card()
                item1.img = "https://static.toiimg.com/thumb/msid-81094145,width-400,resizemode-4/81094145.jpg"
                item1.title ="Hyderbad"
                item1.dis = "First Biriyani,Then Shervani."
            


                item2 = card()
                item2.img = "https://cdn.britannica.com/26/84526-050-45452C37/Gateway-monument-India-entrance-Mumbai-Harbour-coast.jpg"
                item2.title ="Mumbai"
                item2.dis = "The city that never sleeps."
                


                item3 = card()
                item3.img = "https://static.toiimg.com/photo/msid-78100845,width-96,height-65.cms"
                item3.title ="Kerala"
                item3.dis = "Gods Own Country."

                item4 = card()
                item4.img = "https://www.tourmyindia.com/socialimg/jaipur-tourism-rajasthan.jpg"
                item4.title ="Jaipur"
                item4.dis = "The pink city."
                


                item5 = card()
                item5.img = "https://cdn.britannica.com/37/189837-050-F0AF383E/New-Delhi-India-War-Memorial-arch-Sir.jpg"
                item5.title ="New Delhi"
                item5.dis = "The capital of India."
                


                item6 = card()
                item6.img = "https://upload.wikimedia.org/wikipedia/commons/7/70/Neeulm_Valley_AJK_%28Arang_Kel%29.jpg"
                item6.title ="Kashmir"
                item6.dis = "Heaven."
                
                item = [item1,item2,item3,item4,item5,item6]
                return render(request,'home2.html',{'item':item})
            else:
                 error='invalid username and password'
                 return render(request,'index.html', {'error':error})
            
        else:

            if request.session.get('name'):
                item1 = card()
                item1.img = "https://static.toiimg.com/thumb/msid-81094145,width-400,resizemode-4/81094145.jpg"
                item1.title ="Hyderbad"
                item1.dis = "First Biriyani,Then Shervani."
            
 

                item2 = card()
                item2.img = "https://cdn.britannica.com/26/84526-050-45452C37/Gateway-monument-India-entrance-Mumbai-Harbour-coast.jpg"
                item2.title ="Mumbai"
                item2.dis = "The city that never sleeps."
                


                item3 = card()
                item3.img = "https://static.toiimg.com/photo/msid-78100845,width-96,height-65.cms"
                item3.title ="Kerala"
                item3.dis = "Gods Own Country."

                item4 = card()
                item4.img = "https://www.tourmyindia.com/socialimg/jaipur-tourism-rajasthan.jpg"
                item4.title ="Jaipur"
                item4.dis = "The pink city."
                


                item5 = card()
                item5.img = "https://cdn.britannica.com/37/189837-050-F0AF383E/New-Delhi-India-War-Memorial-arch-Sir.jpg"
                item5.title ="New Delhi"
                item5.dis = "The capital of India."
                


                item6 = card()
                item6.img = "https://upload.wikimedia.org/wikipedia/commons/7/70/Neeulm_Valley_AJK_%28Arang_Kel%29.jpg"
                item6.title ="Kashmir"
                item6.dis = "Heaven."
                
                item = [item1,item2,item3,item4,item5,item6]
                return render(request,'home2.html',{'item':item})

            else:
                 return render(request,'index.html')

        
           
       
    

@never_cache
def logout(request):
    
    del request.session['name']
    return redirect('/')



# @never_cache 
# def index(request):
#     if request.session
#     return render(request, "index.html")        







