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
        role ='Database_Query_Problem_Definition_Agent',
        goal ="""Clarify the database query or stored procedure problem the user wants to solve,
            identifying the type of query (e.g., SELECT, INSERT, UPDATE, DELETE) and any specific requirements.""",
        backstory="""You are an expert in understanding and defining database query and stored procedure problems.
            Your goal is to extract a clear, concise problem statement from the user's input,
            ensuring the project starts with a solid foundation for generating the appropriate SQL code.""",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    Data_Assessment_Agent = Agent(
        role='Database_Data_Assessment_Agent',
        goal="""Evaluate the data provided by the user, assessing its quality,
            suitability for the database query or stored procedure, and suggesting any necessary data transformations.""",
        backstory="""You specialize in database data evaluation and preparation.
            Your task is to guide the user in preparing their dataset for the SQL query or stored procedure,
            including suggestions for data cleaning, normalization, and any required data transformations.""",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    Database_Issue_Analysis_Agent = Agent(
        role='Database_Issue_Analysis_Agent',
        goal="""Analyze potential database issues and provide insights to help the team address them
        based on the problem description and data assessment.""",
        backstory="""As an experienced database analyst, you are responsible for identifying potential
        issues in the database based on customer reports and data assessments. Your role is to provide
        detailed analysis and recommendations to the team, enabling them to take appropriate actions
        to enhance the database and improve customer experience.""",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )


    Starter_Code_Generator_Agent = Agent(
         role='SQL_Code_Generator_Agent',
        goal="""Generate precise SQL code for the database query or stored procedure project,
            including SELECT, INSERT, UPDATE, and DELETE statements, data loading, and any necessary database operations,
            based on the problem definition, data assessment, and any additional requirements.""",
        backstory="""You are a SQL code generation expert, capable of transforming problem definitions and data assessments
            into accurate and executable SQL code. Your goal is to provide users with a complete and ready-to-use SQL solution
            for their database query or stored procedure requirements.""",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    # Summarization_Agent = Agent(
    #     role='Starter_Code_Generator_Agent',
    #     goal="""Summarize findings from each of the previous steps of the ML discovery process.
    #         Include all findings from the problem definitions, data assessment and model recommendation 
    #         and all code provided from the starter code generator.
    #         """,
    #     backstory="""You are a seasoned data scientist, able to break down machine learning problems for
    #         less experienced practitioners, provide valuable insight into the problem and why certain ML models
    #         are appropriate, and write good, simple code to help get started on solving the problem.
    #         """,
    #     verbose=True,
    #     allow_delegation=False,
    #     llm=llm,
    # )

    user_question = st.text_input("Mô tả yêu cầu của database")
    data_upload = False
    uploaded_file = st.file_uploader("Upload file .csv database (optional)")
    if uploaded_file is not None:
        try:
            # Attempt to read the uploaded file as a DataFrame
            df = pd.read_csv(uploaded_file).head(5)
            
            # If successful, set 'data_upload' to True
            data_upload = True
            
            # Display the DataFrame in the app
            st.write("Data successfully uploaded and read as DataFrame:")
            st.dataframe(df)
        except Exception as e:
            st.error(f"Error reading the file: {e}")

    if user_question:
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
            description="""Generate precise SQL code for the database query or stored procedure project,
                including SELECT, INSERT, UPDATE, and DELETE statements, data loading, and any necessary database operations,
                based on the problem definition, data assessment, and any additional requirements or recommendations.""",
            agent=Starter_Code_Generator_Agent,
            expected_output="Executable SQL code tailored to the user's database query or stored procedure project, including a brief summary of the problem and code recommendations."
        )

        # task_summarize = Task(
        #     description="""
        #     Summarize the results of the problem definition, data assessment, model recommendation and starter code generator.
        #     Keep the summarization brief and don't forget to share the entirety of the starter code!
        #     """,
        #     agent=Summarization_Agent
        # )


        crew = Crew(
            agents=[Problem_Definition_Agent, Data_Assessment_Agent, Database_Issue_Analysis_Agent,  Starter_Code_Generator_Agent], #, Summarization_Agent],
            tasks=[task_define_problem, task_assess_data, task_recommend_model,  task_generate_code], #, task_summarize],
            verbose=2
        )

        result = crew.kickoff()

        st.write(result)


if __name__ == "__main__":
    GROQ_API_KEY = getConfig()

    main(GROQ_API_KEY)
