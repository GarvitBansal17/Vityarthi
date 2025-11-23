Project title  - Building a todo list.
feature:-
•	 User will be able to add new task with descriptions about it and how to finish it within the time frame.
•	 User will be able to prioritise their task's according to their choices.
•	 Users must be able to able to view their entire Schedule in summarised table form which makes easier for them to understand and set their daily goals accordingly.
•	 User will be able to delete their any wrong entries and also can remove the completed task’s.
•	 User will be able to log a wellness entry (mood, stress rate and cause of any mishappening in the day), summarising will help them to view their past and present mental health conditions.
•	 Users must be able to view their past wellness entries. 
	 Performance
o	Response Time: All pages All pages (e.g., /sheduling, /tracker) must load and display data to the user within 2 seconds.
o	Crud Operation Speed: Task addition, deletion, and wellness log submissions (CRUD operations) must complete and redirect within 1 second.
	 Usability(UX)
o	Accessibility: All form elements(inputs, buttons) must be clear labelled and navigable via keyboard for improved user experience.
o	 Intuitiveness: The applications main navigation links must be present and consistently visible across all primary templates (index.html, scheduling.html etc).
	 Reliability
o	 Data Persistence: All entered tasks must be securely saved to the database and remain persistent across application restarts.
o	 Error Handling: The system must gracefully common errors like the Operational Error without crashing, instead logging the error and displaying a simple, user-friendly message.
	 Security
o	 Data Integrity: The use of SQLAlchemy prevents direct SQL injection attacks by escaping parameters in all queries.
o	 Data Confidentiality: Since this is single-user SQLite application, the primary data security measures is ensuring the database file is not exposed publicly.

overview of this project:-
is an application designed to manage tasks, utilizing fundamental programming concepts like user input handling, data structures (lists, dictionaries), and file I/O for persistence.

technologies/ tools used:-
* flask used for app routing.  
* SQLAlchemy for data base.

Step to install and run the project:-
* download the code file
* insatall the necesarry pakage and libraries like flask(render,templates,request,rediret),SQLAlchemy.
* run the python file.

instruction for testing:- 
on the main website add task discription and there deadline and submite the form check progress traker to see the sumray to se the sheduled tasks

Screenshots:-
<img width="1600" height="858" alt="image" src="https://github.com/user-attachments/assets/4639b3df-42a1-49dd-ad2f-ce78cc8f6764" />
<img width="1600" height="877" alt="image" src="https://github.com/user-attachments/assets/3de3c074-941b-48af-b2fa-96db2fe95373" />
<img width="1600" height="518" alt="image" src="https://github.com/user-attachments/assets/3960243f-4234-4249-9198-d6531b6cbd1e" />
<img width="1600" height="875" alt="image" src="https://github.com/user-attachments/assets/30f99baa-d7a2-40f1-8b28-53e523824ba7" />
<img width="1600" height="544" alt="image" src="https://github.com/user-attachments/assets/72c18a19-4da0-48b8-b873-d5a809a42ba5" />




