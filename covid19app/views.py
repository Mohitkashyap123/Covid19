from django.shortcuts import render,HttpResponse
import requests
# Create your views here.
def index(request) :
    data = True
    result = None
    globalSummary = None
    countries = None
    while(data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            json = result.json()

            globalSummary = json['Global']
            countries = json['Countries']

            data = False
        except:
            data = True
    return render(request , 'covid19app/index.html' ,
                  {'globalSummary' : globalSummary ,
                   'countries' : countries})


def india(request) :
    data = True
    result = None
    countries = None
    while(data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            json = result.json()

            countries = json['Countries']
            India = countries[76]
            #print(India)
            data = False
        except:
            data = True

    # states data
    print("fun is called ")  
    data = True
    while(data):
        try:
            result = requests.get('https://api.covid19india.org/state_district_wise.json')
            json = result.json()
            data = False
        except:
            data = True
    #print(type(json))
    #print(type(json["Andhra Pradesh"]))
    #states = [key for key in json.keys()]
    #print(states)
    #print(len(states))
    #print(json["Andhra Pradesh"])
    state_name = "Andhra Pradesh"
    
    print(state_name)
    districts = json[state_name]['districtData']
    dist_name = [i for i in json[state_name]['districtData']]
    
    #print(f"this is : {state_name}")      
    return render(request , 'covid19app/india.html' ,
                  {'IndiaData' : India ,
                  'districtData' : districts                  
                   } )

def state(request) :
    data = True
    result = None
    countries = None
    while(data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            json = result.json()

            countries = json['Countries']
            India = countries[76]
            #print(India)
            data = False
        except:
            data = True

    # states data
    print("fun is called ")  
    data = True
    while(data):
        try:
            result = requests.get('https://api.covid19india.org/state_district_wise.json')
            json = result.json()
            data = False
        except:
            data = True
    #print(type(json))
    #print(type(json["Andhra Pradesh"]))
    #states = [key for key in json.keys()]
    #print(states)
    #print(len(states))
    #print(json["Andhra Pradesh"])
    state_name = "Rajasthan"
    state_name = str(request.GET.get('state')).strip()
    print(state_name)
    states = [key for key in json.keys()]
    if state_name not in state_name :
        return HttpResponse("")
    print("hello")
    print("hello")
    print("hello")
    print("hello")
    districts = json[state_name]['districtData']
    dist_name = [i for i in json[state_name]['districtData']]
    
    #print(f"this is : {state_name}")      
    return render(request , 'covid19app/state.html' ,
                  {'IndiaData' : India ,
                  'districtData' : districts,
                  'state_name' : state_name                 
                   } )