from __future__ import annotations

from typing import Any
from typing import Literal

from langgraph.graph import END
from langgraph.graph.state import CompiledStateGraph
from langgraph.graph.state import StateGraph
from langgraph.pregel import RetryPolicy

from .states import TableSummarizationState
from .table_summarization_agent import TableSummarizationAgent
from app.externals.agents.base.workflow_manager import BaseWorkflow


class Workflow(BaseWorkflow):

    def __init__(self):
        super().__init__()
        self.agent = TableSummarizationAgent()
        self.graph = self.get_graph()

    def create_workflow(self) -> StateGraph:
        """Define and configure the workflow graph."""
        workflow = StateGraph(TableSummarizationState)

        # Create nodes
        for node_name, node in self.agent.mapping_name_node.items():
            workflow.add_node(
                node_name,
                node,
                retry=RetryPolicy(max_attempts=2),
            )

        # Create edges
        def route_workflow(
            state: TableSummarizationState,
        ) -> Literal['continue', 'end']:
            if state['flow'] == 'continue':
                return 'continue'
            return 'end'

        workflow.set_entry_point('get_schema')
        workflow.add_conditional_edges(
            'get_schema',
            route_workflow,
            {'continue': 'summarize', 'end': END},
        )
        workflow.add_edge('summarize', END)

        return workflow

    def get_graph(self) -> CompiledStateGraph:
        """Return the compiled workflow graph."""
        return self.create_workflow().compile()

    async def run_agent(self, *args: Any, **kwds: Any):
        """Execute the workflow and return the result."""
        result = await self.graph.ainvoke(
            kwds,
        )
        return result
