from urllib.parse import urlparse
from dotenv import load_dotenv
import os
import chromadb
import streamlit as st
def get_credentials():
    load_dotenv()
    globals()["api_key"] = os.getenv("api_key", None)
    globals()["watsonx_project_id"] = os.getenv("project_id", None)

def load_css(file_name):
    with open(file_name) as file:
        st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html=True)

def create_collection_name(url):
    parsed_url = urlparse(url)
    domain_parts = parsed_url.netloc.split('.')
    if len(domain_parts) >= 2:
        return domain_parts[-2]  # Extracting the second-level domain
    else:
        return "base"
    
def chromadb_client():
    import chromadb
    # Set up cache directory (consider user-defined location)
    current_dir = os.getcwd()
    # Replace 'my_custom_cache_path' with your desired location
    custom_cache_path = os.path.join(current_dir, ".cache")
    # Create settings object with custom cache path
    settings = chromadb.Settings(persist_directory=custom_cache_path)
     # Initialize client with custom settings
    client = chromadb.Client(settings)
    return client

def clear_collection(collection_name,client):
    try:
        collection = client.get_collection(collection_name)
        if collection:
            collection.delete()
            print(f"Collection '{collection_name}' cleared successfully!")
    except ValueError:
        pass  # collection does not exist, do nothing



