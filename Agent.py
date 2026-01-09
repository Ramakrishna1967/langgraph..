Agent
Review
We built a router.

Our chat model will decide to make a tool call or not based upon the user input
We use a conditional edge to route to a node that will call our tool or simply end



import os, getpass

def _set_env(var: str):`
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

_set_env("OPENAI_API_KEY")

_set_env("LANGSMITH_API_KEY")
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_PROJECT"] = "langchain-academy"

