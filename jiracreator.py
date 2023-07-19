import os
from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain.agents.agent_toolkits.jira.toolkit import JiraToolkit
from langchain.llms import OpenAI
from langchain.utilities.jira import JiraAPIWrapper
import constants

#organization id = 2d2dabf5-01e8-4787-8834-d86f8d968e8f
os.environ["JIRA_API_TOKEN"] = constants.JIRA_API_KEY
os.environ["JIRA_USERNAME"] = constants.JIRA_USER_NAME
os.environ["JIRA_INSTANCE_URL"] = "https://mygdock.atlassian.net"
os.environ["OPENAI_API_KEY"] = constants.APIKEY



llm = OpenAI(temperature=0)
jira = JiraAPIWrapper()
toolkit = JiraToolkit.from_jira_api_wrapper(jira)
agent = initialize_agent(
    toolkit.get_tools(), llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

agent.run("make a new issue in project company id PRJIS to remind me to make more fried rice")
#agent.run("make a new story in project TES to remind me to make more fried rice")