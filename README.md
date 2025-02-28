# Education Career Analysis

## GitHub Workflow Guide

This guide explains how to contribute to our project using GitHub.

### 1. Setting Up Your Project Folder

Before cloning the repository, create a folder where you want to store the project:
1. Mac Users: Open Terminal
2. Windows Users: Open PowerShell
3. Navigate to the location where you want to store the project:           
    `cd path/to/your/folder  # Replace with your actual path`      
4. If you haven’t created a folder yet, do so:       
    `mkdir education-career-analysis`        
    `cd education-career-analysis`       

### 2. Cloning the Repository

To download the project from GitHub:         
`git clone https://github.com/EduCareer-Insights/education-career-analysis.git`        
`cd education-career-analysis`

Then, set up the main branch:         
`git checkout main`
`git pull origin main`

### 3. Creating a New Branch

Each member has their own assigned branch. Use the correct branch name when switching or cloning.

#### Branch Naming Format:       
`member/task`

#### Branch Assignments:

- rosendo/data-resources → Data Resources
- becca/hypothesis → Hypothesis & Goals
- spencer/descriptive-statistical-analysis → Descriptive & Statistical Analysis
- gianna/missing-values-cleaning → Missing Values & Data Cleaning
- braxton/data-types → Data Types

To switch to your branch after cloning:       
`git checkout rosendo/data-resources  # Replace with your branch name`

### 4. Making Changes & Committing

After editing files, stage the changes:       
`git add .`

Then, commit the changes with a descriptive message:       
`git commit -m "Updated dataset description"`

### 5. Pushing Your Changes to GitHub

After committing, push your branch to GitHub:         
`git push origin rosendo/data-resources  # Replace with your branch name`

### 6. Creating a Pull Request (PR)

- Go to the GitHub repository in your browser.
- Click on the Pull Requests tab.
- Click New Pull Request and select your branch.
- Add a title and description of your changes.
- Click Create Pull Request.

### 7. Reviewing & Merging a Pull Request

Other team members review your PR and suggest changes if needed.
Once approved, merge it by clicking Merge Pull Request.
After merging, delete your branch to keep things clean:       
`git branch -d rosendo/data-resources  # Replace with your branch name`

### 8. Keeping Your Branch Up-to-Date

Before working on new changes, always sync with the latest main:      
`git checkout main`
`git pull origin main`

If your branch is outdated, rebase it:       
`git checkout rosendo/data-resources  # Replace with your branch name`
`git rebase main`
         
---      
         
💡 Best Practices

✅ Use meaningful commit messages (e.g., "Fixed missing values in dataset")        
✅ Always pull the latest changes before starting new work      
✅ Get at least one review before merging a PR      
✅ Do not push directly to main—always use a pull request      