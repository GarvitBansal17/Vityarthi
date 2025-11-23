Project title - Building a todo list. feature:- • User will be able to add new task with descriptions about it and how to finish it within the time frame. • User will be able to prioritise their task's according to their choices. • Users must be able to able to view their entire Schedule in summarised table form which makes easier for them to understand and set their daily goals accordingly. • User will be able to delete their any wrong entries and also can remove the completed task’s. • User will be able to log a wellness entry (mood, stress rate and cause of any mishappening in the day), summarising will help them to view their past and present mental health conditions. • Users must be able to view their past wellness entries.  Performance o Response Time: All pages All pages (e.g., /sheduling, /tracker) must load and display data to the user within 2 seconds. o Crud Operation Speed: Task addition, deletion, and wellness log submissions (CRUD operations) must complete and redirect within 1 second.  Usability(UX) o Accessibility: All form elements(inputs, buttons) must be clear labelled and navigable via keyboard for improved user experience. o Intuitiveness: The applications main navigation links must be present and consistently visible across all primary templates (index.html, scheduling.html etc).  Reliability o Data Persistence: All entered tasks must be securely saved to the database and remain persistent across application restarts. o Error Handling: The system must gracefully common errors like the Operational Error without crashing, instead logging the error and displaying a simple, user-friendly message.  Security o Data Integrity: The use of SQLAlchemy prevents direct SQL injection attacks by escaping parameters in all queries. o Data Confidentiality: Since this is single-user SQLite application, the primary data security measures is ensuring the database file is not exposed publicly.

overview of this project:- is an application designed to manage tasks, utilizing fundamental programming concepts like user input handling, data structures (lists, dictionaries), and file I/O for persistence.

technologies/ tools used:-

flask used for app routing.
SQLAlchemy for data base.
Step to install and run the project:-

download the code file
insatall the necesarry pakage and libraries like flask(render,templates,request,rediret),SQLAlchemy.
run the python file.
instruction for testing:- on the main website add task discription and there deadline and submite the form check progress traker to see the sumray to se the sheduled tasks

Screenshots:-
<img width="1600" height="858" alt="image" src="https://github.com/user-attachments/assets/3427ab03-a46a-4884-a012-c903b08ec4a7" />
<img width="1600" height="877" alt="image" src="https://github.com/user-attachments/assets/7148dc6c-865e-478a-8ae4-ef04703c88f4" />
<img width="1600" height="518" alt="image" src="https://github.com/user-attachments/assets/fd287819-4c65-4713-81f6-8f28be5b0ab6" />
<img width="1600" height="875" alt="image" src="https://github.com/user-attachments/assets/c2b9b40f-244b-4aa3-94f4-6c1094d18508" />
<img width="1600" height="544" alt="image" src="https://github.com/user-attachments/assets/b77d6972-1755-43d2-9bd9-946f1ec9c1d8" />
