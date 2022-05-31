# MuscleHub AB Test

The data analytics project at MuscleHub - a fancy gym.

Currently, when a MuscleHub visitor purchases a membership, they follow the following steps:

    Take a fitness test with a personal trainer.
    Fill out an application for the gym.
    Send in their payment for their first month’s membership.

There is the chance, that the fitness test intimidates some prospective members, so we set up an A/B test.

Visitors are randomly be assigned to one of two groups:

    Group A is still asked to take a fitness test with a personal trainer.
    Group B skips the fitness test and proceed directly to the application.

Hypothesis is that visitors assigned to Group B will be more likely to eventually purchase a membership to MuscleHub than visitors assigned to Group A. So that the null and alternate hypotheses are as follows:

    Null Hypothesis = There will no difference between the visitors in Group A that purchase membership and the visitors in Group B that purchase membership.
    Alternate Hypothesis = There will be more visitors in Group B that will purchase membership than visitors in Group A that will purchase membership.

The significance threshold we will set as the benchmark to either accept or fail to reject the null hypothesis will be:

    𝛼 = 0.05

We analyze the data and create a presentation with our knowledge of conducting A/B testing with Python.

##

For this project, we have to access SQL by using a special Codecademy library that lets us type SQL queries directly into this Jupyter notebook.  We'll have pass each SQL query as an argument to a function called `sql_query`.  Each query will return a Pandas DataFrame. 

## SQLite database:

- `visits` contains information about potential gym customers who have visited MuscleHub
- `fitness_tests` contains information about potential customers in "Group A", who were given a fitness test
- `applications` contains information about any potential customers (both "Group A" and "Group B") who filled out an application.  Not everyone in `visits` will have filled out an application.
- `purchases` contains information about customers who purchased a membership to MuscleHub.

## Goals of the project:

+ Investigate the A and B groups
+ Find out who picks up an application?
+ Find out who purchases a membership?
+ Summarize the acquisition funel with a chart