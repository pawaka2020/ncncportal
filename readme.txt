This is a web app meant to be used together with the NCNC Flutter app.
Previously a backend, but now upgraded to an actual internal staff portal.
This web app was previously based on Flask, but I have decided to migrate the framework to JustPy
for the following reasons:
1 - This web app will involve a lot of dynamic web pages. Flask does not inherently support building server-side web apps
necessary to generate dynamic web pages.
2 - To minimize the complexity from having two bodies of client-side and server-side code when we already have the existing complexity
of synchronizing the code of this web app with the code of the NCNC Flutter app.
3 - JustPy is a sufficiently mature web application to handle the tasks to be done by this web app.
4 - JustPy allows the much more intuitive creation of UI elements top-down rather than left-right that HTML forces users to do.
5 - JustPY allows creation of html and css via Python functions, but we can still use html and css just-in-case if required.
6 - Server-side web apps are simply more secure due to reasons ie increased security from XSS attacks. This will be a web app
that involves order tracks and money transactions, So security is paramount.
Libraries used to create this backend:
JustPy
Mongodb

How to set up:

1. Download and install Mongodb https://www.mongodb.com/try/download/community
2. Change the IPV4_ADDRESS value in config.py to IPV4 address of the internet connection of local machine.
3. Make sure MONGODB_HOST value in models/mongodb/db.py is set to 'mongodb://localhost:27017/' or whichever value matches the MongoDB Compass' localhost value
5. Type 'python app.py' on terminal to launch this backend.
6. If everything goes well, you should be able to see a webpage that shows 'NCNC Backend' on <IPV4_ADDRESS>:5000
(for example, http://192.168.1.40:5000)

Link to JustPy framework: https://justpy.io/