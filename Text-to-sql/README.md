# Project: Text to SQL Query Genrator LLMs Application

**Descreption:**

It's alway intitive abd simpler to think of business quations in plain English. However, a staright forword questions like
"What is the quarterly sales of a specific product across various customer segments?"
May translate to a fairly complex SQL query with joins and multiple subqueries. Which is why building the a "text to SQL generator app" can help.

App that translates natural language queries into SQL using LLMs--> Gemini Pro --> Query -->SQL Database--> Responce

The app should:
1 convert the user input into  SQL queries based on a predefined database schema
2 Excute them against a connected database to return relavant data.

Implementation:

1 SQLlite ---Insert some records--Python program
2 LLMs Application --> Gemini Pro--> SQL Database
