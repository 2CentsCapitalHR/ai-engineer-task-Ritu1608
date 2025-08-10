
import os
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

def build_and_save_index(api_key):
   
    if not api_key:
        raise ValueError("Google API Key is not set.")
    
    os.environ["GOOGLE_API_KEY"] = api_key
    knowledge_base_path = "knowledge_base"
    index_path = "faiss_index"

    if not os.path.isdir(knowledge_base_path):
        print(f"Error: Directory '{knowledge_base_path}' not found.")
        return False
        
    all_chunks = []
    print("Loading documents from the knowledge base...")
    for file_name in os.listdir(knowledge_base_path):
        file_path = os.path.join(knowledge_base_path, file_name)
        if os.path.isfile(file_path):
            try:
                loader = UnstructuredFileLoader(file_path)
                documents = loader.load()
                
                text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
                chunks = text_splitter.split_documents(documents)
                all_chunks.extend(chunks)
                print(f"-> Processed {file_name}")
            except Exception as e:
                print(f"Could not process file {file_name}: {e}")

    if not all_chunks:
        print("No documents were loaded. The knowledge base is empty.")
        return False

    print("\nCreating embeddings and building the FAISS index... (This may take a moment)")
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_documents(all_chunks, embedding=embeddings)
    vector_store.save_local(index_path)
    
    print(f"\nVector database created and saved successfully to '{index_path}'.")
    return True

if __name__ == "__main__":
    print("This script will build the knowledge base for the Corporate Agent.")
    user_api_key = input("Please enter your Google API Key to proceed: ")
    if user_api_key:
        build_and_save_index(user_api_key)
    else:
        print("API Key is required. Exiting.")