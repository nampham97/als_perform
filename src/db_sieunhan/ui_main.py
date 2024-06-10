import streamlit as st
from connect_db_orcl import get_db_connection
from ai_intergration import generate_sql_query, validate_sql_query
import oracledb



st.title("Hạnh 2 Assistant Junior")

# Define the database schema information
table_info = """
LN_CREDIT_FILE_HIST(ID, FILE_ID, CREDIT_APPROVAL_CODE,PROFILE,FILE_NAME,DATE_UPDATED,USER_NAME,TITLE,STATUS,DOCTYPE_ID,TRANGTHAI_SOHOA,TEMOS_ID,OS_ID,CIF,USER_APPROVAL,ERROR_COUNT,ROOT_CODE)
DBM_CREDIT_PROCESS(ID, CREDIT_DISBURSEMENT_CODE,CREDIT_APPROVAL_CODE,IS_PROCESS,LN_CODE,TIME_DISBURSEMENT,INSTANCE_DBM,AA_CODE,INSTANCE_AA,DATE_CREATED,LOAN_SUB_CODE,CURRENT_CODE)
ln_credit_approval(ID	NUMBER	No		1	Khoa chinh
CREDIT_APPROVAL_CODE	VARCHAR2(50 BYTE)	Yes		2	Ma giao dich
LEGAL_CODE	VARCHAR2(50 BYTE)	Yes		3	Mã pháp lý
FINANCIAL_INFO_CODE	VARCHAR2(50 BYTE)	Yes		4	Mã thông tin tài chính
COLLATERAL_CODE	VARCHAR2(50 BYTE)	Yes		5	Mã tài sản bảo đảm
CUSTOMER_CODE	VARCHAR2(50 BYTE)	Yes		6	Mã khách hàng
CUSTOMER_NAME	VARCHAR2(150 BYTE)	Yes		7	Ten khach hang
CIF	VARCHAR2(50 BYTE)	Yes		8	CIF
LOAN_CONDITION	VARCHAR2(50 BYTE)	Yes		9	Dieu kien vay
LOAN_TOTAL	NUMBER	Yes		10	Tong khoan vay
APPROVE_END_LEVEL	VARCHAR2(50 BYTE)	Yes		11	Cap phe duyet cuoi
WORKFLOW_TYPE	VARCHAR2(50 BYTE)	Yes		12	Loai workflow
ROLE_NEXT	VARCHAR2(50 BYTE)	Yes		13	Role tiep theo
USER_NEXT	VARCHAR2(50 BYTE)	Yes		14	User code tiep theo (neu xac dinh)
ROLE_UPDATED	VARCHAR2(50 BYTE)	Yes		15	Role cập nhật
USER_UPDATED	VARCHAR2(50 BYTE)	Yes		16	Người cập nhật
USER_CREATED	VARCHAR2(50 BYTE)	Yes		17	Người tạo
DATE_CREATED	DATE	Yes		18	Ngày tạo
DATE_UPDATED	DATE	Yes		19	Ngaày cập nhật
DEPT_CODE	VARCHAR2(50 BYTE)	Yes		20	Mã phòng ban
BRN_CODE	VARCHAR2(50 BYTE)	Yes		21	Mã chi nhánh
DATE_COMPLETED	DATE	Yes		22	Ngay hoan thanh
STATUS_PROCESS	VARCHAR2(50 BYTE)	Yes		23	Trạng thai dang process
)
"""
package_procedure = """
LN_CREDIT_APPROVAL_V1
DBM_CREDIT_APPROVAL_V1
"""

stored_procedures_info = """
sp_get_employee_details(CREDIT_APPROVAL_CODE)
sp_get_department_budget(CREDIT_APPROVAL_CODE)
"""

st.header("Chuyên gia query SQL")
prompt = st.text_area("Nhập nội dung muốn tìm kiếm:")
if st.button("Xuất SQL và kiểm tra"):
    # Generate SQL query
    query = generate_sql_query(prompt, table_info, package_procedure, stored_procedures_info)
    st.write("Generated Query:")
    st.code(query)

    if validate_sql_query(query):
        st.text("Action query to Databse:")
        # Execute SQL query
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            print("query:", query)
            cursor.execute(query)
            if query.strip().upper().startswith("SELECT"):
                result = cursor.fetchall()
                st.write("Query Result:")
                st.write(result)
            else:
                connection.commit()
                st.success("Query executed successfully.")
        except oracledb.DatabaseError as e:
            st.error(f"Database error: {str(e)}")
        finally:
            cursor.close()
            connection.close()
    else:
        st.error("Invalid SQL query")
