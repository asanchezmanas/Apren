from agency_swarm.agents import Agent


class RepositoryAnalyzer(Agent):
    def __init__(self):
        super().__init__(
            name="RepositoryAnalyzer",
            description="Analyzes the GitHub repository, extracts relevant information, and prepares a summary of the repository structure, key components, and functionalities.",
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
