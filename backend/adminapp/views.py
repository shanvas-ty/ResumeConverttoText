from django.shortcuts import render
import pymongo
from utils import get_db_handle,get_collection_handle
# Create your views here.

def home(request):
    return render(request,'index.html')

def dbconnectionUsers(collectionName):
    from django.conf import settings
    db_handle, mongo_client = get_db_handle('freegodb', 'localhost', '27017')
    # First define the database name
    dbname = mongo_client['freegodb']
    collection_name = dbname[collectionName]
    print(collection_name)
    print(type(collection_name))
    collection_handle = get_collection_handle(db_handle, collection_name.name)
    # Read the documents
    details = collection_handle.find({})
    return details

def userlist(request):
    details = dbconnectionUsers('users')
    # Print on the terminal
    print(details)
    can=0
    int=0
    com=0
    inst=0
    QA=0
    for r in details:
        print(r)
        if r['roles'][0] == 'recruitment-candidate':
            can+=1
        if r['roles'][0] == 'recruitment-interviewer':
            int+=1
        if r['roles'][0] == 'company':
            com+=1
        if r['roles'][0]=='institute':
            inst+=1
        if r['roles'][0] == 'Candidate':
            can+=1
        if r['roles'][0] == 'Questions Author':
            QA+=1
    print(int)
    context= { 'NumCandidate':str(can),
        'NumInterviewer':str(int),
        'NumCompany':str(com),
        'NumInstitute':str(inst),
        'NumQA':str(QA)}

    return render(request,'alluser.html',context)
def interviewerslist(request):
    details = dbconnectionUsers('users')
    # Print on the terminal
    print("data is:",details)
    int=0
    data={}
    for r in details:
        # print(r)
        user={}
        if r['roles'][0] == 'recruitment-interviewer':
            user['name']=(r['fullName'])
            user['mobile']=(r['userMobile'])
            user['email']=(r['email'])
            user['id']=r['_id']
            data[int]=user
            int += 1
    context= {
        'range':range(int),
        'data':data}
    print(context)
    return render(request,'interviewer.html',context)

def Candidatelist(request):
    details = dbconnectionUsers('users')
    # Print on the terminal
    print("data is:",details)
    can=0
    data={}
    for r in details:
        # print(r)
        user={}
        if r['roles'][0] == 'Candidate':
            user['name']=(r['fullName'])
            user['mobile']=(r['userMobile'])
            user['email']=(r['email'])
            user['id']=r['_id']
            data[can]=user
            can += 1
    context= {
        'range':range(can),
    'data':data}
    print(context)
    return render(request,'Candidate.html',context)
def CompanyList(request):
    details = dbconnectionUsers('users')
    # Print on the terminal
    print("data is:",details)
    can=0
    data={}
    for r in details:
        # print(r)
        user={}
        if r['roles'][0] == 'company':
            user['name']=(r['fullName'])
            user['mobile']=(r['userMobile'])
            user['email']=(r['email'])
            user['id']=r['_id']
            data[can]=user
            can += 1
    context= {
        'range':range(can),
    'data':data}
    print(context)
    return render(request,'Company.html',context)

def InstituteList(request):
    details = dbconnectionUsers('users')
    # Print on the terminal
    print("data is:",details)
    can=0
    data={}
    for r in details:
        # print(r)
        user={}
        if r['roles'][0] == 'institute':
            user['name']=(r['fullName'])
            user['mobile']=(r['userMobile'])
            user['email']=(r['email'])
            user['id']=r['_id']
            data[can]=user
            can += 1
    context= {
        'range':range(can),
    'data':data}
    print(context)
    return render(request,'Institute.html',context)

def QAuthorList(request):
    details = dbconnectionUsers('users')
    # Print on the terminal
    print("data is:",details)
    can=0
    data={}
    for r in details:
        # print(r)
        user={}
        if r['roles'][0] == 'Questions Author':
            user['name']=(r['fullName'])
            user['mobile']=(r['userMobile'])
            user['email']=(r['email'])
            user['id']=r['_id']
            data[can]=user
            can += 1
    context= {
        'range':range(can),
    'data':data}
    print(context)
    return render(request,'QuestionAuthor.html',context)


def Profile(request,userid):
    details = dbconnectionUsers('users')
    # Print on the terminal
    print("data is:",details)
    data={}
    confidential=['_id','password','__v','skill_id']
    for r in details:
        print(r)
        if str(r['_id']) == str(userid):
            for i in r:
                if i not in confidential:
                    data[i]=r[i]
    context= {
    'data':data}
    print(context)
    return render(request,'Profile.html',context)