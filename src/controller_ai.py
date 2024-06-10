import os
from dotenv import load_dotenv
from groq import Groq
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# SYSTEM_PROMT_AGENT_1 = os.getenv("SYSTEM_PROMT_AGENT_1")


def extract_text_from_pdf(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()

    return text


def get_text_chunks(raw_text, chunk_size=1000):
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=chunk_size, chunk_overlap=200, length_function=len
    )
    chunks = text_splitter.split_text(raw_text)

    return chunks


def split_text_into_chunks(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i : i + chunk_size])
    return chunks


def search_and_answer(client, query, index, chunks, model, top_k=3):
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), top_k)

    relevant_chunks = [chunks[i] for i in I[0]]
    context = " ".join(relevant_chunks)

    response = client.chat.completions.create(
        messages=[
            # {
            #     "role": "system",
            #     "content": SYSTEM_PROMT_AGENT_1,
            # },
            # {
            #     "role": "user",
            #     "content": promt,
            # },
            {
                "role": "user",
                "content": f"Context: {context}\n\nQuestion: {query}\nAnswer:",
            },
        ],
        model="llama3-8b-8192",
    )

    return response.choices[0].message.content


def main():
    client = Groq(
        api_key=GROQ_API_KEY,
    )

    st.title("August Ultimate")
    st.write("A friendly chatbot that can answer your questions!")

    promt = st.text_input("Ask me anything!")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    index = None
    chunks = None

    with st.sidebar:
        st.subheader("Documentation")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process' to extract text",
            type="pdf",
            key="pdf",
            accept_multiple_files=True,
        )

        query = st.text_input("Enter your question:")

        if st.button("Process"):
            if pdf_docs:
                text = extract_text_from_pdf(pdf_docs)
                chunks = split_text_into_chunks(text)
                print("chunks:", chunks)
                embeddings = model.encode(chunks)
                print("embeddings:", embeddings)
                dimension = embeddings.shape[1]
                print("dimension:", dimension)
                index = faiss.IndexFlatL2(dimension)
                print("idex1:", index)
                index.add(np.array(embeddings))
                print("idex2:", index)
                st.success("PDFs processed successfully!")
                print("idx:", index)
                if index is not None and chunks is not None:
                    with st.spinner("Thinking..."):

                        if query:
                            answer = search_and_answer(
                                client, query, index, chunks, model
                            )
                            st.write(f"Answer: {answer}")
                else:
                    st.error("Please process the PDFs first.")
            else:
                st.error("Please upload PDF files before processing.")


def main_rag():
    spacer, col = st.columns([5, 1])
    with col:
        st.image("src/public/images/side.jpg")
  
    

    st.title("Thư ký của Nam - Chuyên DB")
    st.write("Chào mừng sếp. Tận hưởng với trọn bộ DB RLOS - SAALEM")

    # Set up the customization options
    st.sidebar.title("Customization")
    additional_context = st.sidebar.text_input(
        "Enter additional summarization context for the LLM here (i.e. write it in spanish):"
    )
    model = st.sidebar.selectbox("Chọn loại hình", ["PDFs Upload", "DB", "Super"], index=1)
    max_num_reflections = st.sidebar.slider("Max reflections:", 0, 10, value=5)

    st.tẽt("Xin hãy nhập yêu cầu mong muốn")

if __name__ == "__main__":
    main_rag()
