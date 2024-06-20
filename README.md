# http_server

<h1>HTTP Server(Personal project)</h1>

 

<h2>Description</h2>
This project is a HTTP server wrote using python. It was my first major challenge to myself after college ended.<br />
I used a lot of online resources to help me write this, and used modules such as sys, which I had used briefly before and os, and socket were brand new to me.
<br />


<h2>Languages and Utilities Used</h2>

- <b>python</b> 
- <b>sys</b> 
- <b>os</b>
- <b>socket</b>


<h2>Environments Used </h2>

- <b>Windows 10
- <b>VS Code</b>

<h2>Program walk-through:</h2>

<p align="left">
This function initializes and runs the HTTP server, listening for incoming connections on a specified port. It accepts and processes client connections in an infinite loop, handling graceful shutdown on keyboard interrupt: <br/>
<img src="https://imgur.com/43hNIJo.png" height="80%" width="80%" alt="Home Page"/>
<br />
<br />
This function handles a single client's request by reading the request data from the socket, parsing it, and then generating and sending back an appropriate response. It also includes error handling for malformed requests:  <br/>
<img src="https://imgur.com/j7MLxUJ.png" height="80%" width="80%" alt="Products page"/>
<br />
<br />
This function parses the raw HTTP request data to extract and return the request path, user agent, method, headers, and body. It splits the request into lines, processes the headers, and identifies the body content, ensuring the request line has the correct format: <br/>
<img src="https://imgur.com/cUuFA3L.png" height="80%" width="80%" alt="User login page"/>
<br />
<br />
This function generates an appropriate HTTP response based on the request path, method, and other details. It handles various paths including root, echo, user-agent, and file operations (GET and POST), returning the correct HTTP status and response content:  <br/>
<img src="https://imgur.com/Fg9z6sk.png" height="80%" width="80%" alt="Cart page"/>
<br />
<br />

</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
