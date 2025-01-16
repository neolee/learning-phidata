from phi.agent.agent import Agent
from phi.embedder.ollama import OllamaEmbedder
from phi.knowledge.pdf import PDFKnowledgeBase
from phi.vectordb.lancedb.lance_db import LanceDb
from phi.vectordb.search import SearchType
import llm


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

# these 2 parameters are set their default values, keep them here just for note
knowledge_base.load(recreate=False, skip_existing=True) # type: ignore

agent = Agent(
    model=llm.default, # type: ignore
    knowledge=knowledge_base, # type: ignore
    show_tool_calls=True,
    markdown=True,
)

# q = "What is the 'CAP Theorem' in software architecture?"
# q = "Explain to me what 'Illiberal Democracy' is"
q = "为什么我们要批判新制度经济学？"

agent.print_response(q, stream=True)
