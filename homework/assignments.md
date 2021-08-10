# Homework Projects

You are expected to follow the Duke Honor Code. You can discuss ideas and approaches with your classmates, but you should write and debug your code from scratch. You are not to directly copy code or text from each other, books or the web. Cite any resources you used to complete each assignment.

- There are 5 rather open-ended exercises where you can learn to use new tools and show off your creativity and design flair in addition to programming skills
- Each project is worth 10 points with the following distribution
  - Solution and code quality in notebook - 7 points
  - Educational/entertainment value of Blog - 2 points
  - GitHub commits and log messages - 1 points
- The TA is allowed to give up to 2 extra points for effort above and beyond - so you can get up to 12 points for outstanding work
- Any points above 50 will be used as extra credit
- Assignments are due on Friday 11:59 PM every 2 weeks for the first 10 weeks of the course in the order given
- Late assignments will be penalized by 50\% if submitted within 1 week of deadline, and receive 0 beyond that.
- Every assignment must have code committed, with meaningful log messages, to GitHub
- Every assignment must have an accompanying blog post where you teach others how you accomplished the task.
- Your blog should be viewable by your classmates - post your URL on Sakai for others to see
  
## Assignments

Start a personal website on [GitHub Pages](https://pages.github.com). You can find tutorials for how to do on the web. You will need to blog about each exercise for full credit. The use of a blogging tool like Pelican or Hugo is optional.


**1**. Math is fun

Solve 3 problems from the [Euler Project](https://projecteuler.net/archives) using Python. Of the 3 problems, one must have been solved by fewer than 25,000 people, 1 fewer than 100,000 people and one fewer than 500,000 people. If you want to challenge yourself, choose all 3 problems from the category solved by fewer than 25,000 people. Write a function for each problem, and use [`nuympy`-styple docstrings](https://numpydoc.readthedocs.io/en/latest/format.html) to annotate each function. Write a blog  describing your solutions and how you approached each problem. 

**2**. Number theory and a Google recruitment puzzle

Find the first 10-digit prime in the decimal expansion of 17π. 

The first 5 digits in the decimal expansion of π are 14159. The first 4-digit prime in the decimal expansion of π are 4159. You are asked to find the first 10-digit prime in the decimal expansion of 17π. First solve sub-problems (divide and conquer):

- Write a function to generate an arbitrary large expansion of a mathematical expression like π. Hint: You can use the standard library `decimal` or the 3rd party library `sympy` to do this
- Write a function to check if a number is prime. Hint: See Sieve of Eratosthenes
- Write a function to generate sliding windows of a specified width from a long iterable (e.g. a string representation of a number)

Write unit tests for each of these three functions. You are encouraged, but not required, to try [test-driven development](https://en.wikipedia.org/wiki/Test-driven_development).

Now use these helper functions to write the function that you need.
Write a unit test for this final function, given that the first 10-digit prime in the expansion e is 7427466391. Finally, solve the given problem.

**3**. Creating effective visualizations using [best practices](https://rafalab.github.io/dsbook/data-visualization-principles.html)

Create 3 informative visualizations about malaria using Python in a Jupyter notebook, starting with the data sets at https://github.com/rfordatascience/tidytuesday/tree/master/data/2018/2018-11-13. Where appropriate, make the visualizations [interactive](https://jupyterbook.org/interactive/interactive.html).

**Note** There are many libraries you can use for each task. Choose one library and explain why you chose it in your blog.

**4**. Is there life after graduate school?

Download data of [Science and Engineering PhDs awarded in the US](https://ncses.nsf.gov/pubs/nsf19301/data). Do some analysis in `pandas`. Make a [dashboard visualization](https://pyviz.org/dashboarding/) of a few interesting aspects of the data.

**5**. Dive into Deep Learning

Train a deep learning model to classify beetles, cockroaches and dragonflies using these [images](https://www.dropbox.com/s/fn73sj2e6c9rhf6/insects.zip?dl=0). Note: Original images from https://www.insectimages.org/index.cfm. Blog about this, and *explain* how the neural network classified the images using [SHapley Additive exPlanations](https://github.com/slundberg/shap).
