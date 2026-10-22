import asyncio
from logger import get_logger
from DocumentLoader.TextLoader import load_text_file

logger = get_logger(__name__)

async def main():
    file_path = r"Data\payment_gateway_sample.txt"
    logger.info("Starting document ingestion")

    try:
        documents = await load_text_file(file_path)
        for document in documents:
            print(document.page_content[:200])
        logger.info("Successfully loaded %d document(s)",len(documents),)

    except Exception:
        logger.exception("Document ingestion failed")
        raise
if __name__ == "__main__":
    asyncio.run(main())
