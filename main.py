from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, download_loader
import os
os.environ['OPENAI_API_KEY'] = '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'

print("Loading...")
print("Please press 1. Youtube Transcript Reader")
print("Please press 2. Website Transcript Reader")
user_choice = input("Please enter your selction: ")

if user_choice == "1":
    print("Youtube Transcript Reader")
elif user_choice == "2":
    print("Website Transcript Reader")
else:
    print("Invalid selection, please try again.")



def youtube_loader():
    from llama_index import YoutubeTranscriptReader
    loader = YoutubeTranscriptReader()
    while True:
        try:
            documents = loader.load_data(
                ytlinks=[input("Please enter a youtube link: ")])
            break
        except:
            print("Invalid link, please try again.")


def website_loader():
    #
    #

YoutubeTranscriptReader = download_loader("YoutubeTranscriptReader")

loader = YoutubeTranscriptReader()

while True:
    try:
        documents = loader.load_data(
            ytlinks=[input("Please enter a youtube link: ")])
        break
    except:
        print("Invalid link, please try again.")
    if documents: = "quit"
        break

documents = loader.load_data(
    ytlinks=['https://youtu.be/zFhYJRqz_xk'])

# https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-1C665B4D-7BF7-4FDF-98B0-AA7EE12B5AC2

# documents = SimpleDirectoryReader('data').load_data()

index = GPTVectorStoreIndex.from_documents(documents)
print(index)

query_engine = index.as_query_engine()

question = input("Please enter your question: ")
response = query_engine.query(question)
print(response)
