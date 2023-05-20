from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, download_loader
import os

os.environ['OPENAI_API_KEY'] = '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'

YoutubeTranscriptReader = download_loader("YoutubeTranscriptReader")
loader = YoutubeTranscriptReader()

ytlinks = [input("Please enter the YouTube video URL: ")]

while True:
    documents = loader.load_data(ytlinks=ytlinks)

    index = GPTVectorStoreIndex.from_documents(documents)

    query_engine = index.as_query_engine()

    question = input("Please enter your question (or 'q' to quit): ")

    if question.lower() == 'q':
        break

    response = query_engine.query(question)
    print(response)
