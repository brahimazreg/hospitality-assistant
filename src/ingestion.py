from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader,TextLoader,Docx2txtLoader
from config import PATH_DATA_FILE

def load_documents(path:str=None):

    """ Load all documts exists in data directory"""
    if path is None:
        path = PATH_DATA_FILE

    documents=[]

    pdf_loader=DirectoryLoader(
        path=path ,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader,
        recursive=True,
        show_progress=True
    )

    documents.extend(pdf_loader.load())
    
    txt_loader = DirectoryLoader(
        path=path,
        glob="**/*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
        recursive=True,
        show_progress=True
    )
    
    documents.extend(txt_loader.load())

    docs_loader=DirectoryLoader(
                path=path ,
                glob="**/*.docx",
                loader_cls=Docx2txtLoader,
                recursive=True,
                show_progress=True
            )
        
    documents.extend(docs_loader.load())

    return documents