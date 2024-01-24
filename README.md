## Developing an Interactive Chatbot for the Omdena Website

## Project background
There has been a notable rise in the volume of information circulating on Omdena’s official website. Introducing an interactive chatbot presents an ideal opportunity to communicate information effectively to both new and existing users.

## The problem
The challenge aims to address the problem of effectively managing and disseminating the increasing volume of information on Omdena’s official website while making a positive impact on the local community. As the volume of information circulating on the website continues to grow, it becomes increasingly challenging for users, both new and existing, to access and find the relevant information they need. This creates a barrier to communicating important updates, announcements, and resources effectively to the community. By introducing an interactive chatbot, we can overcome this challenge and enhance the information dissemination process. The chatbot will serve as a virtual assistant capable of providing instant and personalized responses to user queries. It will help users navigate the website, locate specific information, and address their concerns in a timely manner.

This solution will significantly impact the local community by improving the user experience and facilitating efficient access to information. Users will be able to quickly find the information they are seeking, resulting in enhanced engagement, increased participation, and a stronger connection with the Omdena platform. Moreover, the interactive chatbot will provide a more personalized and user-friendly experience, ensuring users receive relevant information tailored to their needs and interests. By effectively communicating information through the chatbot, Omdena can foster a more informed and engaged community, facilitating collaboration and knowledge sharing among members. This, in turn, will promote the growth of the local community, encourage active participation, and contribute to the overall success and impact of Omdena’s initiatives.

## Project goals
 Develop and implement an interactive chatbot on Omdena's official website within a specified timeline. 
 - Train the chatbot to effectively respond to user queries and provide accurate and relevant information.
 - Improve user engagement and satisfaction by enhancing the website's information dissemination process through the chatbot.
 - Increase user accessibility to the website's essential updates, announcements, and resources. - Personalize the chatbot's responses to cater to individual users' specific needs and interests.
 - Measure and analyze the impact of the chatbot on user engagement, website traffic, and overall user satisfaction.
 - Continuously optimize and refine the chatbot based on user feedback and evolving user needs.
 - The chatbot facilitates user knowledge sharing and engagement by fostering a sense of community and collaboration.
 - Enhance the overall user experience on Omdena's website by providing a seamless and efficient information retrieval system through the chatbot.
 - Establish the chatbot as a valuable tool for both new and existing users, contributing to the growth and success of Omdena's initiatives.

## Deployed Solution (Staging) 
#### [Omdena Chat Assistant UI](https://huggingface.co/spaces/pvanand/Omdi-omdena-chat-assistant-ui) [1]
#### [Hosted Model](https://huggingface.co/spaces/pvanand/Omdi-chat-model) [2]
#### [Hosted Action server](https://huggingface.co/spaces/pvanand/omdi-action-server) [3]

- [1] Streamlit frontend + Google Sheets for storing conversation data + RASA backend.
- [2] Pretrained RASA model to classify user intent and provide predefined answers
- [3] Enhances the capability of RASA model with custom logic + fallback answers using cohere free api
  
## Contribution Guidelines
- Have a Look at the [project structure](#project-structure) and [folder overview](#folder-overview) below to understand where to store/upload your contribution
- If you're creating a task, Go to the task folder and create a new folder with the below naming convention and add a README.md with task details and goals to help other contributors understand
    - Task Folder Naming Convention : _task-n-taskname.(n is the task number)_  ex: task-1-data-analysis, task-2-model-deployment etc.
    - Create a README.md with a table containing information table about all contributions for the task.
- If you're contributing for a task, please make sure to store in relavant location and update the README.md information table with your contribution details.
- Make sure your File names(jupyter notebooks, python files, data sheet file names etc) has proper naming to help others in easily identifing them.
- Please restrict yourself from creating unnessesary folders other than in 'tasks' folder (as above mentioned naming convention) to avoid confusion. 

## Project Structure

    ├── LICENSE
    ├── README.md          <- The top-level README for developers/collaborators using this project.
    ├── original           <- Original Source Code of the challenge hosted by omdena. Can be used as a reference code for the current project goal.
    │ 
    │
    ├── reports            <- Folder containing the final reports/results of this project
    │   └── README.md      <- Details about final reports and analysis
    │ 
    │   
    ├── src                <- Source code folder for this project
        │
        ├── data           <- Datasets used and collected for this project
        │   
        ├── docs           <- Folder for Task documentations, Meeting Presentations and task Workflow Documents and Diagrams.
        │
        ├── references     <- Data dictionaries, manuals, and all other explanatory references used 
        │
        ├── tasks          <- Master folder for all individual task folders
        │
        ├── visualizations <- Code and Visualization dashboards generated for the project
        │
        └── results        <- Folder to store Final analysis and modelling results and code.
--------

## Folder Overview

- Original          - Folder Containing old/completed Omdena challenge code.
- Reports           - Folder to store all Final Reports of this project
- Data              - Folder to Store all the data collected and used for this project 
- Docs              - Folder for Task documentations, Meeting Presentations and task Workflow Documents and Diagrams.
- References        - Folder to store any referneced code/research papers and other useful documents used for this project
- Tasks             - Master folder for all tasks
  - All Task Folder names should follow specific naming convention
  - All Task folder names should be in chronologial order (from 1 to n)
  - All Task folders should have a README.md file with task Details and task goals along with an info table containing all code/notebook files with their links and information
  - Update the [task-table](./src/tasks/README.md#task-table) whenever a task is created and explain the purpose and goals of the task to others.
- Visualization     - Folder to store dashboards, analysis and visualization reports
- Results           - Folder to store final analysis modelling results for the project.


