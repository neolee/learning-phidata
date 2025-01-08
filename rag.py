from phi.agent.agent import Agent
from phi.embedder.ollama import OllamaEmbedder
from phi.knowledge.pdf import PDFKnowledgeBase
from phi.vectordb.lancedb.lance_db import LanceDb
from phi.vectordb.search import SearchType
import llm


model = llm.ollama

# create a knowledge base from a pdf
knowledge_base = PDFKnowledgeBase(
    path="db/pdfs",
    vector_db=LanceDb(
        table_name="articles",
        uri="db/lancedb",
        search_type=SearchType.vector,
        embedder=OllamaEmbedder(model="snowflake-arctic-embed2"),
        )
)

# BUG these 2 parameters not working for now, wait for phidata upcoming fix
knowledge_base.load(recreate=False, skip_existing=True) # type: ignore

agent = Agent(
    model=model, # type: ignore
    knowledge=knowledge_base, # type: ignore
    show_tool_calls=True,
    markdown=True,
)

# q = "What is the 'CAP Theorem'?"
q = "Explain to me what 'Illiberal Democracy' is"
# q = "What is the 'Conservative Promises'?"

agent.print_response(q, stream=True)
