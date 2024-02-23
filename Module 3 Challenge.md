---
created: 2024-02-23T12:14:58 (UTC -07:00)
tags: []
source: https://bootcampspot.instructure.com/courses/5432/assignments/73209?module_item_id=1200217
author: 
---

# Module 3 Challenge

> ## Excerpt
> You'll be creating a customer banking system that allows users to calculate and track interest earned on savings and CD accounts. By running this application, users will be able to enter their savings and CD account information, see the interest earned, and view the updated balances after a specified number of months.

---
-   Due Mar 11 by 11:59pm
-   Points 100
-   Submitting a text entry box or a website url

### Background

You'll be creating a customer banking system that allows users to calculate and track interest earned on savings and CD accounts. By running this application, users will be able to enter their savings and CD account information, see the interest earned, and view the updated balances after a specified number of months.

### Files

Download the following files to help you get started:

[Module 3 Challenge files Links to an external site.](https://static.bc-edx.com/ai/ail-v-1-0/m3/lms/starter/M3_Starter_Code.zip)

### Before You Begin

Before starting the assignment, be sure to complete the following steps:

-   Create a new repository for this project called `customer_banking`. **Do not add this homework assignment to an existing repository**.
    
-   Clone the new repository to your computer.
    
-   Inside your local Git repository, add the starter files from your file downloads.
    
-   Push these changes to GitHub or GitLab.
    

### Challenge Instructions

The starter files consist of the following files: `Accounts.py`, `savings_account.py`, `cd_account.py`, and `customer_banking.py`. The `Accounts.py` file contains the `Account` class with methods to set the balance and interest.

In the `savings_account.py` file, you will import the `Account` class and create a `create_savings_account` function that will create a savings account instance, calculate the interest earned based on user input, update the account balance with the earned interest, and return the updated balance and interest earned.

In the `cd_account.py` file, you will import the `Account` class and create a `create_cd_account` function that will create a CD account instance, calculate the interest earned based on user input, update the account balance with the earned interest, and return the updated balance and interest earned.

In the `customer_banking.py` file, you will import the `create_savings_account` and `create_cd_account` functions, then create a `main` function that prompts the user to enter the savings and CD account details, call the corresponding functions to calculate the interest earned and update the balances, and display the results.

#### Create the Savings Account Function

Open the `savings_account.py` file, and do the following:

1.  Imports the `Account` class from the `Accounts.py` file.
    
2.  In the `create_savings_account` function do the following:
    
    -   Create an instance of the `Account` class and pass in the balance and interest parameters.
        
    -   Calculate interest earned.
        
        **hint**
        
    -   Update the savings account balance by adding the interest earned.
        
        **hint**
        
    -   Pass the updated balance to the set balance method using the instance of the `Account` class.
        
    -   Pass the interest earned to the set interest method using the instance of the `Account` class.
        
    -   Return the updated balance and interest earned.
        

#### Create the CD Account Function

Open the `cd_account.py` file, and do the following:

1.  Import the `Account` class from the `Accounts.py` file.
    
2.  In the `create_cd_account` function, do the following:
    
    -   Create an instance of the `Account` class and pass in the parameters.
        
    -   Calculate interest earned.
        
    -   Update the savings account balance by adding the interest earned.
        
        **hint**
        
    -   Pass the updated balance to the set balance method using the instance of the `Account` class.
        
    -   Pass the interest earned to the set interest method using the instance of the `Account` class.
        
    -   Return the updated balance and interest earned.
        

#### Create the Main Function

Open the `customer_banking.py` file, and do the following:

1.  Import the `create_cd_account` and `create_savings_account` functions from the appropriate files.
    
2.  In the `main` function, do the following:
    
    -   Prompt the user to set the savings balance, interest rate, and months for the savings account.
        
        **hint**
        
    -   Call the `create_savings_account` function and pass in the variables from the user.
        
    -   Print out the interest earned and updated savings account balance with interest earned for the given months.
        
    -   Prompt the user to set the CD balance, interest rate, and months for the CD account.
        
        **hint**
        
    -   Call the `create_cd_account` function and pass the variables to the function used to prompt the user from the user.
        
    -   Print out the interest earned and updated CD account balance with interest earned for the given months.
        
    -   Call the main function.
        

### Hints and Considerations

-   Consider what you've learned so far. You’ve learned how to create and import functions, pass arguments and variables into functions, refactor code, create and import class, create class methods, and instances.
    
-   If you're struggling with how to start, consider creating one Python file that has all the functions first, then separate the functions into different files. Also, look back on some of the activities you did in class. Finally, you can use pseudocoding to help you write out the steps.
    
-   Always commit your work and back it up with pushes to GitHub or GitLab. You don't want to lose hours of your hard work! Also make sure that your repo has a detailed `README.md` file.
    

### Requirements

#### Create the Savings Account Function (35 points)

-   The `Account` class from the `Accounts.py` file is imported. (4 points)
    
-   In the `create_savings_account` function, an instance of the `Account` class is created and the balance and interest parameters are passed to the `Account` class. (6 points)
    
-   The interest earned is calculated and assigned to a variable. (4 points)
    
-   The savings account balance is updated by adding the interest earned to the balance and assigned to a variable. (4 points)
    
-   The updated balance is passed to the set balance method using the instance of the `Account` class. (6 points)
    
-   The interest earned is passed to the set balance method using the instance of the `Account` class. (6 points)
    
-   The updated balance and interest earned are returned by the function. (5 points)
    

#### Create the CD Account Function (35 points)

-   The `Account` class from the `Accounts.py` file is imported. (4 points)
    
-   In the `create_cd_account` function, an instance of the `Account` class is created and the balance and interest parameters are passed to the `Account` class. (6 points)
    
-   The interest earned is calculated and assigned to a variable. (4 points)
    
-   The CD account balance is updated by adding the interest earned to the balance and assigned to a variable. (4 points)
    
-   The updated balance is passed to the set balance method using the instance of the `Account` class. (6 points)
    
-   The interest earned is passed to the set balance method using the instance of the `Account` class. (6 points)
    
-   The updated balance and interest earned are returned by the function. (5 points)
    

#### Create the Main Function (30 points)

-   The user is prompted to set the savings balance, interest rate, and months for the savings account. (8 points)
    
-   Code is written to print out the interest earned and updated savings account balance with interest earned for the given months. The values are formatted to two decimal places and thousandths. (6 points)
    
-   The user is prompted to set the savings balance, interest rate, and months for the CD account. (8 points)
    
-   Code is written to print out the interest earned and updated CD account balance with interest earned for the given months. The values are formatted to two decimal places and thousandths. (6 points)
    
-   The `main` function is called to run the program. (2 points)
    

### Grading

This assignment will be evaluated against the requirements and assigned a grade according to the following table:

| Grade | Points |
| --- | --- |
| A (+/-) | 90+ |
| B (+/-) | 80–89 |
| C (+/-) | 70–79 |
| D (+/-) | 60–69 |
| F (+/-) | < 60 |

### Submission

To submit your Challenge assignment, click Submit, and then provide the URL of your GitHub repository for grading.

**note**

You are allowed to miss up to two Challenge assignments and still earn your certificate. If you complete all Challenge assignments, your lowest two grades will be dropped. If you wish to skip this assignment, click Next, and move on to the next module.

Comments are disabled for graded submissions in Bootcamp Spot. If you have questions about your feedback, please notify your instructional staff or your Student Success Manager. If you would like to resubmit your work for an additional review, you can use the Resubmit Assignment button to upload new links. You may resubmit up to three times for a total of four submissions.

**important**

**It is your responsibility to include a note in the README section of your repo specifying code source and its location within your repo**. This applies if you have worked with a peer on an assignment, used code that you did not author or create sourced from a forum such as Stack Overflow, or you received code outside of curriculum content from support staff such as an Instructor, TA, Tutor, or Learning Assistant. This will provide visibility to grading staff of your circumstance in order to avoid flagging your work as plagiarized.

If you are struggling with a challenge assignment or any aspect of the academic curriculum, please remember that there are student support services available for you:

1.  Ask the class Slack channel/peer support.
    
2.  AskBCS Learning Assistants exists in your class Slack application.
    
3.  Office hours facilitated by your instructional staff before and after each class session.
    
4.  [Tutoring Guidelines Links to an external site.](https://docs.google.com/document/d/1hTldEfWhX21B_Vz9ZentkPeziu4pPfnwiZbwQB27E90/edit?usp=sharing) - schedule a tutor session in the Tutor Sessions section of Bootcampspot - Canvas
    
5.  If the above resources are not applicable and you have a need, please reach out to a member of your instructional team, your Student Success Advisor, or submit a support ticket in the Student Support section of your BCS application.
    

### References

None
