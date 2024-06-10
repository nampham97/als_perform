from root_ai import create_client
client = create_client()
def generate_sql_query(prompt, table_info, package_procedure, stored_procedures_info):
    messages = [
        {
            "role": "system",
            "content": "You are an SQL expert from Google. Only generate the SQL query based on the following information. Ensure the query only Text and do not have ; end text. Do not provide any explanation."
        },
        {
            "role": "system",
            "content": f"Database tables and their columns: {table_info}"
        },
        {
            "role": "system",
            "content": f"Package procedures: {package_procedure} and Stored procedures: {stored_procedures_info}"
        },
        {
            "role": "user",
            "content": f"Requirement: {prompt} \nWrite the ONLY SQL query below:"
        }
    ]
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages,
        max_tokens=150
    )
    print('responseAI:', response)
    
    return response.choices[0].message.content.strip()

def validate_sql_query(query):
    # Simple validation example
    return any(keyword in query.upper() for keyword in ["SELECT", "INSERT", "UPDATE", "DELETE"])

if "__name__" == "__main__":
    pass