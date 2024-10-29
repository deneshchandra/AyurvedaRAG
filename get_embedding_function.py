from langchain_aws import BedrockEmbeddings

def get_embedding_function():
    embeddings = BedrockEmbeddings(
        credentials_profile_name="default", region_name="us-west-2"
    )
    # embeddings = OllamaEmbeddings(model="nomic-embed-text") #for running Ollama locally on computer
    return embeddings



   