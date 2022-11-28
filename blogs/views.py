from django.shortcuts import render,redirect
from django.utils import timezone
from django.db.models import Q
import pytz
from django.http import HttpResponse
from .models import Blog,Tags,Comment,ReactionHistory
from textblob import TextBlob
from django.contrib.auth.decorators import login_required
#importing forms
from django.contrib import messages
from .forms import BlogForm,CommentForm,ReportForm
from users.models import Profile
import datetime
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage



#READ-
def home(request):
    
    if request.user.is_authenticated:
        user=request.user
        try:
            profile=user.profile
        except:
            profile=None
        
        
        
        if profile:
            interests=profile.interests.all()
            
            interests_list=[]
            for item in interests:
                interests_list.append(item.title)
            
  
    
            blogs_of_interests=Blog.objects.filter(tags__title__in=interests_list)[0:50]
    
            

        
    
            today = datetime.datetime.now(tz=timezone.utc)
            quarter_ago = today - datetime.timedelta(days=15)
            blogs = Blog.objects.filter(created_on__gte=quarter_ago,)[0:1000]
            records = (blogs | blogs_of_interests).distinct()
            results=12
            #results is max number of model view into the template
            #divided into pages
            paginator=Paginator(records,results)
            try:
                #getting a particular page from query parameter
                #getting page from url
                page=request.GET.get('page')

                #getting the particular page
                #particular subsection of the queryset
                records=paginator.page(page)
                print(f"\n\n\n\n\n{type(records.number)}\n\n\n\n")
                #it will have a number
            except PageNotAnInteger:
                page=1
                records=paginator.page(page)
            except EmptyPage:
                page=paginator.num_pages
                records=paginator.page(page)
            print("\n\n\n\n\n\n\n",{"data":records.number},"\n\n\n\n\n\n\n")
            context={'blogs':records,'paginator':paginator,'current':page}
            return render(request,"blogs/home.html",context)
        
        else:
              today = datetime.datetime.now(tz=timezone.utc)
              quarter_ago = today - datetime.timedelta(days=15)
              blogs = Blog.objects.filter(created_on__gte=quarter_ago,)[0:300]
              records = blogs
              results=12
              paginator=Paginator(records,results)
              try:
                    page=request.GET.get('page')
                    records=paginator.page(page)
              except PageNotAnInteger:
                    page=1
                    records=paginator.page(page)
              except EmptyPage:
                    page=paginator.num_pages
                    records=paginator.page(page)

              context={'blogs':records,'paginator':paginator,'current':page}
              return render(request,"blogs/home.html",context)
             

            
        
    else:

        today = datetime.datetime.now(tz=timezone.utc)
        quarter_ago = today - datetime.timedelta(days=15)
        blogs = Blog.objects.filter(created_on__gte=quarter_ago,)[0:300]
        records = blogs
        results=12
        paginator=Paginator(records,results)
        try:
                    page=request.GET.get('page')
                    records=paginator.page(page)
        except PageNotAnInteger:
                    page=1
                    records=paginator.page(page)
        except EmptyPage:
                    page=paginator.num_pages
                    records=paginator.page(page)
        
        context={'blogs':records,'paginator':paginator,'current':page}
        return render(request,"blogs/home.html",context)
   

#see a project into a single page
@login_required(login_url="login")
def showblog(request,pk):
    blogs=Blog.objects.get(id=pk)
    comments=Comment.objects.filter(blog=blogs)
    print(comment)
    form=CommentForm()

    
    
    
    context={'data':blogs,'comment':comments,'form':form}
    return render(request,"blogs/single_project.html",context)



#New Page
#CREATE
@login_required(login_url="login")
def newblog(request):
    
    form=BlogForm()
    if request.method=="POST":

        content=request.POST['content']
        updated_request = request.POST.copy()

        

        from textblob import TextBlob

        summaryblob=TextBlob(content)

        summarySentiment=summaryblob.sentiment
        
        analysis=f"<Polarity:  {summarySentiment.polarity}>  <Subjectivity:   {summarySentiment.subjectivity}>"
   
        updated_request['analysis']=analysis
        writer=Profile.objects.get(user=request.user)

        updated_request['analysis']=analysis
        updated_request['writer']=writer
        print(updated_request)
        form = BlogForm(updated_request, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('/')
        
    
        title=request.POST['title']
        content=request.POST['content']
        voted=request.POST['voted']
        username = request.user.username
        Blog.objects.create(title=title,author=username,
        content=content,voted=voted)


        
   
        
    else:
        
        return render(request,"blogs/newblog.html",{'form':form})


@login_required(login_url="login")
def updateblog(request,pk):
    blog=Blog.objects.get(id=pk)
    if request.user==blog.writer.user:
    
        #fetchin the particular blog for passing as an instance
       
        form=BlogForm(instance=blog)
        #=if the method is a post method
        if request.method=="POST":
            #method------------------
            content=request.POST['content']
            updated_request = request.POST.copy()

        

            from textblob import TextBlob

            summaryblob=TextBlob(content)

            summarySentiment=summaryblob.sentiment
            analysis=f"<Polarity:  {summarySentiment.polarity}>  <Subjectivity:   {summarySentiment.subjectivity}>"
            
            updated_request['analysis']=analysis
           
            writer=Profile.objects.get(user=request.user)

            updated_request['analysis']=analysis
            updated_request['writer']=writer
            form = BlogForm(updated_request, request.FILES,instance=blog)
            
            if form.is_valid():
                
                form.save()
                return redirect ('/')
        
          
        
        else:
            return render(request,"blogs/newblog.html",{'form':form})

    else:
        messages.error(request,"Invalid Request")
        return redirect("/")


@login_required(login_url="login")
def deleteblog(request,pk):




    blog=Blog.objects.get(id=pk)
    if request.user==blog.writer.user:
    #=if the method is a post method
        if request.method=="POST":
            blog.delete()
            return redirect("home")

    
        #method1
        else:
    
            return render(request,'blogs/delete.html',{'obj':blog})
    else:
        messages.error(request,"Invalid Request")
        return redirect("/")

        

@login_required(login_url="login")

def rate1(request,pk):
    #
    user=request.user
    
    data=Blog.objects.get(id=pk)
    profile=Profile.objects.get(user=user)
  
    #
    reaction=ReactionHistory.objects.filter(blog=data,profile=profile).first()
    
    if reaction:
       
        if reaction.status==False:
            rate=data.rate
            rate=rate+90
            voted=data.voted
            voted+=1
            rate=rate/voted
            data.voted=voted
            data.rate=rate
            data.save()
            reaction.status=True
            reaction.save()
            return redirect("/")
        else:
            return redirect("/")
    else:
            rate=data.rate
            rate=rate+90
            voted=data.voted
            voted+=1
            rate=rate/voted
            data.voted=voted
            data.rate=rate
            data.save()
            ReactionHistory.objects.create(blog=data,profile=profile,status=True)
            return redirect("/")



@login_required(login_url="login")
def rate2(request,pk):
   #
    user=request.user
    
    data=Blog.objects.get(id=pk)
    profile=Profile.objects.get(user=user)
  
    #
    reaction=ReactionHistory.objects.filter(blog=data,profile=profile).first()
    print("----------------------")
    print({"reaction":reaction})
    print("----------------------")
    if reaction:
        if reaction.status==False:
            rate=data.rate
            rate=rate+70
            voted=data.voted
            voted+=1
            rate=rate/voted
            data.voted=voted
            data.rate=rate
            data.save()
            reaction.status=True
            reaction.save()
            return redirect("/")
        else:
            return redirect("/")
    else:
            rate=data.rate
            rate=rate+70
            voted=data.voted
            voted+=1
            rate=rate/voted
            data.voted=voted
            data.rate=rate
            data.save()
            ReactionHistory.objects.create(blog=data,profile=profile,status=True)
            return redirect("/")

@login_required(login_url="login")
def rate3(request,pk):
   #
    user=request.user
    
    data=Blog.objects.get(id=pk)
    profile=Profile.objects.get(user=user)
  
    #
    reaction=ReactionHistory.objects.filter(blog=data,profile=profile).first()
    if reaction:
        if reaction.status==False:
            rate=data.rate
            rate=rate+10
            voted=data.voted
            voted+=1
            rate=rate/voted
            data.voted=voted
            data.rate=rate
            data.save()
            reaction.status=True
            reaction.save()
            return redirect("/")
        else:
            return redirect("/")
    else:
            rate=data.rate
            rate=rate+10
            voted=data.voted
            voted+=1
            rate=rate/voted
            data.voted=voted
            data.rate=rate
            data.save()
            ReactionHistory.objects.create(blog=data,profile=profile,status=True)
            return redirect("/")



#new comment
@login_required(login_url="login")
def comment(request,pk):
    
    blog=Blog.objects.get(id=pk)
    comment=request.POST["comment"]
    user_profile=request.user
    profile=Profile.objects.get(user=user_profile)
    Comment.objects.create(comment=comment,commentor=profile,blog=blog)
  
    return redirect("show",pk=blog.id)

#report
#new comment
@login_required(login_url="login")
def report(request,pk):
    form=ReportForm()
    if request.method=="POST":

        form=ReportForm(request.POST,request.FILES)
        
        if form.is_valid():
            
            try:
                data=form.save(commit=False)
                reported_by=request.user.profile
                blog=Blog.objects.get(id=pk)
                data.reported_by=reported_by
                data.blog=blog
                data.save()
                return redirect("/")
            except:
                messages.error(request,"A review already exists")
                return redirect("/")
        else:
            messages.error(request,"A review already exists")
            return redirect("/")

    
    context={"form":form}
    return render(request,'blogs/report.html',context)
     
    
#search function
def search(request):
    #from django.db.models import Q
    search_query=''
    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')
    #blogs1=Blog.objects.filter(title__icontains=search_query)
    #blogs2=Blog.objects.filter(content__icontains=search_query)
    #blogs = (blogs1 | blogs2).distinct()
    tags=Tags.objects.filter(title__exact=search_query)
    profile=Profile.objects.filter(username__icontains=search_query)
    blogs=Blog.objects.filter(
    Q(title__icontains=search_query) |
    Q(content__icontains=search_query)|
    Q(writer__username__icontains=search_query)|
    Q(tags__in=tags)
    ).distinct()
    #Q(writer__in=profile)
    #or
    #Q(writer__username__icontains=search_query)
    
    #results=3

    #paginator=Paginator(blogs,results)
    #page=request.GET.get('page')
 
    #try:
        
        #blogs=paginator.page(page)
    #except PageNotAnInteger:
        #page=1
        #blogs=paginator.page(page)
    #except EmptyPage:
        #page=paginator.num_pages
        #blogs=paginator.page(page)
  
    #blogs=paginator.page(page)
    
    context={'blogs':blogs,'search_query':search_query}#'paginator':paginator

    return render(request,"blogs/search.html",context)


