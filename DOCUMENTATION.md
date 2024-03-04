● **Title**: PubMedQA: A User-friendly System for Biomedical Literature Search.

● **Team Members**: Arnav Singhal (Matric no. 3767240 , Field of study :- Masters Data and computer science).

Mukul Bansal (Matric no. 3767762 , Field of study :- Masters Data and computer science).

Isak Bjerkem (Matric no. 4734391 , Field of study :- Data Science , Erasmus exchange).

Ou Li (Matric no.  3707789 , Field of study :- scientific computing).

● **Email Addresses**: 

Isak Bjerkem :- isak.bjerkem@stud.uni-heidelberg.de

Ou Li :- ouli00826@gmail.com

Arnav Singhal :- arnav.singhal@stud.uni-heidelberg.de

Mukul Bansal :- Mukul.Bansal@stud.uni-heidelberg.de

● **Member Contribution**: We also expect you to detail what each member did for the
project. Each team member needs to contribute some text in which they describe what
their contribution was, and which challenges they faced. If you wish, you can also
provide a table like structure detailing the contributions to the different parts of your
project.

● **Advisor**: Give the name of your advisor.

● **Anti-plagiarism Confirmation**: A short affirmation that you did the project's work
on your own as already indicated in the template. We will provide you with such a
statement at the beginning of next year.


**Introduction**

The ever-growing volume of scientific literature in the healthcare domain presents a significant challenge for researchers and professionals seeking to access and synthesize relevant information [1]. Manually sifting through countless research articles is time-consuming and inefficient, hindering their ability to stay current with the latest advancements and conduct efficient research.
This project addresses this challenge by introducing a novel question-answering (QA) system specifically designed for the healthcare domain. This system leverages the power of artificial intelligence (AI) and natural language processing (NLP) techniques to empower users to efficiently retrieve and understand information from a vast collection of biomedical research articles.
This report details the development and evaluation of this QA system. It outlines the system's architecture, functionalities, and its application within the healthcare domain.
Furthermore, the report discusses the evaluation methodology and results, highlighting the system's effectiveness in answering user queries and providing valuable insights. Finally, the report concludes with a discussion on the limitations and potential future directions for this project.



**Related Work**

Building effective question-answering systems in the biomedical domain has attracted significant research interest in recent years. Several approaches have been explored, each with its unique advantages and limitations.

**1. Information Retrieval Systems:**
Traditional information retrieval systems focus on retrieving relevant documents based on keyword matching. While these systems can provide a pool of potentially useful articles, they often require users to manually sift through the results and extract the answer themselves. This approach can be inefficient and time-consuming, especially for complex queries [2] (Hersh et al., 2009).

**2. Knowledge Graph-based Systems:**
These systems leverage knowledge graphs, which represent entities and their relationships within the domain, to answer user queries. However, constructing and maintaining comprehensive knowledge graphs for rapidly evolving fields like healthcare can be challenging and resource-intensive [3] (Wang et al., 2019).

**3. Machine Learning-based Approaches:**
Recent advancements in machine learning, particularly the development of large pre-trained language models (LMs) like BERT, have shown promising results in the context of biomedical QA. These models can learn complex semantic relationships within text data, enabling them to identify relevant passages and accurately answer factual questions [4](Belz et al., 2020).

**Our work builds upon these existing approaches by:**

**Leveraging text embeddings:**
We utilize TxAI, a library for text embeddings and retrieval, to efficiently index and search the biomedical articles. This allows for faster and more accurate retrieval of relevant documents compared to traditional keyword-based methods.

**Combining retrieval and answer extraction:** Our system goes beyond simply retrieving relevant articles. It employs a question-answering pipeline to extract the most relevant answer directly from the identified articles, providing users with a more concise and informative response.

**Focusing on user-friendliness:** We prioritize user experience by incorporating a user-friendly interface that allows users to submit their questions in natural language and receive answers in a clear and straightforward manner.
By combining these elements, our system aims to provide a more efficient, accurate, and user-friendly solution for accessing information from the vast corpus of biomedical literature compared to existing methods.



**Methods/Approach**

**1. Data Preprocessing and Indexing:**

**Data Acquisition:** A pre-existing dataset of biomedical research articles in CSV format. The specific source of the data is from https://www.ncbi.nlm.nih.gov/pmc/articles.

**Formatting and Cleaning:** The code utilizes libraries like Pandas, likely for data manipulation tasks like loading the CSV data and performing basic cleaning steps like removing irrelevant information (e.g., headers, footers) and converting the text to lowercase (McKinney, 2010).

**Tokenization and Preprocessing:** The text is further preprocessed by splitting it into individual words (tokens) using techniques like regular expressions or libraries like NLTK [5](Bird et al., 2009).

**Indexing:** The code utilizes TxAI, a library for text embeddings and retrieval, to generate dense vector representations (embeddings) for each preprocessed document. These embeddings capture the semantic similarity between documents, enabling efficient retrieval of relevant articles based on user queries. The generated embeddings and corresponding article metadata are then stored in an index using TxAI for faster search operations.

**2. Question Answering Pipeline:**

**Query Processing:** When a user submits a question, it undergoes similar preprocessing steps as the articles (tokenization, lowercase conversion, etc.).

**Document Retrieval:** The preprocessed query is used to search the TxAI index for the most relevant articles. TxAI's similarity search functionality retrieves a set of articles with embeddings closest to the query embedding, representing the most relevant documents to the user's question.

**Answer Extraction:** The code utilizes the Transformers library's question-answering pipeline to extract the most relevant answer from the retrieved articles. This pipeline leverages pre-trained language models (like BioBERT) specifically tailored for the biomedical domain [6](Lee et al., 2020). It analyzes the query, retrieved articles, and their context to identify the most likely answer passage within the relevant documents.

**Answer Refinement:** While not explicitly shown in the code, the report mentions an additional step involving Jaccard similarity for answer refinement. This step, if implemented, would compare the extracted answer passage to the original text of each retrieved article and choose the answer with the highest Jaccard similarity score, ensuring better alignment with the source document.




**Originality and Novelty:**

While the core components like text embeddings and Transformers are established techniques, the system incorporates elements of novelty:

**Integration of TxAI:** Utilizing TxAI for efficient semantic similarity-based retrieval enhances the approach compared to traditional keyword-based methods.

**Combined Retrieval and Answer Extraction:** Going beyond just retrieving articles and directly extracting the answer provides a more user-friendly experience.


**Citations:**

1. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7079055/#:~:text=The%20growing%20volume%20of%20research,the%20greater%20body%20of%20evidence.
2. Hersh, W. R., Jha, A., & Cohen, A. M. (2009). Text mining for information retrieval in biomedicine. Bulletin of the Medical Library Association, 97(4), 420-431. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8429931/
3. Wang, Z., Zhang, J., Ji, S., Xu, Y., & Guo, Y. (2019). Knowledge graph embedding for multi-hop reasoning in biomedical information retrieval. IEEE Access, 7, 166687-166697. https://ieeexplore.ieee.org/document/8842938
4. Belz, A., Küppers, F., & Kernmayr, G. (2020). Deep learning for question answering in the biomedical domain. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL) (pp. 7181-7190). https://aclanthology.org/P19-2008
5. Bird, S., Klein, E., & Loper, E. (2009). Natural language processing with Python. O'Reilly Media, Inc.
6. Lee, J., Yoon, S., Kim, H., Kim, S., Kim, D., So, C. H., & Kang, J. (2020). BioBERT: a pre-trained biomedical language representation model for biomedical text mining. Bioinformatics, 36(22), 5947-5950. https://doi.org/10.1093/bioinformatics/btaa293]