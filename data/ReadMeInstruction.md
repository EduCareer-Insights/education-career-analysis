# Team Workflow Guide

Below is a single, continuous set of steps that covers how to work with existing branches, create new branches if needed, make changes, and merge updates back into `main`. Please read carefully and follow each step to avoid merge conflicts or confusion.

1. **Install Git and Have a GitHub Account**  
   - Make sure Git is installed on your machine: https://git-scm.com/downloads  
   - Have a GitHub account with collaborator access to this repository.

---
2. **Clone the Repository**  
   - On this repository’s GitHub page, click the green “Code” button. Copy the HTTPS (or SSH) URL.  
   - In your terminal, run:
     ```bash
     git clone https://github.com/EduCareer-Insights/Your_Repo_Name.git
     cd Your_Repo_Name
     ```
   - You now have a local copy of the codebase.

---
3. **Sync Local Main Before Starting Any Work**  
   - Always ensure your local `main` branch is up to date:
     ```bash
     git checkout main
     git pull origin main
     ```

---
4. **Check for Existing Branches or Create a New One**  
   - **If a relevant branch already exists** (e.g., `rosendo/data-resources`, `braxton/data-types`), switch to it:
     ```bash
     git checkout rosendo/data-resources
     git pull origin rosendo/data-resources
     ```
   - **If you need a new branch** for your task, create and switch to it:
     ```bash
     git checkout -b feature-data-wrangling
     ```
   - Use descriptive names (e.g., `bugfix/null-handling`, `docs/readme-update`).

---
5. **Make Your Changes**  
   - Edit or add the code, notebooks, or docs you’re responsible for.  
   - If your work depends on a CSV file, confirm it’s located in the correct folder (e.g., `data/education_career_success.csv`).  
   - If you have tests (even manual checks in notebooks), run them to ensure everything is working.

---
6. **Stage and Commit Locally**  
   - Stage all changes:
     ```bash
     git add .
     ```
     (Or stage individual files as needed.)  
   - Commit with a clear message:
     ```bash
     git commit -m "Implement data wrangling function"
     ```

---
7. **Push Your Branch and Open/Update a Pull Request**  
   - Push your branch to GitHub:
     ```bash
     git push origin <branch-name>
     ```
     (Replace `<branch-name>` with the actual name, e.g., `rosendo/data-resources`.)  
   - If a Pull Request (PR) already exists for this branch, your new commits will appear automatically.  
   - Otherwise, on GitHub, click **Compare & pull request** to open a new PR. Provide a concise summary, tag reviewers if needed.

---
8. **Code Review and Feedback**  
   - Teammates or reviewers may comment on your PR with suggestions or changes.  
   - If you need to fix anything, make additional commits on the same branch and push again. The PR updates automatically.

---
9. **Merge into Main**  
   - Once approved, merge the PR on GitHub (e.g., “Merge pull request” or “Squash and merge”).  
   - After merging, **sync your local `main`**:
     ```bash
     git checkout main
     git pull origin main
     ```

---
10. **Cleanup / Branch Maintenance**  
   - If a branch is no longer needed, you can delete it on GitHub and locally:
     ```bash
     git branch -d <branch-name>
     git push origin --delete <branch-name>
     ```
   - This keeps the repository tidy.

---
11. **Tips & Best Practices**  
   - **Pull Before You Push**: Always `git pull origin main` on the main branch before creating or switching to a feature branch.  
   - **Small, Frequent Commits**: Makes it easier to track changes and revert if needed.  
   - **Descriptive Commit Messages**: Helps teammates (and your future self) understand the history.  
   - **Avoid Committing Large Files**: If the dataset is huge, consider Git LFS or separate hosting.  
   - **Communicate**: If you’re making major changes, let the team know early.

---
12. **Using `check_file_exists` (Optional)**  
   - If your code calls:
     ```python
     original_df = w.check_file_exists('data/education_career_success.csv')
     ```
     Ensure the CSV file is in `data/`. If not found, the script/notebook warns you.  
   - This is optional, but helps confirm data is present locally.

---
13. **Next Steps**  
   - **Team Coordination**: Use GitHub Issues or chat tools to discuss tasks.  
   - **Versioning**: Tag or release stable milestones (e.g., `v1.0`).  
   - **Documentation**: Update this guide, the README, or other docs as processes evolve.

---

**That’s the entire workflow!** By following these steps in one continuous sequence, each team member can safely make changes, open/close pull requests, and merge to `main` without clashing with anyone else’s work.