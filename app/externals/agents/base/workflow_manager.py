from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import Any

from IPython.display import display
from IPython.display import Image
from langgraph.graph.state import CompiledStateGraph
from langgraph.graph.state import StateGraph
from loguru import logger


class BaseWorkflow(ABC):
    """Abstract base class for defining a workflow system."""

    def __init__(self):
        super().__init__()

    @abstractmethod
    def create_workflow(self) -> StateGraph:
        """Define and configure the workflow graph."""
        pass

    @abstractmethod
    def get_graph(self) -> CompiledStateGraph:
        """Return the compiled workflow graph."""
        pass

    @abstractmethod
    async def run_agent(self, *args: Any, **kwds: Any):
        """Execute the workflow and return the result."""
        pass

    def display_graph(self, graph: CompiledStateGraph):
        try:
            display(Image(graph.get_graph(xray=True).draw_mermaid_png()))
        except Exception as e:
            logger.exception(e)
