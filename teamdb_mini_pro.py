import streamlit as st
import pandas as pd
import os
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

def getConfig():
    load_dotenv()
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    return GROQ_API_KEY

def main(key):
    model = 'llama3-70b-8192'

    llm = ChatGroq(
            temperature=0, 
            groq_api_key = key, 
            model_name=model
        )

    # Streamlit UI
    st.title('Team Database mini')
    multiline_text = """
    Team Database mini được thiết kế để phân tích vấn đề về phát triển triển khai một improve/enhance từ phía khách hàng và bàn giao về team BA.
    Gồm có các AI được chia các role rõ ràng (Lead, BA, Dev, QC). Team sẽ cung cấp một góc nhìn về các vấn đề và đưa ra giải pháp
    """

    st.markdown(multiline_text, unsafe_allow_html=True)

    # Display the Groq logo
    spacer, col = st.columns([5, 1])  
    with col:  
        st.image('src/public/images/side.jpg')


    Problem_Definition_Agent = Agent(
        role='Database_Query_Problem_Definition_Agent',
        goal="""Clearly define the database query or stored procedure problem provided by the user,
            identifying the specific type of operation (e.g., SELECT, INSERT, UPDATE, DELETE) and any additional requirements or constraints.""",
        backstory="""As an expert in understanding database query and stored procedure problems, your role is to extract a clear and concise problem statement from the user's input. This ensures the project starts with a solid foundation for generating appropriate SQL code to address the user's needs.""",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    Data_Assessment_Agent = Agent(
        role='Database_Data_Assessment_Agent',
        goal="""Evaluate the quality and suitability of the data provided by the user for the specified database query or stored procedure.
            Suggest any necessary data transformations, cleaning, or preprocessing steps required to prepare the data for the desired operations.""",
        backstory="""You specialize in assessing and preparing data for database operations. Your task is to guide the user in ensuring their dataset is ready for the SQL query or stored procedure, including recommendations for data cleaning, normalization, and any required transformations.""",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    Database_Issue_Analysis_Agent = Agent(
        role='Database_Issue_Analysis_Agent',
        goal="""Analyze potential issues or challenges that may arise in the database based on the defined problem and assessed data.
            Provide detailed insights and recommendations to help the team address and mitigate these issues effectively.""",
        backstory="""As an experienced database analyst, you are responsible for identifying potential issues or challenges in the database based on customer reports, problem definitions, and data assessments. Your role is to provide in-depth analysis and actionable recommendations to the team, enabling them to take appropriate measures to enhance the database and improve customer experience.""",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    Starter_Code_Generator_Agent = Agent(
        role='Oracle_SQL_Code_Generator_Agent',
        goal="""Generate precise and executable Oracle SQL code tailored to the user's database query or stored procedure project.
            The code should include all necessary SQL statements (SELECT, INSERT, UPDATE, DELETE), data loading operations, and any other required Oracle database-specific operations based on the problem definition, data assessment, and recommendations provided.""",
        backstory="""You are an expert in Oracle SQL code generation, capable of transforming problem definitions, data assessments, and recommendations into accurate and ready-to-use Oracle SQL code. Your goal is to provide users with a complete solution for their database query or stored procedure requirements on Oracle databases, ensuring the generated code addresses their specific needs and follows Oracle's SQL syntax and best practices.""",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    QC_Agent = Agent(
        role='QC_Agent',
        goal="""Review the output from the previous agents (Problem Definition, Data Assessment, Database Issue Analysis, and SQL Code Generation) and provide quality assurance feedback.
            Identify any potential issues, inconsistencies, or areas for improvement in the provided solutions.""",
        backstory="""As a quality control expert, your responsibility is to thoroughly review the work done by the other agents involved in the database query or stored procedure project. Your role is to identify any potential issues, inconsistencies, or areas for improvement in the provided solutions, ensuring that the final output meets the highest standards of quality and accuracy.""",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    Summary_Agent = Agent(
        role='Summary_Agent',
        goal="""Provide a comprehensive summary of the entire database query or stored procedure project, including the problem definition, data assessment, identified issues and recommendations, generated SQL code, and quality control feedback.
            Outline a clear action plan for the team to proceed with implementing the proposed solution.""",
        backstory="""You are a seasoned project manager, responsible for consolidating the findings and outputs from all the agents involved in the database query or stored procedure project. Your role is to synthesize the information into a concise yet comprehensive summary, outlining the key aspects of the project, including the problem definition, data assessment, identified issues and recommendations, generated SQL code, and quality control feedback. Additionally, you will provide a clear action plan for the team to proceed with implementing the proposed solution effectively.""",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    user_question = st.text_input("Mô tả yêu cầu của database")
    data_upload = False
    uploaded_file = st.file_uploader("Upload file .csv database (optional)")
    if uploaded_file is not None:
        try:
            # Attempt to read the uploaded file as a DataFrame
            df = pd.read_csv(uploaded_file, encoding='unicode_escape').head(5)
            
            # If successful, set 'data_upload' to True
            data_upload = True
            
            # Display the DataFrame in the app
            st.write("Data successfully uploaded and read as DataFrame:")
            st.dataframe(df)
        except Exception as e:
            st.error(f"Error reading the file: {e}")

    if st.button("Họp nào") and user_question:
        print('user_question:', user_question)
        task_define_problem = Task(
            description="""Clarify and define the database query or stored procedure problem,
                including identifying the type of query (e.g., SELECT, INSERT, UPDATE, DELETE) and any specific requirements.

                Here is the user's problem:

                {ml_problem}
                """.format(ml_problem=user_question),
            agent=Problem_Definition_Agent,
            expected_output="A clear and concise definition of the database query or stored procedure problem."
        )
        if data_upload:
            task_assess_data = Task(
                description="""Evaluate the user's data for quality and suitability for the database query or stored procedure,
                suggesting any necessary data transformations or preprocessing steps.
                
                Here is a sample of the user's data:

                {df}

                The file name is called {uploaded_file}
                
                """.format(df=df.head(), uploaded_file=uploaded_file),
                agent=Data_Assessment_Agent,
                expected_output="An assessment of the data's quality and suitability for the database query or stored procedure, with suggestions for any necessary data transformations or preprocessing."
            )
        else:
            task_assess_data = Task(
                description="""The user has not uploaded any specific data for this problem,
                but please consider a hypothetical dataset that might be useful
                for their database query or stored procedure problem.
                """,
                agent=Data_Assessment_Agent,
                expected_output="A hypothetical dataset that might be useful for the database query or stored procedure problem, along with any necessary data transformations or preprocessing steps."
            )

        task_recommend_model = Task(
            description="""Analyze potential database issues and provide insights to help the team address them
            based on the problem description and data assessment.""",
            agent=Database_Issue_Analysis_Agent,
            expected_output="An analysis of potential database issues and recommendations to address them, based on the defined problem and assessed data."
        )

        task_generate_code = Task(
            description="""Generate precise Oracle SQL code for the database query or stored procedure project,
                including SELECT, INSERT, UPDATE, and DELETE statements, data loading, and any necessary Oracle database-specific operations,
                based on the problem definition, data assessment, and any additional requirements or recommendations.""",
            agent=Starter_Code_Generator_Agent,
            expected_output="Executable Oracle SQL code tailored to the user's database query or stored procedure project, including a brief summary of the problem and code recommendations, following Oracle's SQL syntax and best practices."
        )

        task_qc_review = Task(
            description="""Review the output from the previous agents (Problem Definition, Data Assessment, Database Issue Analysis, and SQL Code Generation)
                and provide quality assurance feedback. Identify any potential issues, inconsistencies, or areas for improvement in the provided solutions.""",
            agent=QC_Agent,
            expected_output="A thorough review of the solutions provided by the other agents, with feedback on potential issues, inconsistencies, or areas for improvement."
        )

        task_summarize = Task(
            description="""Provide a comprehensive summary of the entire database query or stored procedure project, including:
                - Problem definition (clearly labeled)
                - Data assessment (clearly labeled)
                - Identified issues and recommendations (clearly labeled)
                - Generated Oracle SQL code (clearly labeled, formatted for Oracle databases)
                - Quality control feedback (clearly labeled)

                Outline a clear action plan for the team to proceed with implementing the proposed solution.""",
            agent=Summary_Agent,
            expected_output="""A concise yet comprehensive summary of the project, with each section (problem definition, data assessment, identified issues and recommendations, generated Oracle SQL code, quality control feedback) clearly labeled.

        The generated Oracle SQL code should be formatted for Oracle databases.

        Additionally, a clear action plan for the team should be provided."""
        )

        crew = Crew(
            agents=[Problem_Definition_Agent, Data_Assessment_Agent, Database_Issue_Analysis_Agent, Starter_Code_Generator_Agent, QC_Agent, Summary_Agent],
            tasks=[task_define_problem, task_assess_data, task_recommend_model, task_generate_code, task_qc_review, task_summarize],
            verbose=2
        )

        result = crew.kickoff()

        st.write(result)


if __name__ == "__main__":
    GROQ_API_KEY = getConfig()

    main(GROQ_API_KEY)
