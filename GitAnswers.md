1. What is the difference between git and GitLab?
Git is a distributed version control system (VCS) that allows developers to track changes in code, collaborate, and manage different versions of their projects. Git is primarily a command-line tool and operates locally on your computer.
GitLab is a web-based Git repository manager that provides a platform for hosting and managing Git repositories, GitLab allows teams to collaborate on code stored in Git repositories.
2. What is the difference between GitLab, GitHub, and BitBucket?
GitHub: A widely-used platform for hosting Git repositories. It is primarily used for open-source projects and has a strong community. GitHub provides features like issue tracking, pull requests.
GitLab: A Git repository management platform with similar features to GitHub but with a strong focus on DevOps. GitLab also offers self-hosting, meaning you can run your own GitLab server.
BitBucket: Another Git repository management service, primarily used by enterprises.
3. Why would I ever want to use git, but not GitLab?
You may want to use Git without GitLab if you need to work locally on a project and don't require centralized hosting.
4. What are the steps to update the GitLab server with some changes I made on my computer?
Git add . to stage changes, git commit to commit them, push to push changes.
5. What is a branch and why would I use one?
A branch is a separate line of development in a Git repository. It allows you to work on a feature, bug fix, or experiment without affecting the main codebase. Once your work is complete, you can merge the branch back into the main branch.
It helps in isolating work, allows parallel development, and keeps the main branch clean and stable while you experiment or develop new features.
6. How could you visualize a branch with 3 commits, and then another branch that breaks off after the second commit and has a single commit?
7. Give an example of a set of git commands that would result in a merge conflict.
Two users pull from main branch change something on the same spot, the first one to push is abel to bot the second one can not.
9. Is Git suitable for latex documents?
Yes, Git is highly suitable for versioning LaTeX documents. LaTeX files are typically text-based, which makes them easy to track with Git. You can use Git to manage revisions of your LaTeX source code and collaborate with others.
9. Should I from now on version my word and powerpoint slides using git? Why/why not?
While Git can version control Word and PowerPoint files, it's generally not the best choice. These files are binary files, not text-based, which means Git can't show diffs or track changes as easily.
10. What could happen when I push my latest commit to the remote repository without pulling first?
If you push without pulling first, If someone else has pushed changes to the remote repository, your push may be rejected because your local branch is out of date. You may encounter a non-fast-forward error or merge conflicts when trying to push. You would need to pull the changes from the remote, merge them, and then push again.
11. What happens when I pull without commiting my local changes first?
If you try to pull without committing your local changes, Git will either:
Stash your changes automatically (if configured) to temporarily save your work, pull the changes, and then apply your stashed changes. Or reject the pull if your local changes conflict with the incoming changes, and you would need to commit or stash your changes before pulling.
12. What is the difference between branching and forking?
Branching: Branching is creating a new line of development within the same repository. It allows you to work on features, bug fixes, or experiments while keeping the main branch stable.
Forking: Forking is creating a personal copy of someone else's repository on a platform like GitHub or GitLab. You can make changes on your fork without affecting the original repository. Forking is commonly used in open-source projects where contributors don't have direct write access to the main repository.