1. What is the difference between git and Gitlab?
Git is a version control software locally on the computer. Gitlab is an online server that expands the git functions (saves code online, allows collaboration, codechecking etc) 
2.	What is the difference between GitLab, GitHub, and BitBucket?
Gitlab, Github and BitBucket are all version control platforms. While Github (Microsoft) has a big open source community and collaboration, Bitbucket is more restricitve for free use and is developed by Atlassian (good integration with Jira). Gitlab is verz similar to Github (Gitlab Inc.) with a slightly different interface and different sercvers an the community edition is fully open source.
3.	Why would I ever want to use git, but not GitLab? 
In case you only want to manage your projects locally or use git with Github or Bitbucket.
4. What are the steps to update the GitLab server with some changes I made on my computer? 
The first step is to stage your changes: git add . (or specify files). Then you need to commit these change git commit -m "Message". Afterwards you need to push the commit to the sever: git push origin branch-name.
5. What is a branch and why would I use one?  
A branch is a seperate line (next to the main branch) where I can develop new features which don't affect the main branch. This allows for multiple people to develop seperate features at the same time. 
6. see picture
7. Give an example of a set of git commands that would result in a merge conflict. 
A merge conflict arrises if the same file is eddited within the main branch and any other branch.
git add conflict.txt
git commit -m "Initial commit with conflict.txt"
# Create new branch and modify conflict.txt
git checkout -b feature-branch
echo "This is a change from feature-branch" > conflict.txt
git commit -am "Modify conflict.txt in feature-branch"
# go bacl to main and modify the file
git checkout main
echo "This is a change from main" > conflict.txt
git commit -am "Modify conflict.txt in main"
# Merge the changes
git merge feature-branch
8. Is Git suitable for latex documents? 
Yes it is. Since it tracks changes within files. 
9. Should I from now on version my word and powerpoint slides using git? Why/why not? 
No, because Word and PowerPoint files are binary and not text based. Also they can be quite large, which makes it harder to control them in git. 
10. What could happen when I push my latest commit to the remote repository without pulling first?
Two things could happen. If no one else pushed anything to the repository the push will be succeed. If someone else pushed commits to the main repo, the push will be rejected.
11. What happens when I pull without commiting my local changes first? 
It depends. It could cause merge conflicts, but if not git will merge them automatically (fast forward merge). You can also stash local changes (hide them from git).
12.	What is the difference between branching and forking?
If you create a fork you create a complete new repo based on the original repo. Within a fork zou can create branches as well. If you just create a branch you're just on a different line within the og repo.