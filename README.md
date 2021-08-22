# Syllabus for BIOS 823 (2021)

BIOS 823 is designed for people who want to work in a data science team, especially in a healthcare setting. Hence the course focuses on the skills and knowledge needed to contribute to the main roles in a data science team:

- Making data available and accessible for analysis
- Processing data and performing exploratory data analysis
- Statistical inference and machine learning
- Scaling up to big data and deploying automated workflows

You will learn how to use the essential tools for each of these roles effectively. The emphasis is on conceptual understanding, and we will highlight only selected software packages that exemplify each role. Once you understand the concepts, it should be simple to self-learn other similar packages, and you have the opportunity to do so in projects. Applications of data science to the analysis of structured, semi-structured and unstructured data, especially from biomedical contexts, will be interleaved into the course. 

**Prerequisites**

- You have a background in linear algebra
- You have a background in basic statistical inference
- You have a background in basic machine learning
- You are fluent in Python
- You are familiar with the use of `git` for version control
- You enjoy coding and playing with data

Course repository is at https://github.com/cliburn/bios-823-2021

Due to the wide-ranging nature of the syllabus, there is no course textbook. However, recommendations for useful books for each major topic will be suggested for those who want to explore the topic in more depth.

## Objectives for students

- Develop competency in data manipulation and analysis
    - Exam
- Demonstrate mastery of individual skills / packages
    - Homework / blogs
- Integration of separate skills / working in teams
    - Final project
- Communication skills / visual storytelling
    - Written - blogs
    - Oral - presentations, class participation
- Build a (biomedical) data science portfolio
    - GitHub repositories
    - Personal landing page
    - Blogs

## Grading

- 50% mini-project homework
  - A lot of practical self-learning will be done *only* through homework assignments, including exposure to topics and/or alternative packages we have no time to cover in class. The homework assignments (and final project) will also result in the creation of your data science portfolio.
  - Due every two weeks
- 10% coding practice homework
  - Short, more structured exercises to master basic skills
  - Due every week
- 20% exams
  - Test basic competency
  - Based on topics covered in lectures
- 20% final project
  - Opportunity to integrate what's been learned over the course
  - Learn to work as part of a data science team

For letter grade

- A: 90 - 100
- B: 75 - 89
- C: 60 - 74
- F: 59 and below

## Office hours

- Michael Gao <michael.gao@duke.edu> (TA): ?
- Cliburn Chan <cliburn.chan@duke.edu> (Instructor): Thursdays 5-6 pm
  - Please email me in advance if you plan to attend my office hour

## Part 1: Python for Data Science

The basic foundation of data science is the creation of tidy data formats that can then be visualized using a grammar of graphics. We will review data processing and exploratory data visualization, common formats for data sharing, and application programming interfaces (API) for transfer of semi-structured data resources.

### Jupyter and Python

- Jupyter
  - Literate programming
  - Magic functions
  - Polyglot programming
  - Jupyter notebooks and version control
- Programming exercises

### Working with text

- String methods
- String formatting
- Using `re`

### Numerics

- Using `numpy`

### Data manipulation

- Using `pandas`

### Data visualization

- Using `seaborn`

### Portable data formats

- JSON with `jsoon`
- XML with `elementtree`
- HDF with `h5py`
- Other formats `pydata`, `parquet`
- Working with REST APIs

## Part 2: Working with databases

### SQL databases with `sqlite3`

Most data in healthcare settings still reside in relational database's, especially in enterprise data warehouses that have been created to serve as portals to electronic health records. Hence, an essential skill for a data scientist is the use of SQL, especially for constructing data queries. We will also examine examples of a few NoSQL databases, and review their comparative advantages and disadvantages relative to relational databases.

- Relational databases are based on set theory
- Tables, rows, columns, keys, relations, constraints
- Database schema and normalization
- CRUD
- SQL queries
    - Single table queries
    - Window function
    - Joins
    - User defined functions
    - Common table expressions

### NoSQL databases

This is mostly for exposure and we will not go into any depth.

- Key-value with `redis`
    - Uses
    - Collections
- Document with `mongodb`
    - Uses
    - Queries
- Graph with `neo4j`
    - Graph concepts with `networkx`
    - Uses
    - The Cypher language

## Part 3: Machine Learning

Machine learning is an essential skill for any data scientist, so we will review practical issues in classical and deep learning, including feature engineering, imbalanced data, hyper-parameter tuning, and model expandability.

### Classical ML

Main package is`scikit-learn`. Supplementary package is `yellowbrick` for visualization.

- Unsupervised learning
    - Dimension reduction
    - Clustering
    - Recommender systems
- Supervised learning
    - Basic framework for training and evaluation
    - Model families
    - Preprocessing and feature engineering
    - Hyperparameter tuning with `optuna`
    - Model evaluation
    - Explaining models

### Deep learning

Main package is `tensorflow` with `keras`

- Neural network concepts
- Working with data sets
- Effective training 
- Explainable AI (XAI) with `shap`

## Part 3: Working with big data

Finally, we consider three aspects of data engineering for "big data" - construction of pipelines using functional approaches, scaling of algorithms for performance, and the automation of workflows.

### Functional programming

Main packages are `itertools`, `functional`, `toolz`

- Recursion
- Lazy evaluation and iterators
- Comprehensions and generators
- Anonymous functions
- Partial application and currying
- Higher order functions: map, filter, reduce, decorators
- Pipes and chaining operations
- A digression: `coconut`

### Distributed computing

Main package: `spark`

- Concurrent, parallel, distributed
- Simple multi-core processing
- Spark concepts
- Spark SQL
- Spark ML
- Spark Streaming
- GraphFrames

### Workflow management

- Literate programming with `Jupyter` and `nbconvert`
- Source code version control with `git`
- Testing code with `py.test`
- Continuous integration with `githu actions`
- Using containers with `Docker`
- Automating complex workflows
- Creating APIs for analysis with `fastapi`
- Life in the cloud