from agency_swarm.agents import Agent


class DetailedExplainer(Agent):
    def __init__(self):
        super().__init__(
            name="DetailedExplainer",
            description="Provides detailed explanations of the repository.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )
        
    def response_validator(self, message):
        return message
