# What should I include in a commit?
Try to focus on a single thing. It's okay if it takes a lot of lines of code, or if it modifies multiple files. 

>[!question] What if I haven't finished that feature?
>That's the point, you should update as you go, trying to keep control of your code's versions and keeping the commits clean and concise

**Do**

-   do keep the message short (less than 60-ish characters)
-   do explain _what_ the commit does (not _how_ or _why_!)

>[!Rule] Rule of thumb
>If you have to write "and" in a commit, you are probably making too many changes

If you _really_ need to explain **why** you made a commit, do `git commit` , open VSCode and write at the top:
> commit message
> %%(blank line)%%
> Explanation


