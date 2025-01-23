# URL: https://docs.crewai.com/installation

**Scraped At:** 2025-01-23 22:25:59.483600

Search CrewAI docs
  * [crewAIInc/crewAI](https://docs.crewai.com/<https:/github.com/crewAIInc/crewAI>)
  * [crewAIInc/crewAI](https://docs.crewai.com/<https:/github.com/crewAIInc/crewAI>)
Installation
  * [Installation](https://docs.crewai.com/</installation>)
  * [Browserbase Web Loader](https://docs.crewai.com/</tools/browserbaseloadtool>)
  * [Code Docs RAG Search](https://docs.crewai.com/</tools/codedocssearchtool>)
  * [Code Interpreter](https://docs.crewai.com/</tools/codeinterpretertool>)
  * [Composio](https://docs.crewai.com/</tools/composiotool>)
  * [CSV RAG Search](https://docs.crewai.com/</tools/csvsearchtool>)
  * [DALL-E Tool](https://docs.crewai.com/</tools/dalletool>)
  * [Directory RAG Search](https://docs.crewai.com/</tools/directorysearchtool>)
  * [Directory Read](https://docs.crewai.com/</tools/directoryreadtool>)
  * [DOCX RAG Search](https://docs.crewai.com/</tools/docxsearchtool>)
  * [EXA Search Web Loader](https://docs.crewai.com/</tools/exasearchtool>)
  * [File Read](https://docs.crewai.com/</tools/filereadtool>)
  * [File Write](https://docs.crewai.com/</tools/filewritetool>)
  * [Firecrawl Crawl Website](https://docs.crewai.com/</tools/firecrawlcrawlwebsitetool>)
  * [Firecrawl Scrape Website](https://docs.crewai.com/</tools/firecrawlscrapewebsitetool>)
  * [Firecrawl Search](https://docs.crewai.com/</tools/firecrawlsearchtool>)
  * [Github Search](https://docs.crewai.com/</tools/githubsearchtool>)
  * [Google Serper Search](https://docs.crewai.com/</tools/serperdevtool>)
  * [JSON RAG Search](https://docs.crewai.com/</tools/jsonsearchtool>)
  * [MDX RAG Search](https://docs.crewai.com/</tools/mdxsearchtool>)
  * [MySQL RAG Search](https://docs.crewai.com/</tools/mysqltool>)
  * [NL2SQL Tool](https://docs.crewai.com/</tools/nl2sqltool>)
  * [PDF RAG Search](https://docs.crewai.com/</tools/pdfsearchtool>)
  * [PG RAG Search](https://docs.crewai.com/</tools/pgsearchtool>)
  * [Scrape Website](https://docs.crewai.com/</tools/scrapewebsitetool>)
  * [Selenium Scraper](https://docs.crewai.com/</tools/seleniumscrapingtool>)
  * [Spider Scraper](https://docs.crewai.com/</tools/spidertool>)
  * [TXT RAG Search](https://docs.crewai.com/</tools/txtsearchtool>)
  * [Vision Tool](https://docs.crewai.com/</tools/visiontool>)
  * [Website RAG Search](https://docs.crewai.com/</tools/websitesearchtool>)
  * [XML RAG Search](https://docs.crewai.com/</tools/xmlsearchtool>)
  * [YouTube Channel RAG Search](https://docs.crewai.com/</tools/youtubechannelsearchtool>)
  * [YouTube Video RAG Search](https://docs.crewai.com/</tools/youtubevideosearchtool>)
# Installation
Get started with CrewAI - Install, configure, and build your first AI crew
**Python Version Requirements**
CrewAI requires `Python >=3.10 and <3.13`. Here’s how to check your version:
Copy
```
python3 --version

```
If you need to update Python, visit [python.org/downloads](https://docs.crewai.com/<https:/python.org/downloads>)
# 
Installing CrewAI
CrewAI is a flexible and powerful AI framework that enables you to create and manage AI agents, tools, and tasks efficiently. Let’s get you set up! 🚀
1
Install CrewAI
Install CrewAI with all recommended tools using either method:
Terminal
Copy
```
pip install 'crewai[tools]'

```
or
Terminal
Copy
```
pip install crewai crewai-tools

```
Both methods install the core package and additional tools needed for most use cases.
2
Upgrade CrewAI (Existing Installations Only)
If you have an older version of CrewAI installed, you can upgrade it:
Terminal
Copy
```
pip install --upgrade crewai crewai-tools

```
If you see a Poetry-related warning, you’ll need to migrate to our new dependency manager:
Terminal
Copy
```
crewai update

```
This will update your project to use [UV](https://docs.crewai.com/<https:/github.com/astral-sh/uv>), our new faster dependency manager.
Skip this step if you’re doing a fresh installation.
3
Verify Installation
Check your installed versions:
Terminal
Copy
```
pip freeze | grep crewai

```
You should see something like:
Output
Copy
```
crewai==X.X.X
crewai-tools==X.X.X

```
Installation successful! You’re ready to create your first crew.
# 
Creating a New Project
We recommend using the YAML Template scaffolding for a structured approach to defining agents and tasks.
1
Generate Project Structure
Terminal
Copy
```
crewai create crew <project_name>

```
This creates a new project with the following structure:
Copy
```
my_project/
├── .gitignore
├── pyproject.toml
├── README.md
├── .env
└── src/
  └── my_project/
    ├── __init__.py
    ├── main.py
    ├── crew.py
    ├── tools/
    │  ├── custom_tool.py
    │  └── __init__.py
    └── config/
      ├── agents.yaml
      └── tasks.yaml

```
2
Customize Your Project
Your project will contain these essential files:
File| Purpose  
---|---  
`agents.yaml`| Define your AI agents and their roles  
`tasks.yaml`| Set up agent tasks and workflows  
`.env`| Store API keys and environment variables  
`main.py`| Project entry point and execution flow  
`crew.py`| Crew orchestration and coordination  
`tools/`| Directory for custom agent tools  
Start by editing `agents.yaml` and `tasks.yaml` to define your crew’s behavior. Keep sensitive information like API keys in `.env`.
## 
Next Steps
  * [Installing CrewAI](https://docs.crewai.com/<#installing-crewai>)
  * [Creating a New Project](https://docs.crewai.com/<#creating-a-new-project>)
  * [Next Steps](https://docs.crewai.com/<#next-steps>)