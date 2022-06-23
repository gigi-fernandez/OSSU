# Creating a repository
>`git init`

Creates a repository inside the WD

# Copying/cloning
>`git clone <URL> <new-name?>`

Clones an already existing repository from an URL into your WD with an optional argument to rename the repo folder.
>[!important] Be careful!
**It doesn't change your WD to the new folder!** Use `cd <folder-name>` to get to `<master>`

# Checking repo Status
>`git status`

Returns the status of the repo (any pending commits, etc).

# Checking commits
> `git log` <`flags`>

Prints out all commits, specifying date, author and comments.
Navigating the log will be a bit different (no scrollweel):
-   to scroll **down**, press
    -   **`j` or `↓` to move _down_ one line at a time**
    -   `d` to move by half the page screen, `f`  for a whole page screen
-   to scroll **up**, press
    -   **`k` or `↑` to move _up_ one line at a time**
    -   `u` to move by half the page screen, `b`  for a whole page screen
-   press `q` to **quit** out of the log (returns to the regular command prompt)

### Flags
>`--oneline`

Summarizes all commits to just the first digits of the SHA and their comment.

>`--stat`

Specifies which and how many files were modified in the commit and how many insertions/deletions were made.

>`--patch`  OR `-p`

Specifies the actual changes in the files. Removed lines in red, added lines in green.
![[gitlogp.png]]
-   🔵 - the file that is being displayed
-   🔶 - the hash of the first version of the file and the hash of the second version of the file
    -   not usually important, so it's safe to ignore
-   ❤️ - the old version and current version of the file
-   🔍 - the lines where the file is added and how many lines there are
    -   `-15,83` indicates that the old version (represented by the `-`) started at line 15 and that the file had 83 lines
    -   `+15,85` indicates that the current version (represented by the `+`) starts at line 15 and that there are now 85 lines...these 85 lines are shown in the patch below
-   ✏️ - the actual changes made in the commit
    -   lines that are red and start with a minus (`-`) were in the original version of the file but have been removed by the commit
    -   lines that are green and start with a plus (`+`) are new lines that have been added in the commit

adding a `-w` flag will ignore whitespace changes (changing empty lines, characters, etc)

>`git log ... <`SHA`>`

You can use the SHA of the commit you are looking for as the final argument to just get the relevant data.

>`git show ... <`SHA`>`

Prints out the last commit. Same deal as `git log <`SHA`>` if SHA is provided. Also uses all of the previously defined flags.

# Preparing commits
![[git-staging.gif]]
We use `git add <`filename`>` to move the file from the WD into the Index. You can add multiple files by adding a whitespace between filenames. We call this **_staging_**. 

There are multiple ways to add all files in the WD, each of them slightly different:
Command|New|Modified|Deleted
---|---|---|---
`git add .`| [y]|[y]|[n]|
`git add -A`| [y]|[y]|[y]|
`git add -u`| [n]|[y]|[y]|

>[!TIP]
>Run `git status` afterwards to make sure everything's right

If we accidentally stage something we didn't intend to, we can run `git rm --cached <`filename`>` to unstage.

>[!Tip] VSCode Source Control
>You can do most of what git does using VSCode:
>
>![[VSCode source control.png]]

If you want Git to ignore certain files, you can do so in two ways:
1. Running `git add *` instead of `git add .` will ignore all files starting with `.`
2. Including said files in the `.gitignore` file.

For multiple files sharing a characteristic you can use **globbing**:
-   blank lines can be used for spacing
-   `#` - marks line as a comment
-   `*` - matches 0 or more characters
-   `?` - matches 1 character
-   `[abc]` - matches a, b, _or_ c
-   `**` - matches nested directories - `a/**/z` matches
    -   a/z
    -   a/b/z
    -   a/b/c/z
If you, said, wanted to ignore all `.png` files from a folder, you would write into `.gitignore`:
>\*.png

# Commits
>`git commit`

Running this on its own will open your text editor of choice and show you the files about to be added/modified/deleted. Write the comment for the commit on the first line, save and close the editor for it to actually commit.

Alternatively, and more conveniently, you can run this instead to skip the editor:
>`git commit -m "<`enter comment here`>"`


# Check for changes
>`git diff`

Checks for both staged and unstaged changes

# Tagging commits
`git tag (-a) <`identifier-of-tag`>`

This creates a tag that you can latch on to commits. This is helpful for keeping track of certain things.

>The `(-a)` argument indicates that the flag is optional, and used to specify that the tag will be anotated, which gives more info on who made the tag, when and a message.

You can also run `git tag` without any arguments or flags to check your repo's tags. `git log` will also show which commits have which tags.

Deleting tags is as simple as running `git tag -d <`identifier-of-tag`>`, `-d` being short for `--delete`.

# Branching
>`git branch` <`name-of-branch`> <`SHA`>

- **No arguments:** Will print out the different branches of the repo. 
- **Adding `<`name-of-branch`>`:** Will create said branch from the last commit. 
	- **Adding <`SHA`>:** Will create a branch from the specified commit.
	- Alternatively, add the name of a branch instead of <`SHA`> to branch from there.

### Switching active branch
`git checkout <`name-of-branch`>` will switch the active branch to the specified name.
This works by removing everything in the WD, but adding all of the files referenced by said branch. Nothing is lost, all of the removed files are stored in the previous branch.
>To switch and create a new branch at the same time, run:
>	`git checkout -b <`name-of-branch`>`

### Deleting a branch
If you wanted to completely remove a branch from the repo, do just like with tags and add `-d` before <`name-of-branch`>. 
>`git branch -d <`name-of-branch`>`

If it has commits found nowhere else, it won't let you delete it unless you do `-D` instead of `-d`.

# Merging
To merge `branch-B` into `branch-A`, make sure to set `branch-A` as your active branch and then run
>`git merge branch-B`

This will apply the changes made to `branch-B` into `branch-A`.

If only new things were added on top of `branch-A`, it's called a _fast-forward merge_. Otherwise, it's called a _regular merge_. 

### Merge conflicts
Whenever you modify the same thing in multiple branches and try to merge them, there will be some changes that need manual approval for merging. This causes a _**merge conflict**_.

Git will modify files causing a merge conflict signaling which lines are causing the issue. You must pick a version, commit the changes and then merge.

# Fixing mistakes
### Mistakes in last commit
You can revert them with the flag `--amend`.
>`git commit --amend`

Simple as that!

### Reverting changes in a specific commit
> `git revert <`SHA`>`

This reverts the changes of the specified commit. It works by **creating a new commit that reverses all the changes.**

### Reseting/Deleting commits
>`git reset <`reference-to-commit`>`

This removes commits from the repo and can send them to one of three places, depending on the flag (goes before the reference):
- No flag/`--mixed`: Sends the commit to the WD.
- `--soft`: Sends the commit to the staging area
- `--hard`: Sends the commit to the trash (deletes it in 30 days)

<`reference-to-commit`> works differently from SHA references.
-   `^`  indicates the parent commit
-   `~`  indicates the _first_ parent commit. 
>The main difference between the `^` and the `~` is when a commit is created _from a merge_. A merge commit has _two_ parents. With a merge commit, the `^` reference is used to indicate the _first_ parent of the commit while `^2` indicates the _second_ parent. The first parent is the branch you were on when you ran `git merge` while the second parent is the branch that was merged in.

>[!warning]
This is a bit risky and can have harmful side-effects. **Use with caution!** You can actually use `git branch backup` to create a backup just in case and then run `git merge backup`.


