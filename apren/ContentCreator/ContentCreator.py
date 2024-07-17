from agency_swarm.agents import Agent


class ContentCreator(Agent):
    def __init__(self):
        super().__init__(
            name="ContentCreator",
            description="Creates detailed and easy-to-understand explanations based on the analysis provided by the RepositoryAnalyzer. Focuses on making the content educational and accessible.",
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
