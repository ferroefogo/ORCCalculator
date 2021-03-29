-ORC Calculator-
===Organic Ranking Cycle System Calculator===
+/**
+CONTENTS
+---------
+1. Introduction
+2. Requirements
+3. Configuration/Testing
+4. API Connection
+5. Regards
+----------------
+1. Introduction
+----------------
+ The ORC Calculator is a tool used to calculate the monetary cost of an ORC (Organic Ranking Cycle) system, given component variables, such as power, area and volume.
+ This is an upgrade on the previous system that only allowed 5 of each component type to be entered at a time. 
+ Additionally the super horrendous program design of the previous system was bothering me alot, so I just decided to crunch the code required by 10 fold (OOP approach - duh...)
+----------------
+2. Requirements
+----------------
+ Must be ran on python 3.x
+ The program requires the following 
+ list of external modules to function:
+                  - sqlite3
+                  - pandas
+                  - anvil
+ All that is externally required from the main.py that is ran is all of its contributing files within the folder, such as the .db file, .csv files for the results and an API
+ connection that I will discuss further later.
+-------------------------
+3. Configuration/Testing
+-------------------------
+ Those who might want to test the database, or look to see how it was made can open the COMPONENT_DB.py
+ file in IDLE mode to show the database creation code.
+
+ To create a new fresh database, the standard ComponentData.db that comes with the system can be deleted, and the COMPONENT_DB.py
+ file must be ran.
+
+ The config_id.txt file stores the currently selected configuration opened in the window of the program.
+
+ The CurrentConfig.csv and TargetConfig.csv files store the database data in a text format to be formatted onto a .PDF file later.
+
+ The PDFReports folder is the default path to save the PDF folders produced by the system.
+
+-------------------------
+4. API Connection
+ The creation, formatting and downloading of the PDF files that are created from the current and target configurations selected is handled by the Anvil web-app
+ developing system, where the data from the database concerning the selected configurations, is transferred to an online database at the Anvil servers and placed through a
+ formatting process to place the data into a PDF format in a neat, useful fashion using different tables and bar graph statistics, with more to come.
+ 
+ This part of the system is out of reach of the public, as the anvil web-app requires a token key that is hidden, so that data cannot be stolen from there.
+ 
+-----------
+5. Regards
+-----------
+ Made by Marco Fernandes
+ Developed for The Thermodynamics department of the University of Brighton
+ On Python 3.7.4
+-------------------------
