{% include nav.html %}
# Create Task Plan
Local Showtimes

Part A

| Section | Question | Answer | 
| --- | --- | --- |
| i| Describe the overall purpose of the program | The purpose of the program is to display movie showings in certain theatres based on a zip code that the user inputs. The information will be shown in an organized table. This information that will be displayed is the movie name, movie genres, and the location/showtimes of that specific movie.  |
| ii| Describes what functionality of the program is demonstrated in the video| The video shows the user inputting a zip code and the API returning showtimes and locations based on that input. It also demonstrates the local storage updates, as a list is created of past zip code searches. |
| iii| Describes the input and output of the program demonstrated in the video| Input is a zip code between values 1 and 99999, and the output is a table of information about movies, genres, showtimes, and locations. |

Part B

| Section | Question | Answer | 
| --- | --- | --- |
| i | The first program code segment must show how data have been stored in the list. |![image](https://user-images.githubusercontent.com/50186752/165035232-a2a18cc7-9d80-4a7a-afb7-a22e057bc92c.png)This shows a function that adds the data from zipcode variable and pushes it to the end of the zipHistory list.|
| ii| The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose.| ![image](https://user-images.githubusercontent.com/50186752/165027534-6fad75e0-f4af-4532-98bd-cb563f3b245c.png)In the second part of the program we are checking to see if the list isn't empty and splitting up the data stored with commas to make it more readable for the user.|
| iii | Identifies the name of the list being used in this response| ``` zipHistory ``` is the name of the list being analyzed and rewritten in this function.|
| iv | Describes what the data contained in the list represent in your program| The data in the list represents all past zip code inputs that the user has made, showing only the last 3.|
| v | Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list| The list manages the complexity of the program because it stores the history of the zip codes in an efficient way that will help a user see their latest searches. If we did not use a list for this, it would be difficult to reference the zip codes in the rest of the program, and would make it more difficult to display a neat history. |

Part C

| Section | Question | Answer | 
| --- | --- | --- |
| i| The first program code segment must be a student-developed procedure that: Defines the procedure’s name and return type (if necessary), contains and uses one or more parameters that have an effect on the functionality of the procedure, and implements an algorithm that includes sequencing, selection and iteration| ![image](https://user-images.githubusercontent.com/50186752/165035427-41453591-9374-405e-b724-da710e06432e.png) ![image](https://user-images.githubusercontent.com/50186752/165035471-83a093ce-68c0-4e9c-b28f-c257f8ff6cc7.png) ![image](https://user-images.githubusercontent.com/50186752/165035499-3b8a02c3-6779-44db-a825-0c34d3b5df9b.png) ![image](https://user-images.githubusercontent.com/50186752/165035527-8c70a1bd-7f64-45a2-a564-2c9ee23c1eb3.png)|
| ii| The second program code segment must show where your student-developed procedure is being called in your program| ![image](https://user-images.githubusercontent.com/50186752/165035592-86674f75-7629-4715-851e-883cbcd92570.png)|
|iii |Describes in general what the identified procedure does and how it contributes to the overall functionality of the program | The procedure represented above takes the user input and saves it in the localstorage. It shifts the list if there is more than three items there as we only want to show the last three entered zipcodes. It will then use the zipcode and get the information from our api and iterate through the json block to display in a nice table.|
|iv | Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it.| Firs the user inputs their zipcode. We then use python requests package to get information from an API utilizing the users zipcode. While that is happening we are saving the zipcode in the localstorage data. |

Part D:

| Section | Question | Answer | 
| --- | --- | --- |
| i| Describes two calls to the procedure identified in written response3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute.| zipHistory([92129, 92127, 92126]) vs zipHistory([92137, 92116, 92037])|
| ii| Describes what condition(s) is being tested by each call to the procedure| Checks to see if the given input of the zipcode is 5 digits long. Other condition is that there is only three zipcodes in the resulting list. |
| iii| Identifies the result of each call| There will be an output of 'Past Zipcodes: 92129, 92127, 92126'. and  'Past Zipcodes: 92137, 92116, 92037'|



