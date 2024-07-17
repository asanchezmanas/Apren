from agency_swarm.tools import BaseTool
from pydantic import Field
import requests

class RepositoryAnalyzerTool(BaseTool):
    """
    This tool analyzes the repository structure, key components, and functionalities based on the fetched repository details.
    It parses the repository data to identify the main directories, files, and their purposes.
    It also identifies key components such as main scripts, configuration files, and documentation.
    """

    repo_details: dict = Field(
        ..., description="The fetched repository details in JSON format."
    )

    def parse_repository_structure(self):
        """
        Parse the repository details to identify the main directories and files.
        """
        structure = {
            "directories": [],
            "files": []
        }
        
        if "tree" in self.repo_details:
            for item in self.repo_details["tree"]:
                if item["type"] == "tree":
                    structure["directories"].append(item["path"])
                elif item["type"] == "blob":
                    structure["files"].append(item["path"])
        
        return structure

    def identify_key_components(self, structure):
        """
        Identify key components such as main scripts, configuration files, and documentation.
        """
        key_components = {
            "main_scripts": [],
            "config_files": [],
            "documentation": []
        }
        
        for file in structure["files"]:
            if file.endswith(".py") or file.endswith(".sh"):
                key_components["main_scripts"].append(file)
            elif file.endswith(".json") or file.endswith(".yaml") or file.endswith(".yml"):
                key_components["config_files"].append(file)
            elif file.lower().startswith("readme") or file.lower().startswith("docs"):
                key_components["documentation"].append(file)
        
        return key_components

    def prepare_summary_report(self, structure, key_components):
        """
        Prepare a summary report based on the analysis of the repository structure and key components.
        """
        report = "Repository Analysis Report\n"
        report += "===========================\n\n"
        
        report += "Main Directories:\n"
        for directory in structure["directories"]:
            report += f"- {directory}\n"
        
        report += "\nMain Files:\n"
        for file in structure["files"]:
            report += f"- {file}\n"
        
        report += "\nKey Components:\n"
        report += "---------------\n"
        
        report += "Main Scripts:\n"
        for script in key_components["main_scripts"]:
            report += f"- {script}\n"
        
        report += "\nConfiguration Files:\n"
        for config in key_components["config_files"]:
            report += f"- {config}\n"
        
        report += "\nDocumentation:\n"
        for doc in key_components["documentation"]:
            report += f"- {doc}\n"
        
        return report

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method should utilize the fields defined above to perform the task.
        """
        try:
            structure = self.parse_repository_structure()
            key_components = self.identify_key_components(structure)
            report = self.prepare_summary_report(structure, key_components)
            return report
        except Exception as e:
            return f"An error occurred during analysis: {e}"

# Example usage:
# repo_details = {
#     "tree": [
#         {"path": "src", "type": "tree"},
#         {"path": "src/main.py", "type": "blob"},
#         {"path": "README.md", "type": "blob"},
#         {"path": "config.yaml", "type": "blob"}
#     ]
# }
# tool = RepositoryAnalyzerTool(repo_details=repo_details)
# print(tool.run())