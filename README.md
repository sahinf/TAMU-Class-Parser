# TAMU Class Parser
A quick python script for parsing specifically the .json file that loads Howdy Portal's classes..

# HOW-TO
Python code to parse the .json file manually obtained by inspecting a Class Search page on Howdy. Once you see all the classes you would like to parse through (1xx-3xx), go to inspect element and then into 'Network'. Then filter for 'XHR' and you will have the .json available for downloading

# Instructions to find the correct .json file
The instructions acquire the .json file through Firefox but any browser should work
1. Search for class or class range through Howdy

![Class Search](/images/classes.png)

2. Open up the inspect element

3. Navigate to "Network"

4. Filter by XHR (you may have to RELOAD the page). The type should be .json and the file name should look similar

![Inspect Element](/images/inspect.png)

5. double-click it and your browser should open up the .json in a new tab

![Json file](/images/json.png)

6. Right-click and save the page as "searchResults". the type should be .json
