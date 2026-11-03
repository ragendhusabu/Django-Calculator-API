from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View 
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator 
from json import loads
# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class AdditionView(View):
    def post(self,request):
        request_body =request.body
        form_data =loads(request_body)#convert json to dict
        n1=form_data.get('num1')
        n2=form_data.get('num2')
        result =n1+n2
        print(request_body)

        data ={
            'sum' :result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class SubtractionView(View):
    def post(self,request):
        data =request.body
        form_data =loads(data)
        n1 =form_data.get('num1')
        n2= form_data.get('num2')
        difference =n1=n2
        difference_data ={
            "Difference": difference
        }
        return JsonResponse(difference_data)

@method_decorator(csrf_exempt,name='dispatch')
class MultiplicationView(View):
    def post(self,request):
        data =request.body
        form_data =loads(data)
        n1 =form_data.get('num1')
        n2= form_data.get('num2')
        product =n1*n2
        product_data ={
            "result" : product
        }
        return JsonResponse(product_data)

@method_decorator(csrf_exempt,name='dispatch')
class DivisionView(View):
    def post(self,request):
        data =request.body
        form_data =loads(data)
        n1 =form_data.get('num1')
        n2= form_data.get('num2')
        division =n1/n2
        division_data ={
            "result" : division
        }
        return JsonResponse(division_data)

@method_decorator(csrf_exempt,name='dispatch')
class ModulousView(View):
    def post(self,request):
        data =request.body
        form_data =loads(data)
        n1 =form_data.get('num1')
        n2= form_data.get('num2')
        mod =n1%n2
        mod_data ={
            "result" : mod
        }
        return JsonResponse(mod_data)
    
@method_decorator(csrf_exempt,name='dispatch')
class PercentageView(View):
    def post(self,request):
        data =request.body
        form_data =loads(data)
        n1 =form_data.get('obtained_marks')
        n2= form_data.get('total_marks')
        percentage =(n1/n2)*100
        percentage_data ={
            "result" : percentage
        }
        return JsonResponse(percentage_data)

@method_decorator(csrf_exempt,name='dispatch')
class bmiView(View):
    def post(self,request):
        data =request.body
        form_data =loads(data)
        w =form_data.get('weight')
        height= form_data.get('height')
        h= height/100

        bmi =w/(h**2)
        bmi_data ={
            "BMI" : bmi
        }
        return JsonResponse(bmi_data)
    
@method_decorator(csrf_exempt,name='dispatch')
class AreaView(View):
    def post(self,request):
        data =request.body
        form_data =loads(data)
        l =form_data.get('length')
        b= form_data.get('breadth')
    
        area =l*b
        area_data ={
            "Area of recangle" : area
        }
        return JsonResponse(area_data)

@method_decorator(csrf_exempt,name='dispatch')
class AgeView(View):
    def post(self,request):
        data =request.body
        form_data =loads(data)
        birth_year =form_data.get('birth_year')
        current_year= form_data.get('current_year')
    
        age =current_year-birth_year
        age_data ={
            "Age of the person is" : age
        }
        return JsonResponse(age_data)

@method_decorator(csrf_exempt,name='dispatch')
class SimpleInterestView(View):
    def post(self,request):
        data =request.body
        form_data =loads(data)
        p =form_data.get('principal')
        t= form_data.get('time')
        r =form_data.get('rate')
    
        simple_interest =(p*t*r)//100
        interest_data ={
            "principal" : 10000,
            "rate"      :5,
            "time"      :2,
            "simple_interest" :simple_interest
        }
        return JsonResponse(interest_data)

@method_decorator(csrf_exempt,name='dispatch')
class ElectricityBillView(View):
    def post(self,request):
        data =request.body
        form_data =loads(data)
        units =form_data.get('units')
        rate= form_data.get('rate')
        e_bill =units*rate
        bill_data ={
                "units" :212,
                "rate"  :6,
                "e-bill":e_bill
        }
        return JsonResponse(bill_data)