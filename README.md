# TAMU Class Parser
A quick python script for parsing specifically the .json file that loads Howdy Portal's classes.

# Instructions
1. Go to Howdy and search for the class/class range that would like to parse
![Class Search](/images/classes.png)

2. Open up the inspect element

3. Navigate to "Network"

4. Filter by XHR (you may have to RELOAD the page). The type should be .json and the file name should look similar

![Inspect Element](/images/inspect.png)

5. double-click it and your browser should open up the .json in a new tab

![Json file](/images/json.png)

6. Right-click and save the page as "searchResults". The type should be '.json'. the full file name.type should be "searchResults.json"

7. The output will be a formatted .csv file for exporting into better formats
