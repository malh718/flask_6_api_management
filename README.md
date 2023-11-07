# flask_6_api_management



## 1. Flask-based RESTful API:
Utilize Flask to develop an endpoint that can handle a simple GET request.
The response should be in JSON format. 

The class example the format is
https://jsonplaceholder.typicode.com/posts/1

As the screenshot shows, and endpoint was developed and a GET request was implemented as shown in the screenshot.

<img width="666" alt="Screen Shot 2023-11-07 at 2 39 25 PM" src="https://github.com/malh718/flask_6_api_management/assets/102617334/533aa9f7-632b-404c-8542-54d65755bcb8">



I also did the same thing with the phrase "Hello from MALIHAS Flask API Endpoint Server" as shown below.

https://5000-cs-741144739238-default.cs-us-east1-rtep.cloudshell.dev/?authuser=0


<img width="982" alt="Screen Shot 2023-11-07 at 2 48 56 PM" src="https://github.com/malh718/flask_6_api_management/assets/102617334/d0bd6d99-6beb-41da-976a-8e32a78f3242">



<img width="1162" alt="Screen Shot 2023-11-07 at 2 49 31 PM" src="https://github.com/malh718/flask_6_api_management/assets/102617334/06925c8f-7814-44dc-a7e5-d002afdd481c">

My code is shown in the screen shot below.

<img width="972" alt="Screen Shot 2023-11-07 at 2 43 28 PM" src="https://github.com/malh718/flask_6_api_management/assets/102617334/da969b71-6000-421e-b873-ee3f76041b50">

This is the url when you change authuser to hello
https://5000-cs-741144739238-default.cs-us-east1-rtep.cloudshell.dev/hello
<img width="722" alt="Screen Shot 2023-11-07 at 2 55 52 PM" src="https://github.com/malh718/flask_6_api_management/assets/102617334/b720b842-49c3-489b-a835-d9c803e9e430">

This is the url and it shows the name " Hello Rameama " 
In order to do this at the end of the URL after hello, i put ?name=rameama
https://5000-cs-741144739238-default.cs-us-east1-rtep.cloudshell.dev/hello?name=rameama
<img width="1170" alt="Screen Shot 2023-11-07 at 2 58 49 PM" src="https://github.com/malh718/flask_6_api_management/assets/102617334/6fb76bcf-4c10-46e7-8c88-63fcb96c395d">

## 2. Azure API deployment:
I deployed this through GCP because I do not have anymore Azure credits. In order to do this I followed the instructions that were present in the assignment.

2. GCP Cloud Functions API deployment:
I used this link to help me deploy. http function: https://cloud.google.com/functions/docs/create-deploy-http-python

My first step was creating a repo in github which I named flask_6_api_management.

I cloned that in my Google CLI.

From here I made an main.py file,  and copied in the appropriate code from week6.
Next I created a requirements.txt file which contained function_framework==3/*.

From there I have to build and test the function locally, which I did by copying and pasting in pip install -r requirements.txt
PATH=$PATH:~/.local/bin. and also with the function framwwork which is functions-framework-python --target-http

Thankfully from here I was able to visit my function and again where I see the screenshot above

URL:https://5000-cs-430379961417-default.cs-us-east1-rtep.cloudshell.dev/?authuser=1&redirectedPreviously=true
<img width="710" alt="Screen Shot 2023-11-07 at 3 41 22 PM" src="https://github.com/malh718/flask_6_api_management/assets/102617334/c9954ccb-89b1-4d26-9bb8-eaae85b5465a">

Next we have to deploy the function:

In order to do this I used a combination of the instructions given by google and also how to deploy an app present in HHA 504 week 2. 

At this point I had already had my cloud platform project and it was called flaskenddeploy with a project ID under the same  name.

My next steps were:
gcloud projects list
gcloud config set project [Flaskenddeploy]

*** It was at this point I realized I did not have a .yaml file so I created that and 
made sure I was in the right directory which was flask_6_api_management

<img width="1056" alt="Screen Shot 2023-11-07 at 4 24 15 PM" src="https://github.com/malh718/flask_6_api_management/assets/102617334/dca40505-661d-415a-b871-3f3278941ea2">

After that was completed I had to input gcloud app deploy, and it succesfully deployed on GCP.  As shown by a screenshot of the traffic below.

<img width="1096" alt="Screen Shot 2023-11-07 at 3 20 22 PM" src="https://github.com/malh718/flask_6_api_management/assets/102617334/b4c998df-ce71-43a4-80a3-3bb92df9911f">


Errors deploying:

At this point I ran into a couple of issues deploying on GCP.

<img width="687" alt="Screen Shot 2023-11-07 at 4 28 26 PM" src="https://github.com/malh718/flask_6_api_management/assets/102617334/5c84c088-1959-4918-88ee-908b21549d5f">


Once I did app deploy it brought me to the choose the region where you are located, and I chose 18. Then when ERROR: (gcloud.app.deploy) PERMISSION_DENIED: The caller does not have permission

I was really confused by this, and when I put that error into stackoverflow it said that I had to go into my Google Cloud and into the IAM and admin page. From here I went to grant access to my personal email which I have in my google CLI. However, no matter what I did or how many times I reloaded or tried to redeploy it would not work.

At this point I switched into my stonybrookemail for the cloud shell , opened another tab with another google Cloud shell, cloned my github repo, and when I went to deploy the app there were no issues with permissions and it deployed succesfully as shown by the screenshot below. 

<img width="817" alt="Screen Shot 2023-11-07 at 4 30 42 PM" src="https://github.com/malh718/flask_6_api_management/assets/102617334/a03d6252-fb95-4ce9-a576-a9eec29f1f2f">


## 3. OpenAPI Specification and Documentation:

For the final step,I made sure to pip install flasgger and add the Swagger(app) line of code into my main.py file.
I ran the requirements.txt file. pip install -r requirements.txt
For this portion where you have to do the docstring documentation it is important that you have all your proper parameters set and to make sure the indentation is correct. It should look like this   """
    This endpoint returns a greeting message.
    ---
    parameters:
      - name: name
        in: query
        type: string
        required: false
        default: World
    responses:
      200:
        description: A greeting message
    """

Docstring documentation file:
<img width="993" alt="Screen Shot 2023-11-07 at 4 59 07 PM" src="https://github.com/malh718/flask_6_api_management/assets/102617334/492aad0a-354b-4510-90d9-5e056c9ede5e">

<img width="970" alt="Screen Shot 2023-11-07 at 5 01 41 PM" src="https://github.com/malh718/flask_6_api_management/assets/102617334/794f0b83-e698-4551-bde6-f8dec023a042">

<img width="950" alt="Screen Shot 2023-11-07 at 5 03 27 PM" src="https://github.com/malh718/flask_6_api_management/assets/102617334/5c89699b-0266-4b4d-ac4e-87717dd2da43">

<img width="959" alt="Screen Shot 2023-11-07 at 5 03 11 PM" src="https://github.com/malh718/flask_6_api_management/assets/102617334/dc029448-9cd7-48b6-bfc7-0b4004323fcb">

Potential errors for #3: 

So initally this didnt work for me and I couldnt figure out what I was doing wrong. Turns out I was missing a part of the code and the spacing was off and that is why it showed me no operations. However, once I went back into my main.py and corrected everything it went through. 

<img width="878" alt="Screen Shot 2023-11-07 at 5 07 53 PM" src="https://github.com/malh718/flask_6_api_management/assets/102617334/7f495a2d-7844-463a-b4fa-c8ff1c4592bc">


