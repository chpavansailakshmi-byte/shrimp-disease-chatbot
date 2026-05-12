import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import streamlit as st
from PIL import Image
# Load PDF
loader = PyPDFLoader("shrimp_diseases.pdf")
documents = loader.load()

# Split text
text_splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

texts = text_splitter.split_documents(documents)

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Vector DB
db = FAISS.from_documents(texts, embeddings)

# Streamlit UI
st.title("🦐 Shrimp Disease Chatbot")

query = st.text_input("Ask a question:")

if query:

    
    query = query.lower()

    if "wfs" in query:
        query = "White Feces Syndrome"

    elif "wssv" in query:
        query = "White Spot Syndrome Virus"

    elif "ehp" in query:
        query = "Enterocytozoon hepatopenaei"

    elif "rms" in query:
        query = "Running Mortality Syndrome"

    elif "imnv" in query:
        query = "Infectious Myonecrosis Virus"

    elif "cmnv" in query:
        query = "Covert Mortality Nodavirus"

    elif "div1" in query:
        query = "Decapod Iridescent Virus 1"

    elif "ihhnv" in query:
        query = "Runt Deformity Syndrome"

    elif "lss" in query:
        query = "Loose Shell Syndrome"

    elif "hpv" in query:
        query = "Hepatopancreatic Parvovirus"

    elif "yhd" in query:
        query = "Yellow Head Disease"

    docs = db.similarity_search(query, k=1)

    st.subheader("Answer:")

    for doc in docs:
        st.write(doc.page_content)
    if "white spot" in query.lower():
        image = Image.open("images/white Spot Syndrome Virus.png")
        st.image(image, caption="White Spot Disease")
    elif "ehp" in query.lower():
        image = Image.open("images/EMS.png")
        st.image(image, caption="EHP Disease")
    elif "running mortality" in query.lower() or "rms" in query.lower():
        image = Image.open("images/RMS.png")
        st.image(image, caption="Running Mortality Syndrome")
    elif "white feces" in query.lower() or "wfs" in query.lower():
        image = Image.open("images/WFS.png")
        st.image(image, caption="White Feces Syndrome")
    elif "black gill" in query.lower():
        image = Image.open("images/BGD.png")
        st.image(image, caption="Black Gill Disease")
    elif "imnv" in query.lower() or "myo" in query.lower():
        image = Image.open("images/IMNV.png")
        st.image(image, caption="IMNV Disease")
    elif "cmnv" in query.lower():
        image = Image.open("images/CMNV.png")
        st.image(image, caption="CMNV Disease")
    elif "d1v1" in query.lower():
        image = Image.open("images/D1V1.png")
        st.image(image, caption="DIV1 Disease")
    elif "vibriosis" in query.lower():
        image = Image.open("images/Vibriosis.png")
        st.image(image, caption="Vibriosis")
    elif "ihhnv" in query.lower() or "runt deformity" in query.lower():
        image = Image.open("images/IHHNV.png")
        st.image(image, caption="IHHNV Disease")
    elif "loose shell" in query.lower() or "lss" in query.lower():
        image = Image.open("images/LSS.png")
        st.image(image, caption="Loose Shell Syndrome")
    elif "hpv" in query.lower():
        image = Image.open("images/HPV.png")
        st.image(image, caption="HPV Disease")
    elif "yellow head" in query.lower() or "yhd" in query.lower():
        image = Image.open("images/YHD.png")
        st.image(image, caption="Yellow Head Disease")
    elif "luminescent vibriosis" in query.lower():
        image = Image.open("images/Luminescent Vibriosis.png")
        st.image(image, caption="Luminescent Vibriosis")
    
    