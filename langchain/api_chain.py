from langchain.chains.api.prompt import API_RESPONSE_PROMPT

from langchain.chains import APIChain
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0)

GREETING_API_DOCS = """API documentation:
Endpoint: http://127.0.0.1:8000/
GET /

This API is for greeting message by time and country.

Query parameters table:
time | string | time for greeting, available: morning, noon, night | required
country | string | Limit search results to a specific country, available: ja,en,fr,de,es,it,pt,ru,zh,ar,ko | required

Response schema (JSON object):
greeting | string | greeting message

"""

chain_new = APIChain.from_llm_and_api_docs(llm, GREETING_API_DOCS, verbose=True)

question = "ドイツの朝の挨拶は？"
print("Question:", question)
chain_new.run(question)
