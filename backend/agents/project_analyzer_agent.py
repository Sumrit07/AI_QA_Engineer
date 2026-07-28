from backend.agents.supervisor_agent import SupervisorAgent


class ProjectAnalyzerAgent:

    def __init__(self):
        self.supervisor = SupervisorAgent()

    def analyze_project(self, project_path):

        result = self.supervisor.analyze_project(project_path)

        return result