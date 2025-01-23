# URL: https://docs.crewai.com/concepts/tasks

**Scraped At:** 2025-01-23 22:25:59.501942

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
Detailed guide on managing and creating tasks within the CrewAI framework.
## 
Overview of a Task
In the CrewAI framework, a `Task` is a specific assignment completed by an `Agent`.
### 
Task Execution Flow
The execution flow is defined when creating the crew:
Code
Copy
```
crew = Crew(
  agents=[agent1, agent2],
  tasks=[task1, task2],
  process=Process.sequential # or Process.hierarchical
)

```
## 
Task Attributes
Attribute| Parameters| Type| Description  
---|---|---|---  
**Description**| `description`| `str`|  A clear, concise statement of what the task entails.  
**Expected Output**| `expected_output`| `str`|  A detailed description of what the task’s completion looks like.  
**Name** _(optional)_| `name`| `Optional[str]`|  A name identifier for the task.  
**Agent** _(optional)_| `agent`| `Optional[BaseAgent]`|  The agent responsible for executing the task.  
**Context** _(optional)_| `context`| `Optional[List["Task"]]`|  Other tasks whose outputs will be used as context for this task.  
**Async Execution** _(optional)_| `async_execution`| `Optional[bool]`|  Whether the task should be executed asynchronously. Defaults to False.  
**Config** _(optional)_| `config`| `Optional[Dict[str, Any]]`|  Task-specific configuration parameters.  
**Output File** _(optional)_| `output_file`| `Optional[str]`|  File path for storing the task output.  
**Output JSON** _(optional)_| `output_json`| `Optional[Type[BaseModel]]`|  A Pydantic model to structure the JSON output.  
**Output Pydantic** _(optional)_| `output_pydantic`| `Optional[Type[BaseModel]]`|  A Pydantic model for task output.  
**Callback** _(optional)_| `callback`| `Optional[Any]`|  Function/object to be executed after task completion.  
## 
There are two ways to create tasks in CrewAI: using **YAML configuration (recommended)** or defining them **directly in code**.
### 
YAML Configuration (Recommended)
Using YAML configuration provides a cleaner, more maintainable way to define tasks. We strongly recommend using this approach to define tasks in your CrewAI projects.
After creating your CrewAI project as outlined in the [Installation](https://docs.crewai.com/concepts/</installation>) section, navigate to the `src/latest_ai_development/config/tasks.yaml` file and modify the template to match your specific task requirements.
Variables in your YAML files (like `{topic}`) will be replaced with values from your inputs when running the crew:
Code
Copy
```
crew.kickoff(inputs={'topic': 'AI Agents'})

```
Here’s an example of how to configure tasks using YAML:
tasks.yaml
Copy
```
research_task:
 description: >
  Conduct a thorough research about {topic}
  Make sure you find any interesting and relevant information given
  the current year is 2024.
 expected_output: >
  A list with 10 bullet points of the most relevant information about {topic}
 agent: researcher
reporting_task:
 description: >
  Review the context you got and expand each topic into a full section for a report.
  Make sure the report is detailed and contains any and all relevant information.
 expected_output: >
  A fully fledge reports with the mains topics, each with a full section of information.
  Formatted as markdown without '```'
 agent: reporting_analyst
 output_file: report.md

```
To use this YAML configuration in your code, create a crew class that inherits from `CrewBase`:
crew.py
Copy
```
# src/latest_ai_development/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
@CrewBase
class LatestAiDevelopmentCrew():
 """LatestAiDevelopment crew"""
 @agent
 def researcher(self) -> Agent:
  return Agent(
   config=self.agents_config['researcher'],
   verbose=True,
   tools=[SerperDevTool()]
  )
 @agent
 def reporting_analyst(self) -> Agent:
  return Agent(
   config=self.agents_config['reporting_analyst'],
   verbose=True
  )
 @task
 def research_task(self) -> Task:
  return Task(
   config=self.tasks_config['research_task']
  )
 @task
 def reporting_task(self) -> Task:
  return Task(
   config=self.tasks_config['reporting_task']
  )
 @crew
 def crew(self) -> Crew:
  return Crew(
   agents=[
    self.researcher(),
    self.reporting_analyst()
   ],
   tasks=[
    self.research_task(),
    self.reporting_task()
   ],
   process=Process.sequential
  )

```
The names you use in your YAML files (`agents.yaml` and `tasks.yaml`) should match the method names in your Python code.
### 
Direct Code Definition (Alternative)
Alternatively, you can define tasks directly in your code without using YAML configuration:
task.py
Copy
```
from crewai import Task
research_task = Task(
  description="""
    Conduct a thorough research about AI Agents.
    Make sure you find any interesting and relevant information given
    the current year is 2024.
  """,
  expected_output="""
    A list with 10 bullet points of the most relevant information about AI Agents
  """,
  agent=researcher
)
reporting_task = Task(
  description="""
    Review the context you got and expand each topic into a full section for a report.
    Make sure the report is detailed and contains any and all relevant information.
  """,
  expected_output="""
    A fully fledge reports with the mains topics, each with a full section of information.
    Formatted as markdown without '```'
  """,
  agent=reporting_analyst,
  output_file="report.md"
)

```
Directly specify an `agent` for assignment or let the `hierarchical` CrewAI’s process decide based on roles, availability, etc.
## 
Task Output
Understanding task outputs is crucial for building effective AI workflows. CrewAI provides a structured way to handle task results through the `TaskOutput` class, which supports multiple output formats and can be easily passed between tasks.
The output of a task in CrewAI framework is encapsulated within the `TaskOutput` class. This class provides a structured way to access results of a task, including various formats such as raw output, JSON, and Pydantic models.
By default, the `TaskOutput` will only include the `raw` output. A `TaskOutput` will only include the `pydantic` or `json_dict` output if the original `Task` object was configured with `output_pydantic` or `output_json`, respectively.
### 
Task Output Attributes
Attribute| Parameters| Type| Description  
---|---|---|---  
**Description**| `description`| `str`|  Description of the task.  
**Summary**| `summary`| `Optional[str]`|  Summary of the task, auto-generated from the first 10 words of the description.  
**Raw**| `raw`| `str`|  The raw output of the task. This is the default format for the output.  
**Pydantic**| `pydantic`| `Optional[BaseModel]`|  A Pydantic model object representing the structured output of the task.  
**JSON Dict**| `json_dict`| `Optional[Dict[str, Any]]`|  A dictionary representing the JSON output of the task.  
**Agent**| `agent`| `str`|  The agent that executed the task.  
**Output Format**| `output_format`| `OutputFormat`|  The format of the task output, with options including RAW, JSON, and Pydantic. The default is RAW.  
### 
Task Methods and Properties
Method/Property| Description  
---|---  
**json**|  Returns the JSON string representation of the task output if the output format is JSON.  
**to_dict**|  Converts the JSON and Pydantic outputs to a dictionary.  
**str**|  Returns the string representation of the task output, prioritizing Pydantic, then JSON, then raw.  
### 
Accessing Task Outputs
Once a task has been executed, its output can be accessed through the `output` attribute of the `Task` object. The `TaskOutput` class provides various ways to interact with and present this output.
#### 
Example
Code
Copy
```
# Example task
task = Task(
  description='Find and summarize the latest AI news',
  expected_output='A bullet list summary of the top 5 most important AI news',
  agent=research_agent,
  tools=[search_tool]
)
# Execute the crew
crew = Crew(
  agents=[research_agent],
  tasks=[task],
  verbose=True
)
result = crew.kickoff()
# Accessing the task output
task_output = task.output
print(f"Task Description: {task_output.description}")
print(f"Task Summary: {task_output.summary}")
print(f"Raw Output: {task_output.raw}")
if task_output.json_dict:
  print(f"JSON Output: {json.dumps(task_output.json_dict, indent=2)}")
if task_output.pydantic:
  print(f"Pydantic Output: {task_output.pydantic}")

```
## 
Task Dependencies and Context
Code
Copy
```
research_task = Task(
  description="Research the latest developments in AI",
  expected_output="A list of recent AI developments",
  agent=researcher
)
analysis_task = Task(
  description="Analyze the research findings and identify key trends",
  expected_output="Analysis report of AI trends",
  agent=analyst,
  context=[research_task] # This task will wait for research_task to complete
)

```
## 
Task Guardrails
Task guardrails provide a way to validate and transform task outputs before they are passed to the next task. This feature helps ensure data quality and provides efeedback to agents when their output doesn’t meet specific criteria.
### 
Using Task Guardrails
To add a guardrail to a task, provide a validation function through the `guardrail` parameter:
Code
Copy
```
from typing import Tuple, Union, Dict, Any
def validate_blog_content(result: str) -> Tuple[bool, Union[Dict[str, Any], str]]:
  """Validate blog content meets requirements."""
  try:
    # Check word count
    word_count = len(result.split())
    if word_count > 200:
      return (False, {
        "error": "Blog content exceeds 200 words",
        "code": "WORD_COUNT_ERROR",
        "context": {"word_count": word_count}
      })
    # Additional validation logic here
    return (True, result.strip())
  except Exception as e:
    return (False, {
      "error": "Unexpected error during validation",
      "code": "SYSTEM_ERROR"
    })
blog_task = Task(
  description="Write a blog post about AI",
  expected_output="A blog post under 200 words",
  agent=blog_agent,
  guardrail=validate_blog_content # Add the guardrail function
)

```
### 
Guardrail Function Requirements
  1. **Function Signature** :
     * Must accept exactly one parameter (the task output)
     * Should return a tuple of `(bool, Any)`
     * Type hints are recommended but optional
  2. **Return Values** :
     * Success: Return `(True, validated_result)`
     * Failure: Return `(False, error_details)`
### 
Error Handling Best Practices
  1. **Structured Error Responses** :
Code
Copy
```
def validate_with_context(result: str) -> Tuple[bool, Union[Dict[str, Any], str]]:
  try:
    # Main validation logic
    validated_data = perform_validation(result)
    return (True, validated_data)
  except ValidationError as e:
    return (False, {
      "error": str(e),
      "code": "VALIDATION_ERROR",
      "context": {"input": result}
    })
  except Exception as e:
    return (False, {
      "error": "Unexpected error",
      "code": "SYSTEM_ERROR"
    })

```
  1. **Error Categories** :
     * Use specific error codes
     * Include relevant context
     * Provide actionable feedback
  2. **Validation Chain** :
Code
Copy
```
from typing import Any, Dict, List, Tuple, Union
def complex_validation(result: str) -> Tuple[bool, Union[str, Dict[str, Any]]]:
  """Chain multiple validation steps."""
  # Step 1: Basic validation
  if not result:
    return (False, {"error": "Empty result", "code": "EMPTY_INPUT"})
  # Step 2: Content validation
  try:
    validated = validate_content(result)
    if not validated:
      return (False, {"error": "Invalid content", "code": "CONTENT_ERROR"})
    # Step 3: Format validation
    formatted = format_output(validated)
    return (True, formatted)
  except Exception as e:
    return (False, {
      "error": str(e),
      "code": "VALIDATION_ERROR",
      "context": {"step": "content_validation"}
    })

```
### 
Handling Guardrail Results
When a guardrail returns `(False, error)`:
  1. The error is sent back to the agent
  2. The agent attempts to fix the issue
  3. The process repeats until: 
     * The guardrail returns `(True, result)`
     * Maximum retries are reached
Example with retry handling:
Code
Copy
```
from typing import Optional, Tuple, Union
def validate_json_output(result: str) -> Tuple[bool, Union[Dict[str, Any], str]]:
  """Validate and parse JSON output."""
  try:
    # Try to parse as JSON
    data = json.loads(result)
    return (True, data)
  except json.JSONDecodeError as e:
    return (False, {
      "error": "Invalid JSON format",
      "code": "JSON_ERROR",
      "context": {"line": e.lineno, "column": e.colno}
    })
task = Task(
  description="Generate a JSON report",
  expected_output="A valid JSON object",
  agent=analyst,
  guardrail=validate_json_output,
  max_retries=3 # Limit retry attempts
)

```
## 
It’s also important to note that the output of the final task of a crew becomes the final output of the actual crew itself.
### 
Using `output_pydantic`
The `output_pydantic` property allows you to define a Pydantic model that the task output should conform to. This ensures that the output is not only structured but also validated according to the Pydantic model.
Here’s an example demonstrating how to use output_pydantic:
Code
Copy
```
import json
from crewai import Agent, Crew, Process, Task
from pydantic import BaseModel

class Blog(BaseModel):
  title: str
  content: str

blog_agent = Agent(
  role="Blog Content Generator Agent",
  goal="Generate a blog title and content",
  backstory="""You are an expert content creator, skilled in crafting engaging and informative blog posts.""",
  verbose=False,
  allow_delegation=False,
  llm="gpt-4o",
)
task1 = Task(
  description="""Create a blog title and content on a given topic. Make sure the content is under 200 words.""",
  expected_output="A compelling blog title and well-written content.",
  agent=blog_agent,
  output_pydantic=Blog,
)
# Instantiate your crew with a sequential process
crew = Crew(
  agents=[blog_agent],
  tasks=[task1],
  verbose=True,
  process=Process.sequential,
)
result = crew.kickoff()
# Option 1: Accessing Properties Using Dictionary-Style Indexing
print("Accessing Properties - Option 1")
title = result["title"]
content = result["content"]
print("Title:", title)
print("Content:", content)
# Option 2: Accessing Properties Directly from the Pydantic Model
print("Accessing Properties - Option 2")
title = result.pydantic.title
content = result.pydantic.content
print("Title:", title)
print("Content:", content)
# Option 3: Accessing Properties Using the to_dict() Method
print("Accessing Properties - Option 3")
output_dict = result.to_dict()
title = output_dict["title"]
content = output_dict["content"]
print("Title:", title)
print("Content:", content)
# Option 4: Printing the Entire Blog Object
print("Accessing Properties - Option 5")
print("Blog:", result)

```
In this example:
  * A Pydantic model Blog is defined with title and content fields.
  * The task task1 uses the output_pydantic property to specify that its output should conform to the Blog model.
  * After executing the crew, you can access the structured output in multiple ways as shown.
#### 
Explanation of Accessing the Output
  1. Dictionary-Style Indexing: You can directly access the fields using result[“field_name”]. This works because the CrewOutput class implements the **getitem** method.
  2. Directly from Pydantic Model: Access the attributes directly from the result.pydantic object.
  3. Using to_dict() Method: Convert the output to a dictionary and access the fields.
  4. Printing the Entire Object: Simply print the result object to see the structured output.
### 
Using `output_json`
The `output_json` property allows you to define the expected output in JSON format. This ensures that the task’s output is a valid JSON structure that can be easily parsed and used in your application.
Here’s an example demonstrating how to use `output_json`:
Code
Copy
```
import json
from crewai import Agent, Crew, Process, Task
from pydantic import BaseModel

# Define the Pydantic model for the blog
class Blog(BaseModel):
  title: str
  content: str

# Define the agent
blog_agent = Agent(
  role="Blog Content Generator Agent",
  goal="Generate a blog title and content",
  backstory="""You are an expert content creator, skilled in crafting engaging and informative blog posts.""",
  verbose=False,
  allow_delegation=False,
  llm="gpt-4o",
)
# Define the task with output_json set to the Blog model
task1 = Task(
  description="""Create a blog title and content on a given topic. Make sure the content is under 200 words.""",
  expected_output="A JSON object with 'title' and 'content' fields.",
  agent=blog_agent,
  output_json=Blog,
)
# Instantiate the crew with a sequential process
crew = Crew(
  agents=[blog_agent],
  tasks=[task1],
  verbose=True,
  process=Process.sequential,
)
# Kickoff the crew to execute the task
result = crew.kickoff()
# Option 1: Accessing Properties Using Dictionary-Style Indexing
print("Accessing Properties - Option 1")
title = result["title"]
content = result["content"]
print("Title:", title)
print("Content:", content)
# Option 2: Printing the Entire Blog Object
print("Accessing Properties - Option 2")
print("Blog:", result)

```
In this example:
  * A Pydantic model Blog is defined with title and content fields, which is used to specify the structure of the JSON output.
  * The task task1 uses the output_json property to indicate that it expects a JSON output conforming to the Blog model.
  * After executing the crew, you can access the structured JSON output in two ways as shown.
#### 
Explanation of Accessing the Output
  1. Accessing Properties Using Dictionary-Style Indexing: You can access the fields directly using result[“field_name”]. This is possible because the CrewOutput class implements the **getitem** method, allowing you to treat the output like a dictionary. In this option, we’re retrieving the title and content from the result.
  2. Printing the Entire Blog Object: By printing result, you get the string representation of the CrewOutput object. Since the **str** method is implemented to return the JSON output, this will display the entire output as a formatted string representing the Blog object.
By using output_pydantic or output_json, you ensure that your tasks produce outputs in a consistent and structured format, making it easier to process and utilize the data within your application or across multiple tasks.
## 
## 
Code
Copy
```
import os
os.environ["OPENAI_API_KEY"] = "Your Key"
os.environ["SERPER_API_KEY"] = "Your Key" # serper.dev API key
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
research_agent = Agent(
 role='Researcher',
 goal='Find and summarize the latest AI news',
 backstory="""You're a researcher at a large company.
 You're responsible for analyzing data and providing insights
 to the business.""",
 verbose=True
)
# to perform a semantic search for a specified query from a text's content across the internet
search_tool = SerperDevTool()
task = Task(
 description='Find and summarize the latest AI news',
 expected_output='A bullet list summary of the top 5 most important AI news',
 agent=research_agent,
 tools=[search_tool]
)
crew = Crew(
  agents=[research_agent],
  tasks=[task],
  verbose=True
)
result = crew.kickoff()
print(result)

```
This demonstrates how tasks with specific tools can override an agent’s default set for tailored task execution.
## 
In CrewAI, the output of one task is automatically relayed into the next one, but you can specifically define what tasks’ output, including multiple, should be used as context for another task.
This is useful when you have a task that depends on the output of another task that is not performed immediately after it. This is done through the `context` attribute of the task:
Code
Copy
```
# ...
research_ai_task = Task(
  description="Research the latest developments in AI",
  expected_output="A list of recent AI developments",
  async_execution=True,
  agent=research_agent,
  tools=[search_tool]
)
research_ops_task = Task(
  description="Research the latest developments in AI Ops",
  expected_output="A list of recent AI Ops developments",
  async_execution=True,
  agent=research_agent,
  tools=[search_tool]
)
write_blog_task = Task(
  description="Write a full blog post about the importance of AI and its latest news",
  expected_output="Full blog post that is 4 paragraphs long",
  agent=writer_agent,
  context=[research_ai_task, research_ops_task]
)
#...

```
## 
Asynchronous Execution
You can define a task to be executed asynchronously. This means that the crew will not wait for it to be completed to continue with the next task. This is useful for tasks that take a long time to be completed, or that are not crucial for the next tasks to be performed.
You can then use the `context` attribute to define in a future task that it should wait for the output of the asynchronous task to be completed.
Code
Copy
```
#...
list_ideas = Task(
  description="List of 5 interesting ideas to explore for an article about AI.",
  expected_output="Bullet point list of 5 ideas for an article.",
  agent=researcher,
  async_execution=True # Will be executed asynchronously
)
list_important_history = Task(
  description="Research the history of AI and give me the 5 most important events.",
  expected_output="Bullet point list of 5 important events.",
  agent=researcher,
  async_execution=True # Will be executed asynchronously
)
write_article = Task(
  description="Write an article about AI, its history, and interesting ideas.",
  expected_output="A 4 paragraph article about AI.",
  agent=writer,
  context=[list_ideas, list_important_history] # Will wait for the output of the two tasks to be completed
)
#...

```
## 
Callback Mechanism
The callback function is executed after the task is completed, allowing for actions or notifications to be triggered based on the task’s outcome.
Code
Copy
```
# ...
def callback_function(output: TaskOutput):
  # Do something after the task is completed
  # Example: Send an email to the manager
  print(f"""
    Task completed!
    Task: {output.description}
    Output: {output.raw}
  """)
research_task = Task(
  description='Find and summarize the latest AI news',
  expected_output='A bullet list summary of the top 5 most important AI news',
  agent=research_agent,
  tools=[search_tool],
  callback=callback_function
)
#...

```
## 
Accessing a Specific Task Output
Once a crew finishes running, you can access the output of a specific task by using the `output` attribute of the task object:
Code
Copy
```
# ...
task1 = Task(
  description='Find and summarize the latest AI news',
  expected_output='A bullet list summary of the top 5 most important AI news',
  agent=research_agent,
  tools=[search_tool]
)
#...
crew = Crew(
  agents=[research_agent],
  tasks=[task1, task2, task3],
  verbose=True
)
result = crew.kickoff()
# Returns a TaskOutput object with the description and results of the task
print(f"""
  Task completed!
  Task: {task1.output.description}
  Output: {task1.output.raw}
""")

```
## 
Tool Override Mechanism
Specifying tools in a task allows for dynamic adaptation of agent capabilities, emphasizing CrewAI’s flexibility.
## 
Error Handling and Validation Mechanisms
While creating and executing tasks, certain validation mechanisms are in place to ensure the robustness and reliability of task attributes. These include but are not limited to:
  * Ensuring only one output type is set per task to maintain clear output expectations.
  * Preventing the manual assignment of the `id` attribute to uphold the integrity of the unique identifier system.
These validations help in maintaining the consistency and reliability of task executions within the crewAI framework.
## 
Task Guardrails
Task guardrails provide a powerful way to validate, transform, or filter task outputs before they are passed to the next task. Guardrails are optional functions that execute before the next task starts, allowing you to ensure that task outputs meet specific requirements or formats.
### 
Basic Usage
Code
Copy
```
from typing import Tuple, Union
from crewai import Task
def validate_json_output(result: str) -> Tuple[bool, Union[dict, str]]:
  """Validate that the output is valid JSON."""
  try:
    json_data = json.loads(result)
    return (True, json_data)
  except json.JSONDecodeError:
    return (False, "Output must be valid JSON")
task = Task(
  description="Generate JSON data",
  expected_output="Valid JSON object",
  guardrail=validate_json_output
)

```
### 
How Guardrails Work
  1. **Optional Attribute** : Guardrails are an optional attribute at the task level, allowing you to add validation only where needed.
  2. **Execution Timing** : The guardrail function is executed before the next task starts, ensuring valid data flow between tasks.
  3. **Return Format** : Guardrails must return a tuple of `(success, data)`: 
     * If `success` is `True`, `data` is the validated/transformed result
     * If `success` is `False`, `data` is the error message
  4. **Result Routing** : 
     * On success (`True`), the result is automatically passed to the next task
     * On failure (`False`), the error is sent back to the agent to generate a new answer
### 
Common Use Cases
#### 
Data Format Validation
Code
Copy
```
def validate_email_format(result: str) -> Tuple[bool, Union[str, str]]:
  """Ensure the output contains a valid email address."""
  import re
  email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
  if re.match(email_pattern, result.strip()):
    return (True, result.strip())
  return (False, "Output must be a valid email address")

```
#### 
Content Filtering
Code
Copy
```
def filter_sensitive_info(result: str) -> Tuple[bool, Union[str, str]]:
  """Remove or validate sensitive information."""
  sensitive_patterns = ['SSN:', 'password:', 'secret:']
  for pattern in sensitive_patterns:
    if pattern.lower() in result.lower():
      return (False, f"Output contains sensitive information ({pattern})")
  return (True, result)

```
#### 
Data Transformation
Code
Copy
```
def normalize_phone_number(result: str) -> Tuple[bool, Union[str, str]]:
  """Ensure phone numbers are in a consistent format."""
  import re
  digits = re.sub(r'\D', '', result)
  if len(digits) == 10:
    formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return (True, formatted)
  return (False, "Output must be a 10-digit phone number")

```
### 
Advanced Features
#### 
Chaining Multiple Validations
Code
Copy
```
def chain_validations(*validators):
  """Chain multiple validators together."""
  def combined_validator(result):
    for validator in validators:
      success, data = validator(result)
      if not success:
        return (False, data)
      result = data
    return (True, result)
  return combined_validator
# Usage
task = Task(
  description="Get user contact info",
  expected_output="Email and phone",
  guardrail=chain_validations(
    validate_email_format,
    filter_sensitive_info
  )
)

```
#### 
Custom Retry Logic
Code
Copy
```
task = Task(
  description="Generate data",
  expected_output="Valid data",
  guardrail=validate_data,
  max_retries=5 # Override default retry limit
)

```
## 
Creating Directories when Saving Files
You can now specify if a task should create directories when saving its output to a file. This is particularly useful for organizing outputs and ensuring that file paths are correctly structured.
Code
Copy
```
# ...
save_output_task = Task(
  description='Save the summarized AI news to a file',
  expected_output='File saved successfully',
  agent=research_agent,
  tools=[file_save_tool],
  output_file='outputs/ai_news_summary.txt',
  create_directory=True
)
#...

```
## 
Conclusion
  * [Overview of a Task](https://docs.crewai.com/concepts/<#overview-of-a-task>)
  * [Task Execution Flow](https://docs.crewai.com/concepts/<#task-execution-flow>)
  * [Task Attributes](https://docs.crewai.com/concepts/<#task-attributes>)
  * [YAML Configuration (Recommended)](https://docs.crewai.com/concepts/<#yaml-configuration-recommended>)
  * [Direct Code Definition (Alternative)](https://docs.crewai.com/concepts/<#direct-code-definition-alternative>)
  * [Task Output](https://docs.crewai.com/concepts/<#task-output>)
  * [Task Output Attributes](https://docs.crewai.com/concepts/<#task-output-attributes>)
  * [Task Methods and Properties](https://docs.crewai.com/concepts/<#task-methods-and-properties>)
  * [Accessing Task Outputs](https://docs.crewai.com/concepts/<#accessing-task-outputs>)
  * [Example](https://docs.crewai.com/concepts/<#example>)
  * [Task Dependencies and Context](https://docs.crewai.com/concepts/<#task-dependencies-and-context>)
  * [Task Guardrails](https://docs.crewai.com/concepts/<#task-guardrails>)
  * [Using Task Guardrails](https://docs.crewai.com/concepts/<#using-task-guardrails>)
  * [Guardrail Function Requirements](https://docs.crewai.com/concepts/<#guardrail-function-requirements>)
  * [Error Handling Best Practices](https://docs.crewai.com/concepts/<#error-handling-best-practices>)
  * [Handling Guardrail Results](https://docs.crewai.com/concepts/<#handling-guardrail-results>)
  * [Using output_pydantic](https://docs.crewai.com/concepts/<#using-output-pydantic>)
  * [Explanation of Accessing the Output](https://docs.crewai.com/concepts/<#explanation-of-accessing-the-output>)
  * [Using output_json](https://docs.crewai.com/concepts/<#using-output-json>)
  * [Explanation of Accessing the Output](https://docs.crewai.com/concepts/<#explanation-of-accessing-the-output-2>)
  * [Asynchronous Execution](https://docs.crewai.com/concepts/<#asynchronous-execution>)
  * [Callback Mechanism](https://docs.crewai.com/concepts/<#callback-mechanism>)
  * [Accessing a Specific Task Output](https://docs.crewai.com/concepts/<#accessing-a-specific-task-output>)
  * [Tool Override Mechanism](https://docs.crewai.com/concepts/<#tool-override-mechanism>)
  * [Error Handling and Validation Mechanisms](https://docs.crewai.com/concepts/<#error-handling-and-validation-mechanisms>)
  * [Task Guardrails](https://docs.crewai.com/concepts/<#task-guardrails-2>)
  * [Basic Usage](https://docs.crewai.com/concepts/<#basic-usage>)
  * [How Guardrails Work](https://docs.crewai.com/concepts/<#how-guardrails-work>)
  * [Common Use Cases](https://docs.crewai.com/concepts/<#common-use-cases>)
  * [Data Format Validation](https://docs.crewai.com/concepts/<#data-format-validation>)
  * [Content Filtering](https://docs.crewai.com/concepts/<#content-filtering>)
  * [Data Transformation](https://docs.crewai.com/concepts/<#data-transformation>)
  * [Advanced Features](https://docs.crewai.com/concepts/<#advanced-features>)
  * [Chaining Multiple Validations](https://docs.crewai.com/concepts/<#chaining-multiple-validations>)
  * [Custom Retry Logic](https://docs.crewai.com/concepts/<#custom-retry-logic>)
  * [Creating Directories when Saving Files](https://docs.crewai.com/concepts/<#creating-directories-when-saving-files>)
  * [Conclusion](https://docs.crewai.com/concepts/<#conclusion>)