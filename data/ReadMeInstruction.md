# Team Workflow Guide

This guide provides a single, continuous set of steps for working on this project together, from installing Git to merging final changes into the `main` branch.

1. **Install Git**  
   - Make sure you have Git installed on your machine.  
   - If you need help, visit https://git-scm.com/downloads.

---
2. **GitHub Account**  
   - Each team member must have a GitHub account.  
   - Ensure you have collaborator access to this repository so you can push and pull changes.

---
3. **Cloning the Repository**  
   - On the repository’s GitHub page, click the green “Code” button and copy the HTTPS or SSH link.  
   - Open your terminal or command prompt, then run:
     ```bash
     git clone https://github.com/EduCareer-Insights/Your_Repo_Name.git
     cd Your_Repo_Name
     ```
   - You now have the codebase on your local machine.

---
4. **Creating a Branch for**  
   - First, make sure your local `main` branch is up to date:
     ```bash
     git checkout main
     git pull origin main
     ```
   - Create a new branch with a descriptive name:
     ```bash
     git checkout -b feature-data-wrangling
     ```
   - This new branch is where you’ll make your changes without affecting `main`.

---
5. **Making Changes**  
   - Edit or add code, notebooks, or documentation files relevant to your task.  
   - If your work depends on a CSV, confirm it’s placed in the correct folder (e.g., `data/`).  
   - If you have tests, run them to ensure everything is working correctly.

---
6. **Committing Your Changes**  
   - Stage the changes:
     ```bash
     git add .
     ```
     (Or list specific files, e.g. `git add my_notebook.ipynb`.)  
   - Commit:
     ```bash
     git commit -m "Implement data wrangling function"
     ```
     Use clear, concise messages describing your changes.

---
7. **Push and Create a Pull Request**  
   - Push your new branch to GitHub:
     ```bash
     git push origin feature-data-wrangling
     ```
   - Go to your repository page on GitHub. You should see a prompt to “Compare & pull request.”  
   - Click it, provide a short description of your changes, add reviewers if needed, and create the PR.

---
8. **Code Review & Approval**  
   - Your teammates can comment or request changes in the Pull Request.  
   - If changes are requested, make them on your local branch, commit, and push again; the PR updates automatically.  
   - Once everyone is satisfied, the PR can be approved.

---
9. **Merging into Main**  
   - After approval, merge your PR via GitHub (e.g. “Merge pull request” or “Squash and merge”).  
   - Sync your local `main` with the latest changes:
     ```bash
     git checkout main
     git pull origin main
     ```
   - Your work is now part of the main codebase.

---
10. **Common Tips & Best Practices**  
   - **Pull Before Push**: Always `git pull origin main` when you switch to `main` to avoid conflicts.  
   - **Small, Frequent Commits**: Easier to track changes and revert if needed.  
   - **Descriptive Branch Names**: e.g., `bugfix-missing-data`, `docs-update-readme`.  
   - **Avoid Committing Large Files**: If the dataset is huge, consider Git LFS or separate hosting.  
   - **Team Communication**: If you’re making major changes, inform the team early.

---
11. **Using `check_file_exists` (Optional)**  
   - If you have a function like:
     ```python
     data_df = check_file_exists('data/education_career_success.csv')
     ```
     Ensure the CSV is in `data/education_career_success.csv` so the script/notebook can find it.  
   - If it’s not present locally, the script will warn you to download or clone properly.

---
12. **Next Steps**  
   - **Team Coordination**: Use GitHub Issues or a team chat for day-to-day updates.  
   - **Versioning**: Tag stable releases (e.g. `v1.0`) if you want to mark major milestones.  
   - **Documentation**: Keep this guide, the README, and any other docs updated with new changes or processes.

---

**That’s it!** By following these sequential steps, everyone on the team can safely make changes, open Pull Requests for review, and merge into `main` without causing conflicts.