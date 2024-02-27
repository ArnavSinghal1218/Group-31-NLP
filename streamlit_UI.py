# streamlit UI
import streamlit as st
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

indexName = "pmids"

try:
    es = Elasticsearch(
        "https://localhost:9200",
        basic_auth=("elastic", "your_password"),  # Update with your actual password
        ca_certs="path/to/your/http_ca.crt"  # Update with the actual path to your certificate
    )
    if es.ping():
        st.success("Successfully connected to Elasticsearch!")
    else:
        st.error("Oops!! Cannot connect to Elasticsearch.")
except Exception as e:
    st.error(f"Connection Error: {e}")

def search(input_query):
    model = SentenceTransformer('all-mpnet-base-v2')
    query_vector = model.encode(input_query)

    query = {
        "field": "AbstractVector",  # Assuming your documents have an 'AbstractVector' field
        "query_vector": query_vector,
        "k": 10,
        "num_candidates": 500
    }
    res = es.knn_search(index=indexName, knn=query, source=["Title", "Abstract"])
    results = res["hits"]["hits"]

    return results

def main():
    st.title("PubMed Article Search")

    # Input: User enters search query
    search_query = st.text_input("Enter your search query")

    # Button: User triggers the search
    if st.button("Search"):
        if search_query:
            # Perform the search and get results
            results = search(search_query)

            # Display search results
            st.subheader("Search Results")
            for result in results:
                with st.container():
                    if '_source' in result:
                        try:
                            st.header(f"{result['_source']['Title']}")
                        except Exception as e:
                            st.error(e)
                        
                        try:
                            st.write(f"Abstract: {result['_source']['Abstract']}")
                        except Exception as e:
                            st.error(e)
                        st.divider()

if __name__ == "__main__":
    main()
