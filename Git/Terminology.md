# Commit 
Git thinks of its data like a **set of snapshots of a mini file system**.  
Every time you commit, or save the state of your project in Git, it basically **takes a picture of what all your files look like at that moment and stores a reference to that snapshot.**

# Repository (repo)
A directory that contains your project work, as well as a few files which are used to communicate with Git. Repositories  
can exist either locally on your computer or as a remote copy on another computer.

# Areas of Git
![[Git Areas.png]]

## Working Directory
The files that you see in your computer's file system. When you open your project files up on a code editor, you're working with files in the **Working Directory**.

This is in contrast to the files that have been saved (in **commits**!) in the repository.

When working with Git, the Working Directory is also different from the command line's concept of the current working directory which is the directory that your shell is "looking at" right now.

## Checkout
When content in the repository has been copied to the Working Directory. It is possible to checkout many things from a repository; a file, a commit, a branch, etc.

## Staging Area/Index
A file in the Git directory that stores what will go in the next commit.

# SHA
It's a hash ID of each commit. It looks something like:
>`e2adf8ae3e2e4ed40add75cc44cf9d0a869afeb6`

# Branch
It's essentially a different, parallel line of development of the same project. Think of it as making a save in a game and branching into two playthroughs. They are parallel, but they don't affect each other until they are **merged**.

