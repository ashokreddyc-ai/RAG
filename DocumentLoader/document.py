from langchain_core.documents import Document

document = Document(
    page_content='hello,world',
    metadata={"source":"https://example.com","purpose":"Explain LangChain Document loder"}
)

print(document.page_content)
print(document.metadata)