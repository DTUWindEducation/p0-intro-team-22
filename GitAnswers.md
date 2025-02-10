Q1. What vis the difference between git and GitLab?
A1. Git is a version control system that maintains versions of files locally. GitLab, on the other hand, is an online platform that uses Git repositories to provide cloud-based hosting, allowing teams to collaborate, manage projects, and work remotely on files.
Q2. What is the difference between GitLab, GitHub, and BitBucket?
A2. GitHub: A widely-used platform for hosting Git repositories. It is primarily used for open-source projects and has a strong community. GitHub provides features like issue tracking, pull requests.
GitLab: A Git repository management platform with similar features to GitHub but with a strong focus on DevOps. GitLab also offers self-hosting, meaning you can run your own GitLab server.
BitBucket: Another Git repository management service, primarily used by enterprises.
Q3. Why would I ever want to use git, but not GitLab?
A3. In a situation where I just want to have version control over a file stored locally, without having any necessity for cloud storage and other collaborators I can prefer using Git alone, excluding the usage of GitLab.
Q4. What are the steps to update the GitLab server with some changes I made on my computer?
A4. After making changes on the file locally, the first step is to add the file using "git add" command. Then we commit the changes made using "git commit", which updates the version and the file locally. Then using "git push" command we can push the changes made locally to the online GitLab database.
Q5. What is a branch and why would I use one?
A5. A branch is a subfolder from the main repo, where you can make changes that do not affect the main branch
Q6. How could you visualize a branch with 3 commits, and then another branch that breaks off after the second commit and has a single commit?
A6.     - ---(A)---(B)---(C)---
                   |
                   --(D)---
Q7. Give an example of a set of git commands that would result in a merge conflict.
A7. A merge conflict will happen if you edit a file in the main branch and another person edits the same file and tries to merge it
Q8. Is Git suitable for latex documents?
A8.Yes, Git is highly suitable for versioning LaTeX documents. LaTeX files are typically text-based, which makes them easy to track with Git. You can use Git to manage revisions of your LaTeX source code and collaborate with others.
Q9. Should I from now on version my word and powerpoint slides using git? Why/why not?
A9. While Git can version control Word and PowerPoint files, it's generally not the best choice. These files are binary files, not text-based, which means Git can't show diffs or track changes as easily.
Q10. What could happen when I push my latest commit to the remote repository without pulling first?
A10. Two things could happen. If no one else pushed anything to the repository the push will be succeed. If someone else pushed commits to the main repo, the push will be rejected.
Q11. What happens when I pull without commiting my local changes first?
A11. It depends. It could cause merge conflicts, but if not git will merge them automatically (fast forward merge). You can also stash local changes (hide them from git). 
Q12. What is the difference between branching and forking?
A12. If you create a fork you create a complete new repository based on the original repository. Within a fork you can create branches as well. If you just create a branch you're just on a different line within the original/same repository.
