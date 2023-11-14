from django.shortcuts import render

def index (request):
  context = {
    'title':'Home',
    'posts':[
      {
       
        'date':'',
        'post_title':'',
        'post_description':'',
        'post_category': '',       
       },
       {
        
        'date':'',
        'post_title':'',
        'post_description':'',
        'post_category': '',       
       },
        {

        'date':'',
        'post_title':'',
        'post_description':'',
        'post_category': '',       
       },
    ],
    'quote':[
      {
        'image':'',
        'quote_descriptions':'',
        'quote_author':''
      }
      
    ]
    }
  
  return render (request, 'app_blog/index.html', context)

def about (request):
  context = {'title':'About'}
  return render (request, 'app_blog/about.html', context)


def styles (request):
  context = {'title':'Styles'}
  return render (request, 'app_blog/styles.html', context)


def contact (request):
  context = {'title':'Contact'}
  return render (request, 'app_blog/contact.html', context)