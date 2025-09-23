# `git`

A nice, user-friendly introduction to `git` is available [here](https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud).
And the official documentation is [here](https://git-scm.com/doc).

Intro: for those who do not know, `SHA1` is either the ID (long or short, it does not matter) of the commit, which one can get via a `git log`, or a tree-path relative to the `HEAD` (e.g.: latest commit=`HEAD`, second to last=`HEAD^` or `HEAD~1`, ($n+1$)-th to
last=`HEAD~n`).
More info [here](https://git-scm.com/docs/git-cherry-pick).

For inexperienced users who want to perform simple tasks, such as looking at the changelogs and commit history, or creating commits, the user-friendly, GUI programs such as `git-cola` (manage the current status of your git repository) and `gitk` (looking at the commit tree and moving around it) are advisable.

_Bonus._ This could seem totally unrelated, but, here is one the most visited question on `StackOverflow` (more than 2 million times!) which deals with [How to exit the `Vim` editor](https://stackoverflow.com/questions/11828270/how-do-i-exit-the-vim-editor).
You may want to have a look at this question which has more than 8 million views and it is indeed `git`-related: [How do I undo the most recent local commits in `git`?](https://stackoverflow.com/questions/927358/how-do-i-undo-the-most-recent-local-commits-in-git)

* Run `git` commands from another directory: `git -C <path> <cmd>` (mnemonic: as in `make`).
    Originally it was: `--git-dir=<path> --work-dir=<path>`.

* `git add <file_name>`: move the modifications in `file_name` to commit stage (that is, they will be include in the next commit)

    * The option `-p`, aka cherry-picking, splits the `file_name` into chucks, so that you can choose which modifications are to be staged.
        For each of them, you will have to tell `git` what to do with it: if it is to keep, answer `y`; if not, `n`.
        Other answers are possible, for example use `s` (for split) reduce the chunk size / split the current chunk into sub-chunks.
        [Here](https://stackoverflow.com/questions/1122210/can-i-modify-git-adds-hunk-size) you can find the meaning of all of the possible answers.
        This could be done easily with `git-cola`.

    * `git add -A` or `git add .`: stage *all* files, even the new ones (not yet tracked).

    * `git add -u` or `git add --update`: stage *all tracked* files but skip new ones

* `git commit`: creates a new commit with the staged modifications. This operation is easily done in `git-cola`.

    * `-m "Commit title"`: a simple and fast way to create a commit;

    * `-a`: all the modified files, even those which are not staged yet are added to the commit;

    * Forgot a file in your last commit or want to modify it? `git commit --amend` add the staged modifications to the last commit.

    * Commit with the same message as the original (after a reset, or with the `--amend` option): `git commit -c ORIG_HEAD`.

* Writing good commit messages

    * [Conventional commits](https://www.conventionalcommits.org/en/v1.0.0/): a style-guide for writing commits messages.
        The main structure is “`<type>[(scope)][!]: <Short description>`” where:

        * `type` is one of the following: `fix`, `feat`, `chore`, `docs`, `improvement`, `perf`, `refactor`, `test`, `ci`, `build`

        * `scope`, in parentheses, is optional and tells to which part of the repository the modifications are applied

        * `!` is optional and signals that the commit is important, for instance introduces a new cool features, remove the support for a particular case/library...

        * Example: “`feat(api)!: Add access to low-level config`”

        * Why should you write like this?
            It provides a template which is quite easy to understand.
            Moreover, some tools allows one to automatically analyze the commit history and extract insightful information based on this syntax and can provide a changelog.

    * Link a commit to an issues: it suffices to quote the issue number anywhere in the commit message as such `#xxx` where `xxx` is the issue number.
        Moreover, one can directly close an issue with a similar strategy, more details [here](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue): for instance put `close #xxx` in the commit message

* Choosing good branch names:

    * More generally, [here](https://nvie.com/posts/a-successful-git-branching-model/) is an article about a good branching conventions / strategies.

    * It is suggested to prepend categories to branch names, e.g., `features/new_cool_dev`.
      One could choose the category according the same principles of conventional commits described above.
      An interesting [article](https://dev.to/varbsan/a-simplified-convention-for-naming-branches-and-commits-in-git-il4).

    * Sometimes, using category in branch names is recognized by git platforms which can improve the displaying for instance of the PR associated to the branch.

    * In every modern git platform one can open branches directly associated with an issue.

* Tagging: e.g., adding things like `v1.0`, have a look [here](https://git-scm.com/book/en/v2/Git-Basics-Tagging)

    * Add: `git tag -a <tagname> -m"<message>"`

    * Publish: by default, the git push command doesn't transfer tags to remote servers.
        You will have to explicitly push tags to a shared server: `git push origin <tagname>`, or for all tags at once `git push origin --tags`

    * Delete: it should be done in two steps. First, delete locally `git tag -d <tagname>`, then publish `git push origin --delete <tagname>`

* For all merging-related commands (`am`, `merge`, `cherry-pick`, `rebase`, `pull --rebase`...), if errors occur, you can use

    * `git <command> --continue`: the problems have been solved, tells `git` to continue what it was doing,

    * `git <command> --abort`: cancel the operation and return to the pre-sequence state, the situation before `git <command>` was called,

    * `git <command> --quit`: similar to `abort`, but do not reset the `HEAD` back to the original branch.
        The index and working tree are also left unchanged,

    * `git <command> --skip`: in some commands, e.g. the `rebase`-related ones, skip (do not apply) the current commit, and continue.

* `git reset [options] SHA1`, [here](https://git-scm.com/docs/git-reset):

    * `--soft`, Does not touch the index or the working tree at all, but resets the `HEAD` to `SHA1`,

    * `--mixed`, (default) Resets the index but not the working tree (the files do not change),

    * `--hard`, Resets the index *and* the working tree;

* `git rebase -i SHA1`: (`-i` stands for interactive) enables to modify (delete, move up or down the log tree, fix up, squash, reword) the commits from `SHA1` to `HEAD`;

* Modify an old commit (for which `--amend` would not work): use a `rebase -i`

    * For basic modifications: look [here](https://stackoverflow.com/questions/1186535/how-to-modify-a-specified-commit);

    * For splitting a commit or complex modifications: follow [here](https://stackoverflow.com/questions/6217156/break-a-previous-commit-into-multiple-commits) (I suggest to `rebase` to one commit before the one you want to modify).

* (Re)set the remote reference (from where git pulls) for the branch `branch_name`

    ``` bash
    git branch [<branch_name>] --set-upstream-to new_remote/remote_branch
    ```

    If `branch_name` is not provided, the current branch will be used as default;

* Working with remote repositories

    * Getting the latest commits: `git pull`.
        One may want to add the `--rebase` option so that your non yet published commits stay on top of the tree.

    * Publish the latest local commits: `git push`.
        It is always better to do a `git pull --rebase` before pushing in order to avoid conflicts.

* Pushing

    * Push a new branch: `git push -u origin <branch>`: `-u` set the upstream reference at the same time

    * Push a new project to [GitHub](https://github.com/) for the first time: follow [this](https://help.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line).

    * Damn! You have just pushed a commit and you realize just now that it needs an amend.
        Modify it in you local repository then force-push it, have a look [here](https://stackoverflow.com/questions/179123/how-to-modify-existing-unpushed-commit-messages).

    * Push except the last commit: [here](https://stackoverflow.com/questions/8879375/git-push-push-all-commits-except-the-last-one), `git push origin HEAD^:master`

* Rename a branch:

    * If on the branch to rename: `git branch -m <new_name>`

    * If on another branch: `git branch -m <old_name> <new_name>`

* Patching: Patches are objects that stores the differences between two `git` states.

    * There are two kinds of patches:

        * Raw (I don’t know if that’s the official definition, but I think that gives the idea): they are simply the output of `git diff`.

        * Mailbox format: patches of this kind, in addition to the raw difference, also contain information additional information, e.g., the author.
            This type is typically used when sharing patches.

    * Create patches:

        * Raw format: just save the output of `git diff`, for instance with a simple redirection: e.g., `git diff > test.patch`

        * [Mailbox format](https://git-scm.com/docs/git-format-patch): `git format-patch [options] <SHA1>`. Create patches from `SHA1` to most recent commit

            * `-<n>`: create only `n` patches (always starting from `SHA1`);

            * `--start-number <n>`: the patches are numbered starting from `n`;

            * `-N`: commits are unnumbered.

            * `-o <out_dir>`: output directory

    * Apply patches

        * [`git apply`](https://git-scm.com/docs/git-apply): works both on raw and mailbox formats.

        * [`git am [options] path/to/patch`](https://git-scm.com/docs/git-am): apply a mailbox patch.

            * Differently, form the simple `apply`, **it also adds a related commit to the tree**.

            * `-3`: if the patch does not apply cleanly for a certain file, falls back to the version of the most recent common commit between the current tree and the one coming with the patch, and propose a 3-way merge (current, patch, and ancestor),

            * `--reject`: when the application fails, tells `git` to apply as many modifications as possible and to temporarily skip the impossible ones.
                The rejected modification will be stored in `*.rej` files.
                The application has to be completed manually (you will have to personally modify the files)

* Get current branch: `git branch --show-current`

* [Merge](https://git-scm.com/docs/git-merge) a branch: `git merge [options] <to_merge>` incorporate all the commits of `o_merge` onto the current branch.
    Some info also on [`GitHub`](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-request-merges).

    * If the history of the current and to-be-merged branch split, then an additional, automatically-generated commit is added (it is usually called “Merge branch \[...\]”).
        To avoid that, you can try to rebase `branch_to_merge` over the final brunch, and possibly use the option `--ff-only`.

    * It `branch_to_merge` has more than one commits, use `--squash` to merge all its commits without, however, committing the changes into the current branch.

* Rebasing: see [here](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)

* Stashing: sometimes modifications are not yet ready for a commit but you have to go checkout another branch and `git` won’t let you because of the modifications.
    That’s where stashing comes in: it’s a heap, a space where one can put modifications without them being in the official history.
    The state will be restored to `HEAD` (possibly the staged changes remain).
    Of course, one can recover them afterwards.

    * Stash modifications: `git stash`

        * Stashes are just like commit, hence one can give a message, use `-m 'Message'`

        * By default, it stashes all the modifications on any files in the `git` view.
            One can select a specific file `git stash -- file.txt`

    * Recover a stash: `git stash pop`

        * It actually performs to actions: apply the stash and delete it from the heap

        * By default, it takes the stash on the top of the heap, the last sent in, however one can select a specific one `git stash pop stash@{n}`

    * Delete a stash without applying it: `git stash drop`

        * See above to choose a specific stash

        * Abort a popping: sometimes the stash is not what you remember, in that case abort wit `git reset --merge`

* List files followed by `git`: `git ls-tree <SHA1>`.
    Advised options:

    * `--full-tree`: start from the root of the repository

    * `-r`: recursive

    * `--name-only`

* `git revert SHA1`: cancel the modifications done by commit `SHA1`.
    More info on the [man page](https://git-scm.com/docs/git-revert) and [this answer](https://stackoverflow.com/a/4114122).

* Add a file but then ignore it.
    This is quite a common situation: in a multi-developer project, there is a base configuration file and each dev customize it as they wish.
    One would like to keep the file into the repo, and also not to follow it.
    The solution is explained [here](https://stackoverflow.com/questions/3319479/can-i-git-commit-a-file-and-ignore-its-content-changes): add it then change the index

    ``` bash
    git update-index --assume-unchanged <file>
    ```

    To undo:

    ``` bash
    git update-index --no-assume-unchanged <file>
    ```

* `git` and `chmod` / file permissions: one can change the permissions of a file followed by `git` with, for instance:

    ``` bash
    git update-index --chmod=+x <file>
    ```

* `git log`: show the commit logs.
    [Manual](https://git-scm.com/docs/git-log)

    * `-<n>`, `-n <n>`: limit the number of commits to output

    * `--since=<date>`, `--after=<date>`: show commits more recent than `date`

    * `--until=<date>`, `--before=<date>`: show commits older than `date`

    * `-L <start>,<end>:<file>`: show commits which modified the zone of `file` delimited by the line numbers `start` and `end`

    * `-L:<function>:<file>`: show commits which modified function `function` of `file`

    * `--name-only`: show only files modified by commit

    * `-- <path>|<path/to/filename>`: show commits which modified the files in `path` (resp. the file `path/to/filename`).
        To be put after all other options;

    * `--pretty[=<format>]`, `--format=<format>`: customize the format of your output.
        You may want to choose predefined styles, then `format` can be chosen in `oneline`, `short`, `medium`, `full`, `fuller`, ...

* [`git` hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks): hooks are scripts that are automatically triggered before/after certain events (e.g., commit, checkout, push)

    * Some examples are already available in each repository.
        Have a look at directory `.git/hooks`, you will find a bunch of script with extension `.sample`.
        One can write their own script in bash, python, everything one wants.
        To enable one hook, just remove the `.sample` extension (e.g., `pre-commit`) and make it executable.

    * [An example](https://verdantfox.com/blog/how-to-use-git-pre-commit-hooks-the-hard-way-and-the-easy-way) for pre-commit hooks.
        Also, check out the [`pre-commit` framework](https://github.com/pre-commit/pre-commit-hooks).

* Commit cherry-picking ([manual](https://git-scm.com/docs/git-cherry-pick)): apply a specific commit from another branch

    ``` bash
    git cherry-picking <commit>
    ```

    * Example: apply to the current branch the third-to-last commit of branch `branch_name`:

      ``` bash
      git cherry-picking <branch_name>~4
      ```

* Show config:

    * Have a look at the global or local config file: `~/.gitconfig` or `repository/root/.git/config`

    * List everything: `git config [--global] --list`

    * Specific key: `git config [--global] --get <key_name>`

    * Search: `git config [--global] --get-regexp <pattern>`

* Aliases: as for bash, one can create custom aliases to shortcut some common commands.
    In order to to that simply use

    ``` bash
    git config [options] alias.<shortcut> '<cmd>'
    ```

    for instance

    ``` bash
    git config [--global] alias.pr 'pull ---rebase'
    ```

* Proxy: some info are given [here](https://gist.github.com/evantoli/f8c23a37eb3558ab8765).
    Try to simply run (from wherever)

    ``` bash
    git config --global http.proxy <server>:<port>
    ```

* List of files modified by a commit: from this [SO’s answer](https://stackoverflow.com/a/424142/12152457) (see also comments)

    ``` bash
    git diff-tree --no-commit-id --name-only -r <sha> # For scripts
    # try also --name-status: it gives info if modified, added, deleted,
    # mode changes,...
    # or...
    git show --pretty="" --name-only <sha>
    ```

* List all authors / developers in a project: see [here](https://stackoverflow.com/questions/9597410/list-all-developers-on-a-project-in-git) `git shortlog -sne`

* Ignore files from the syncing:

    * Add them to `.gitignore`.
        Since `.gitignore` itself is synchronized, the exclusion is global and will stay in the tree, meaning that any new clone of the repository will see it; one can also add `.gitignore` to itself;

    * Add them to `.git/info/exclude`.
        This is local and impacts only the local directory and clone of the repository.

* `git` **cannot** track empty directories.
    Hence, one should include a dummy file and add it to the tree.
    Some people use `.gitkeep` as naming convention for this dummy file.

* `git bisect`: help to find the commit causing the bug by a bisection procedure

    * `start`: initialize the procedure.

    * `bad [commit]`: tag commit as bad (default is current).

    * `good [commit]`: tag commit as good (default is current).

    * `reset`: once you have find the buggy commit, quit the procedure and go back to were you were at the beginning.

* `git grep` ([Manual](https://git-scm.com/docs/git-grep)): it basically works as `grep` (see <a href="#ssec:grep" data-reference-type="autoref" data-reference="ssec:grep">[ssec:grep]</a>) but on tracked files only: `git grep 'time_t' -- '*.[ch]'`.
    Some bonus options:

    * Notice that `--` marks the end of the options.

    * `--and`, `--or`, `--not`. Option `-e` should be used.

* `git blame` ([Manual](https://git-scm.com/docs/git-blame)): Show what revision and author last modified each line of a file.
    **ATTENTION:** `blame` returns info line by line; if you are just interested to know the last commit to date which modified a certain file, then use `git log -- file.txt`

    * “`-L <start>,<end>`” or “`-L :<foo>`”: Annotate only the line range given by `start` and `end` or by the function name regex `foo`

* Submodules: [here](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

    * Typically, an useful command in `git submodules update [--init]`

    * The status of the submodules is shown when running `git status`, to avoid that use option `--ignore-submodules=all`

* Sometimes the `.git` directory (where all the `git` magic happens) is larger than the projects itself: imaging having to store all the commits, changes,...
    [Here](https://stackoverflow.com/questions/5277467/how-can-i-clean-my-git-folder-cleaned-up-my-project-directory-but-git-is-sti) you find how to do a little house-keeping.
    `git gc` might be an option, as well.

* [`git filter-branch`](https://git-scm.com/docs/git-filter-branch): modify the tree according to filters.
    This command is very powerful but it rewrites the history, so, before doing it, be sure to read the link in the dedicated item below.

* About [rewriting `git` history](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History).
    See GitHub help about [removing sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).
    WARNING: it is highly advised not to rewrite the history of a published repository, since collaborators that already had the sources, will certainly have issues since their history does not correspond anymore.
    Hence, do not use it lightly and only on not-yet published repositories / branches.

## GitLab API

Users can manage and control a GitLab project via an API.
This includes uploading files, creating commits / tags / release / branches, trigger pipeline,...

* To access the API an authentication method should be used: either Oauth2 or simply an access token with API rights.
    The commands given below will use this latter method.
    To create a token, go to project `Preferences`, then `Access Tokens`

* The (numeric) ID of the project is necessary, actually, more generally all the URL of the project.
    It is different from the name of the project.
    It can be found in the examples `Preferences > CI/CD > General pipelines > Pipeline triggers`.
    Keep the URL until the numeric ID.

* The complete guide is [here](https://docs.gitlab.com/ee/api/), but, beware it is huge!

* Typically, a request will take the form of a call to the project API via `curl`, just open a terminal and launch

    ``` bash
    curl --header "PRIVATE-TOKEN: "<your_token>" \
         --request POST \
         --something \
         "https://example.gitlab.com/api/v4/projects/<ID>/<something>"
    ```

    where one has to use an access token and the numeric ID recovered in previous points.
    In what follows, we give what should replace the “`something`” above.

* [Upload a file](https://docs.gitlab.com/ee/api/projects.html#upload-a-file) (it can be later used in a release):

    ``` bash
    curl [...] --form "file=@relative/path/to/file.txt \
          "https://example.gitlab.com/api/v4/projects/<ID>/uploads"
    ```

    If the uploaded succeeded, the path to the online resource is returned / print to screen.
