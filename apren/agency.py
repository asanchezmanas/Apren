from agency_swarm import Agency
from RoadmapCreator import RoadmapCreator
from StepByStepGuideCreator import StepByStepGuideCreator
from DetailedExplainer import DetailedExplainer
from ContentCreator import ContentCreator
from RepositoryAnalyzer import RepositoryAnalyzer
from AprenCEO import AprenCEO

ceo = AprenCEO()
repo_analyzer = RepositoryAnalyzer()
content_creator = ContentCreator()

agency = Agency([ceo, [ceo, repo_analyzer],
                 [repo_analyzer, content_creator],
                 [content_creator, ceo]],
                shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
                max_prompt_tokens=25000,  # default tokens in conversation for all agents
                temperature=0.3,  # default temperature for all agents
                )

if __name__ == '__main__':
    agency.demo_gradio()