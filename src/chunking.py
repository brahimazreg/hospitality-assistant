from langchain_text_splitters import  RecursiveCharacterTextSplitter
from config import CHUNK_SIZE ,CHUNK_OVERLAP


def split_into_chunks(documents):
    """ split documents in chunks"""
    splitters=RecursiveCharacterTextSplitter(
        chunk_size= CHUNK_SIZE ,
        chunk_overlap =CHUNK_OVERLAP,
        separators=["\n\n", "\n", " ", ""]
    )


    chunks = splitters.split_documents(documents)
    return chunks