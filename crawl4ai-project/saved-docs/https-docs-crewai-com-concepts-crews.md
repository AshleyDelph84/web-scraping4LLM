# URL: https://docs.crewai.com/concepts/crews

**Scraped At:** 2025-01-23 22:25:59.512736

Search CrewAI docs
  * [crewAIInc/crewAI](https://docs.crewai.com/concepts/<https:/github.com/crewAIInc/crewAI>)
  * [crewAIInc/crewAI](https://docs.crewai.com/concepts/<https:/github.com/crewAIInc/crewAI>)
  * [Installation](https://docs.crewai.com/concepts/</installation>)
  * [Browserbase Web Loader](https://docs.crewai.com/concepts/</tools/browserbaseloadtool>)
  * [Code Docs RAG Search](https://docs.crewai.com/concepts/</tools/codedocssearchtool>)
  * [Code Interpreter](https://docs.crewai.com/concepts/</tools/codeinterpretertool>)
  * [Composio](https://docs.crewai.com/concepts/</tools/composiotool>)
  * [CSV RAG Search](https://docs.crewai.com/concepts/</tools/csvsearchtool>)
  * [DALL-E Tool](https://docs.crewai.com/concepts/</tools/dalletool>)
  * [Directory RAG Search](https://docs.crewai.com/concepts/</tools/directorysearchtool>)
  * [Directory Read](https://docs.crewai.com/concepts/</tools/directoryreadtool>)
  * [DOCX RAG Search](https://docs.crewai.com/concepts/</tools/docxsearchtool>)
  * [EXA Search Web Loader](https://docs.crewai.com/concepts/</tools/exasearchtool>)
  * [File Read](https://docs.crewai.com/concepts/</tools/filereadtool>)
  * [File Write](https://docs.crewai.com/concepts/</tools/filewritetool>)
  * [Firecrawl Crawl Website](https://docs.crewai.com/concepts/</tools/firecrawlcrawlwebsitetool>)
  * [Firecrawl Scrape Website](https://docs.crewai.com/concepts/</tools/firecrawlscrapewebsitetool>)
  * [Firecrawl Search](https://docs.crewai.com/concepts/</tools/firecrawlsearchtool>)
  * [Github Search](https://docs.crewai.com/concepts/</tools/githubsearchtool>)
  * [Google Serper Search](https://docs.crewai.com/concepts/</tools/serperdevtool>)
  * [JSON RAG Search](https://docs.crewai.com/concepts/</tools/jsonsearchtool>)
  * [MDX RAG Search](https://docs.crewai.com/concepts/</tools/mdxsearchtool>)
  * [MySQL RAG Search](https://docs.crewai.com/concepts/</tools/mysqltool>)
  * [NL2SQL Tool](https://docs.crewai.com/concepts/</tools/nl2sqltool>)
  * [PDF RAG Search](https://docs.crewai.com/concepts/</tools/pdfsearchtool>)
  * [PG RAG Search](https://docs.crewai.com/concepts/</tools/pgsearchtool>)
  * [Scrape Website](https://docs.crewai.com/concepts/</tools/scrapewebsitetool>)
  * [Selenium Scraper](https://docs.crewai.com/concepts/</tools/seleniumscrapingtool>)
  * [Spider Scraper](https://docs.crewai.com/concepts/</tools/spidertool>)
  * [TXT RAG Search](https://docs.crewai.com/concepts/</tools/txtsearchtool>)
  * [Vision Tool](https://docs.crewai.com/concepts/</tools/visiontool>)
  * [Website RAG Search](https://docs.crewai.com/concepts/</tools/websitesearchtool>)
  * [XML RAG Search](https://docs.crewai.com/concepts/</tools/xmlsearchtool>)
  * [YouTube Channel RAG Search](https://docs.crewai.com/concepts/</tools/youtubechannelsearchtool>)
  * [YouTube Video RAG Search](https://docs.crewai.com/concepts/</tools/youtubevideosearchtool>)
Understanding and utilizing crews in the crewAI framework with comprehensive attributes and functionalities.
## 
What is a Crew?
A crew in crewAI represents a collaborative group of agents working together to achieve a set of tasks. Each crew defines the strategy for task execution, agent collaboration, and the overall workflow.
## 
Crew Attributes
Attribute| Parameters| Description  
---|---|---  
**Process** _(optional)_| `process`|  The process flow (e.g., sequential, hierarchical) the crew follows. Default is `sequential`.  
**Verbose** _(optional)_| `verbose`|  The verbosity level for logging during execution. Defaults to `False`.  
**Manager LLM** _(optional)_| `manager_llm`|  The language model used by the manager agent in a hierarchical process. **Required when using a hierarchical process.**  
**Function Calling LLM** _(optional)_| `function_calling_llm`|  If passed, the crew will use this LLM to do function calling for tools for all agents in the crew. Each agent can have its own LLM, which overrides the crew’s LLM for function calling.  
**Config** _(optional)_| `config`|  Optional configuration settings for the crew, in `Json` or `Dict[str, Any]` format.  
**Max RPM** _(optional)_| `max_rpm`|  Maximum requests per minute the crew adheres to during execution. Defaults to `None`.  
**Language** _(optional)_| `language`|  Language used for the crew, defaults to English.  
**Language File** _(optional)_| `language_file`|  Path to the language file to be used for the crew.  
**Cache** _(optional)_| `cache`|  Specifies whether to use a cache for storing the results of tools’ execution. Defaults to `True`.  
**Embedder** _(optional)_| `embedder`|  Configuration for the embedder to be used by the crew. Mostly used by memory for now. Default is `{"provider": "openai"}`.  
**Full Output** _(optional)_| `full_output`|  Whether the crew should return the full output with all tasks outputs or just the final output. Defaults to `False`.  
**Step Callback** _(optional)_| `step_callback`|  A function that is called after each step of every agent. This can be used to log the agent’s actions or to perform other operations; it won’t override the agent-specific `step_callback`.  
**Task Callback** _(optional)_| `task_callback`|  A function that is called after the completion of each task. Useful for monitoring or additional operations post-task execution.  
**Share Crew** _(optional)_| `share_crew`|  Whether you want to share the complete crew information and execution with the crewAI team to make the library better, and allow us to train models.  
**Output Log File** _(optional)_| `output_log_file`|  Whether you want to have a file with the complete crew output and execution. You can set it using True and it will default to the folder you are currently in and it will be called logs.txt or passing a string with the full path and name of the file.  
**Manager Agent** _(optional)_| `manager_agent`| `manager` sets a custom agent that will be used as a manager.  
**Prompt File** _(optional)_| `prompt_file`|  Path to the prompt JSON file to be used for the crew.  
**Crew Max RPM** : The `max_rpm` attribute sets the maximum number of requests per minute the crew can perform to avoid rate limits and will override individual agents’ `max_rpm` settings if you set it.
## 
There are two ways to create crews in CrewAI: using **YAML configuration (recommended)** or defining them **directly in code**.
### 
YAML Configuration (Recommended)
Using YAML configuration provides a cleaner, more maintainable way to define crews and is consistent with how agents and tasks are defined in CrewAI projects.
After creating your CrewAI project as outlined in the [Installation](https://docs.crewai.com/concepts/</installation>) section, you can define your crew in a class that inherits from `CrewBase` and uses decorators to define agents, tasks, and the crew itself.
#### 
Example Crew Class with Decorators
code
Copy
```
from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, task, crew, before_kickoff, after_kickoff

@CrewBase
class YourCrewName:
  """Description of your crew"""
  # Paths to your YAML configuration files
  # To see an example agent and task defined in YAML, checkout the following:
  # - Task: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
  # - Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
  agents_config = 'config/agents.yaml' 
  tasks_config = 'config/tasks.yaml' 
  @before_kickoff
  def prepare_inputs(self, inputs):
    # Modify inputs before the crew starts
    inputs['additional_data'] = "Some extra information"
    return inputs
  @after_kickoff
  def process_output(self, output):
    # Modify output after the crew finishes
    output.raw += "\nProcessed after kickoff."
    return output
  @agent
  def agent_one(self) -> Agent:
    return Agent(
      config=self.agents_config['agent_one'],
      verbose=True
    )
  @agent
  def agent_two(self) -> Agent:
    return Agent(
      config=self.agents_config['agent_two'],
      verbose=True
    )
  @task
  def task_one(self) -> Task:
    return Task(
      config=self.tasks_config['task_one']
    )
  @task
  def task_two(self) -> Task:
    return Task(
      config=self.tasks_config['task_two']
    )
  @crew
  def crew(self) -> Crew:
    return Crew(
      agents=self.agents, # Automatically collected by the @agent decorator
      tasks=self.tasks,  # Automatically collected by the @task decorator. 
      process=Process.sequential,
      verbose=True,
    )

```
The `CrewBase` class, along with these decorators, automates the collection of agents and tasks, reducing the need for manual management.
#### 
Decorators overview from `annotations.py`
CrewAI provides several decorators in the `annotations.py` file that are used to mark methods within your crew class for special handling:
  * `@CrewBase`: Marks the class as a crew base class.
  * `@agent`: Denotes a method that returns an `Agent` object.
  * `@task`: Denotes a method that returns a `Task` object.
  * `@crew`: Denotes the method that returns the `Crew` object.
  * `@before_kickoff`: (Optional) Marks a method to be executed before the crew starts.
  * `@after_kickoff`: (Optional) Marks a method to be executed after the crew finishes.
These decorators help in organizing your crew’s structure and automatically collecting agents and tasks without manually listing them.
### 
Direct Code Definition (Alternative)
Alternatively, you can define the crew directly in code without using YAML configuration files.
code
Copy
```
from crewai import Agent, Crew, Task, Process
from crewai_tools import YourCustomTool
class YourCrewName:
  def agent_one(self) -> Agent:
    return Agent(
      role="Data Analyst",
      goal="Analyze data trends in the market",
      backstory="An experienced data analyst with a background in economics",
      verbose=True,
      tools=[YourCustomTool()]
    )
  def agent_two(self) -> Agent:
    return Agent(
      role="Market Researcher",
      goal="Gather information on market dynamics",
      backstory="A diligent researcher with a keen eye for detail",
      verbose=True
    )
  def task_one(self) -> Task:
    return Task(
      description="Collect recent market data and identify trends.",
      expected_output="A report summarizing key trends in the market.",
      agent=self.agent_one()
    )
  def task_two(self) -> Task:
    return Task(
      description="Research factors affecting market dynamics.",
      expected_output="An analysis of factors influencing the market.",
      agent=self.agent_two()
    )
  def crew(self) -> Crew:
    return Crew(
      agents=[self.agent_one(), self.agent_two()],
      tasks=[self.task_one(), self.task_two()],
      process=Process.sequential,
      verbose=True
    )

```
In this example:
  * We manually create and manage the list of agents and tasks.
  * This approach provides more control but can be less maintainable for larger projects.
## 
Crew Output
The output of a crew in the CrewAI framework is encapsulated within the `CrewOutput` class. This class provides a structured way to access results of the crew’s execution, including various formats such as raw strings, JSON, and Pydantic models. The `CrewOutput` includes the results from the final task output, token usage, and individual task outputs.
### 
Crew Output Attributes
Attribute| Parameters| Type| Description  
---|---|---|---  
**Raw**| `raw`| `str`|  The raw output of the crew. This is the default format for the output.  
**Pydantic**| `pydantic`| `Optional[BaseModel]`|  A Pydantic model object representing the structured output of the crew.  
**JSON Dict**| `json_dict`| `Optional[Dict[str, Any]]`|  A dictionary representing the JSON output of the crew.  
**Token Usage**| `token_usage`| `Dict[str, Any]`|  A summary of token usage, providing insights into the language model’s performance during execution.  
### 
Crew Output Methods and Properties
Method/Property| Description  
---|---  
**json**|  Returns the JSON string representation of the crew output if the output format is JSON.  
**to_dict**|  Converts the JSON and Pydantic outputs to a dictionary.  
* ***str****|  Returns the string representation of the crew output, prioritizing Pydantic, then JSON, then raw.  
### 
Accessing Crew Outputs
Once a crew has been executed, its output can be accessed through the `output` attribute of the `Crew` object. The `CrewOutput` class provides various ways to interact with and present this output.
#### 
Example
Code
Copy
```
# Example crew execution
crew = Crew(
  agents=[research_agent, writer_agent],
  tasks=[research_task, write_article_task],
  verbose=True
)
crew_output = crew.kickoff()
# Accessing the crew output
print(f"Raw Output: {crew_output.raw}")
if crew_output.json_dict:
  print(f"JSON Output: {json.dumps(crew_output.json_dict, indent=2)}")
if crew_output.pydantic:
  print(f"Pydantic Output: {crew_output.pydantic}")
print(f"Tasks Output: {crew_output.tasks_output}")
print(f"Token Usage: {crew_output.token_usage}")

```
## 
## 
Cache Utilization
Caches can be employed to store the results of tools’ execution, making the process more efficient by reducing the need to re-execute identical tasks.
## 
Crew Usage Metrics
After the crew execution, you can access the `usage_metrics` attribute to view the language model (LLM) usage metrics for all tasks executed by the crew. This provides insights into operational efficiency and areas for improvement.
Code
Copy
```
# Access the crew's usage metrics
crew = Crew(agents=[agent1, agent2], tasks=[task1, task2])
crew.kickoff()
print(crew.usage_metrics)

```
## 
Crew Execution Process
### 
Kicking Off a Crew
Once your crew is assembled, initiate the workflow with the `kickoff()` method. This starts the execution process according to the defined process flow.
Code
Copy
```
# Start the crew's task execution
result = my_crew.kickoff()
print(result)

```
### 
Different Ways to Kick Off a Crew
Once your crew is assembled, initiate the workflow with the appropriate kickoff method. CrewAI provides several methods for better control over the kickoff process: `kickoff()`, `kickoff_for_each()`, `kickoff_async()`, and `kickoff_for_each_async()`.
  * `kickoff()`: Starts the execution process according to the defined process flow.
  * `kickoff_for_each()`: Executes tasks for each agent individually.
  * `kickoff_async()`: Initiates the workflow asynchronously.
  * `kickoff_for_each_async()`: Executes tasks for each agent individually in an asynchronous manner.
Code
Copy
```
# Start the crew's task execution
result = my_crew.kickoff()
print(result)
# Example of using kickoff_for_each
inputs_array = [{'topic': 'AI in healthcare'}, {'topic': 'AI in finance'}]
results = my_crew.kickoff_for_each(inputs=inputs_array)
for result in results:
  print(result)
# Example of using kickoff_async
inputs = {'topic': 'AI in healthcare'}
async_result = my_crew.kickoff_async(inputs=inputs)
print(async_result)
# Example of using kickoff_for_each_async
inputs_array = [{'topic': 'AI in healthcare'}, {'topic': 'AI in finance'}]
async_results = my_crew.kickoff_for_each_async(inputs=inputs_array)
for async_result in async_results:
  print(async_result)

```
These methods provide flexibility in how you manage and execute tasks within your crew, allowing for both synchronous and asynchronous workflows tailored to your needs.
### 
Replaying from a Specific Task
Kickoffs will now save the latest kickoffs returned task outputs locally for you to be able to replay from.
### 
To use the replay feature, follow these steps:
  1. Open your terminal or command prompt.
  2. Navigate to the directory where your CrewAI project is located.
  3. Run the following command:
To view the latest kickoff task IDs, use:
Copy
```
crewai log-tasks-outputs

```
Then, to replay from a specific task, use:
Copy
```
crewai replay -t <task_id>

```
These commands let you replay from your latest kickoff tasks, still retaining context from previously executed tasks.
  * [What is a Crew?](https://docs.crewai.com/concepts/<#what-is-a-crew>)
  * [Crew Attributes](https://docs.crewai.com/concepts/<#crew-attributes>)
  * [YAML Configuration (Recommended)](https://docs.crewai.com/concepts/<#yaml-configuration-recommended>)
  * [Example Crew Class with Decorators](https://docs.crewai.com/concepts/<#example-crew-class-with-decorators>)
  * [Decorators overview from annotations.py](https://docs.crewai.com/concepts/<#decorators-overview-from-annotations-py>)
  * [Direct Code Definition (Alternative)](https://docs.crewai.com/concepts/<#direct-code-definition-alternative>)
  * [Crew Output](https://docs.crewai.com/concepts/<#crew-output>)
  * [Crew Output Attributes](https://docs.crewai.com/concepts/<#crew-output-attributes>)
  * [Crew Output Methods and Properties](https://docs.crewai.com/concepts/<#crew-output-methods-and-properties>)
  * [Accessing Crew Outputs](https://docs.crewai.com/concepts/<#accessing-crew-outputs>)
  * [Example](https://docs.crewai.com/concepts/<#example>)
  * [Cache Utilization](https://docs.crewai.com/concepts/<#cache-utilization>)
  * [Crew Usage Metrics](https://docs.crewai.com/concepts/<#crew-usage-metrics>)
  * [Crew Execution Process](https://docs.crewai.com/concepts/<#crew-execution-process>)
  * [Kicking Off a Crew](https://docs.crewai.com/concepts/<#kicking-off-a-crew>)
  * [Different Ways to Kick Off a Crew](https://docs.crewai.com/concepts/<#different-ways-to-kick-off-a-crew>)
  * [Replaying from a Specific Task](https://docs.crewai.com/concepts/<#replaying-from-a-specific-task>)