from agency_swarm.agents import Agent


class RoadmapCreator(Agent):
    def __init__(self):
        super().__init__(
            name="RoadmapCreator",
            description="Creates a comprehensive roadmap to replicate the repository, including a step-by-step guide to build the same project.",
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
