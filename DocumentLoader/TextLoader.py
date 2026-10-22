
from pathlib import Path

from langchain_community.document_loaders import TextLoader
from logger import get_logger

logger = get_logger(__name__)


async def load_text_file(
    file_path: str,
    encoding: str = "utf-8",
    autodetect_encoding: bool = True,
):
    path = Path(file_path)

    if not path.is_file():
        logger.error("File not found: %s", path)
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix.lower() != ".txt":
        logger.error("Unsupported file type: %s", path.suffix)
        raise ValueError("Only .txt files are supported")

    loader = TextLoader(
        file_path=str(path),
        encoding=encoding,
        autodetect_encoding=autodetect_encoding,
    )

    try:
        documents = await loader.aload()

        for document in documents:
            document.metadata["file_name"] = path.name
            document.metadata["file_type"] = "txt"

        logger.info(
            "Loaded %d document(s) from %s",
            len(documents),
            path.name,
        )

        return documents

    except Exception:
        logger.exception("Failed to load TXT file: %s", path.name)
        raise
