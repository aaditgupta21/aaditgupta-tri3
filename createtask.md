{% include nav.html %}
# Create Task Plan
Local Showtimes

Part A

| Section | Question | Answer | 
| --- | --- | --- |
| i| Describe the overall purpose of the program | The purpose of the program is to show when the latest movies are showing in a person's local theatre.  |
| ii| Describes what functionality of the program is demonstrated in the video| The video has the user input their zipcode and the system outputs the latest showtimes. There is also a list of the last three zipcodes saved. |
| iii| Describes the input and output of the program demonstrated in the video| The input is the zipcode and the output is the table of information that is specifically for the user. |

Part B

| Section | Question | Answer | 
| --- | --- | --- |
| i | The first program code segment must show how data have been stored in the list. | ![image](https://user-images.githubusercontent.com/89180255/155897960-f6e66d0d-91f4-40f0-9bbd-d01f303eb8f7.png) This shows how the stored zip codes will create a list, as a comma splits each value.|
| ii| The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose.| ![image](https://user-images.githubusercontent.com/89180255/155898007-b8ef53b0-09a2-42a4-be8f-dc9c66e83694.png) <br >The list will remove the first item if there is more than 3 items in the list already.</br>|
| iii | Identifies the name of the list being used in this response| ``` zipHistory ``` is the name of the list.|
| iv | Describes what the data contained in the list represent in your program| The data in the list is the last three zipcodes that the user inputs. |
| v | Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list| The list manages the complexity of our program code as it utilizes localstorage of a browser to save data efficiently. It is a neat way to show history of user input. |

Part C

| Section | Question | Answer | 
| --- | --- | --- |
| i| The first program code segment must be a student-developed procedure that: Defines the procedure’s name and return type (if necessary), contains and uses one or more parameters that have an effect on the functionality of the procedure, and implements an algorithm that includes sequencing, selection and iteration| ![image](https://user-images.githubusercontent.com/89180255/155898526-99fe98d1-33f7-4836-9ff0-64d8d2a4829d.png) ![image](https://user-images.githubusercontent.com/89180255/155898565-757f5cd5-fbb0-4b54-bb30-8f1b14d6b9e1.png)|
| ii| The second program code segment must show where your student-developed procedure is being called in your program| ![image](https://user-images.githubusercontent.com/89180255/155898608-cfd9f8ea-af07-43db-b7e9-c1b3abf02998.png)|
|iii |Describes in general what the identified procedure does and how it contributes to the overall functionality of the program | The procedure represented above takes the user input and saves it in the localstorage. It shifts the list if there is more than three items there as we only want to show the last three entered zipcodes. It will then use the zipcode and get the information from our api and iterate through the json block to display in a nice table.|
|iv | Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it.| Firs the user inputs their zipcode. We then use python requests package to get information from an API utilizing the users zipcode. While that is happening we are saving the zipcode in the localstorage data. |

Part D:

| Section | Question | Answer | 
| --- | --- | --- |
| i| Describes two calls to the procedure identified in written response3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute.| ![image](https://user-images.githubusercontent.com/89180255/155899352-1d262a7a-7924-4e64-80cc-96abf97acfe6.png) ![image](https://user-images.githubusercontent.com/89180255/155899301-0d97852a-978a-4f97-901f-af00a4c60be6.png)|
| ii| Describes what condition(s) is being tested by each call to the procedure| It checks to see if the user input is a valid zipcode. The ziphistory list must have 3 items so it checks if there is more than 3 and if there is then it will remove the first item of the list. |
| iii| Identifies the result of each call| There will be an output of 'Past Zipcodes'. |



