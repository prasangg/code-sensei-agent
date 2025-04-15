from llama_cpp import Llama
from huggingface_hub import hf_hub_download
import os

# Load HUGGINGFACE_TOKEN token from .env file
# This is a placeholder for loading environment variables
# You can use python-dotenv or similar libraries to load .env files
import dotenv
dotenv.load_dotenv()

HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
#  

repo_id = "TheBloke/Mistral-7B-Instruct-v0.2-GGUF"
model_filename = "mistral-7b-instruct-v0.2.Q4_K_M.gguf"
temperature = 0.7
n_ctx: int = 4096
n_batch: int = 512
n_gpu_layers: int = 50

def load_llm():

    model_path: str = hf_hub_download(
        repo_id=repo_id,
        filename=model_filename,
        token=os.getenv("HUGGINGFACE_TOKEN"),
        cache_dir="models")  # Uncomment if token is required,
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at: {model_path}")

    llm = Llama(
        model_path=model_path,
        n_ctx=n_ctx,
        n_batch=n_batch,
        n_gpu_layers=n_gpu_layers,
        temperature=temperature,
        verbose=True
    )
    return llm

# to download the model, uncomment the following line

# if __name__ == "__main__":
#     load_llm()