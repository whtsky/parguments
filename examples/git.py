#!/usr/bin/env python
from parguments import Parguments

doc = """
usage: git [--version] [--exec-path=<path>] [--html-path]
           [-p|--paginate|--no-pager] [--no-replace-objects]
           [--bare] [--git-dir=<path>] [--work-tree=<path>]
           [-c name=value]
           <command> [<args>...]
       git [--help]

The most commonly used git commands are:
   add        Add file contents to the index
   branch     List, create, or delete branches
   checkout   Checkout a branch or paths to the working tree
   clone      Clone a repository into a new directory
   commit     Record changes to the repository
   push       Update remote refs along with associated objects
   remote     Manage set of tracked repositories

See 'git help <command>' for more information on a specific command.
"""


git = Parguments(doc, version='git version 1.7.4.4',
    options_first=True)


@git.command
def add(args):
    """
usage: git add [options] [--] [<filepattern>...]

-h, --help
-n, --dry-run        dry run
-v, --verbose        be verbose

-i, --interactive    interactive picking
-p, --patch          select hunks interactively
-e, --edit           edit current diff and apply
-f, --force          allow adding otherwise ignored files
-u, --update         update tracked files
-N, --intent-to-add  record only the fact that the path will be added later
-A, --all            add all, noticing removal of tracked files
--refresh            don't add, only refresh the index
--ignore-errors      just skip files which cannot be added because of errors
--ignore-missing     check if - even missing - files are ignored in dry run
    """
    print(args)


@git.command
def branch(args):
    """
usage: git branch [options] [-r | -a] [--merged=<commit> | --no-merged=<commit>]
       git branch [options] [-l] [-f] <branchname> [<start-point>]
       git branch [options] [-r] (-d | -D) <branchname>
       git branch [options] (-m | -M) [<oldbranch>] <newbranch>

Generic options
    -h, --help
    -v, --verbose         show hash and subject, give twice for upstream branch
    -t, --track           set up tracking mode (see git-pull(1))
    --set-upstream        change upstream info
    --color=<when>        use colored output
    -r                    act on remote-tracking branches
    --contains=<commit>   print only branches that contain the commit
    --abbrev=<n>          use <n> digits to display SHA-1s

Specific git-branch actions:
    -a                    list both remote-tracking and local branches
    -d                    delete fully merged branch
    -D                    delete branch (even if not merged)
    -m                    move/rename a branch and its reflog
    -M                    move/rename a branch, even if target exists
    -l                    create the branch's reflog
    -f, --force           force creation (when already exists)
    --no-merged=<commit>  print only not merged branches
    --merged=<commit>     print only merged branches
    """
    print(args)


def clone(args):
    """usage: git clone [options] [--] <repo> [<dir>]

        -v, --verbose         be more verbose
        -q, --quiet           be more quiet
        --progress            force progress reporting
        -n, --no-checkout     don't create a checkout
        --bare                create a bare repository
        --mirror              create a mirror repository (implies bare)
        -l, --local           to clone from a local repository
        --no-hardlinks        don't use local hardlinks, always copy
        -s, --shared          setup as shared repository
        --recursive           initialize submodules in the clone
        --recurse-submodules  initialize submodules in the clone
        --template <template-directory>
                              directory from which templates will be used
        --reference <repo>    reference repository
        -o, --origin <branch>
                              use <branch> instead of 'origin' to track upstream
        -b, --branch <branch>
                              checkout <branch> instead of the remote's HEAD
        -u, --upload-pack <path>
                              path to git-upload-pack on the remote
        --depth <depth>       create a shallow clone of that depth

    """
    print(args)

git.add_command(clone)


def print_args(args):
    print(args)


git.add_command(name='checkout', func=print_args, doc="""
usage: git checkout [options] <branch>
       git checkout [options] <branch> -- <file>...

    -q, --quiet           suppress progress reporting
    -b <branch>           create and checkout a new branch
    -B <branch>           create/reset and checkout a branch
    -l                    create reflog for new branch
    -t, --track           set upstream info for new branch
    --orphan <new branch>
                          new unparented branch
    -2, --ours            checkout our version for unmerged files
    -3, --theirs          checkout their version for unmerged files
    -f, --force           force checkout (throw away local modifications)
    -m, --merge           perform a 3-way merge with the new branch
    --conflict <style>    conflict style (merge or diff3)
    -p, --patch           select hunks interactively

""")

git.add_command(name='commit', func=print_args,
    doc="""usage: git commit [options] [--] [<filepattern>...]

    -h, --help
    -q, --quiet           suppress summary after successful commit
    -v, --verbose         show diff in commit message template

Commit message options
    -F, --file <file>     read message from file
    --author <author>     override author for commit
    --date <date>         override date for commit
    -m, --message <message>
                          commit message
    -c, --reedit-message <commit>
                          reuse and edit message from specified commit
    -C, --reuse-message <commit>
                          reuse message from specified commit
    --fixup <commit>      use autosquash formatted message to fixup specified commit
    --squash <commit>     use autosquash formatted message to squash specified commit
    --reset-author        the commit is authored by me now
                          (used with -C-c/--amend)
    -s, --signoff         add Signed-off-by:
    -t, --template <file>
                          use specified template file
    -e, --edit            force edit of commit
    --cleanup <default>   how to strip spaces and #comments from message
    --status              include status in commit message template

Commit contents options
    -a, --all             commit all changed files
    -i, --include         add specified files to index for commit
    --interactive         interactively add files
    -o, --only            commit only specified files
    -n, --no-verify       bypass pre-commit hook
    --dry-run             show what would be committed
    --short               show status concisely
    --branch              show branch information
    --porcelain           machine-readable output
    -z, --null            terminate entries with NUL
    --amend               amend previous commit
    --no-post-rewrite     bypass post-rewrite hook
    -u, --untracked-files=<mode>
                          show untracked files, optional modes: all, normal, no.
                          [default: all]

""")

git.add_command(name='push', func=print_args,
    doc="""usage: git push [options] [<repository> [<refspec>...]]

    -h, --help
    -v, --verbose         be more verbose
    -q, --quiet           be more quiet
    --repo <repository>   repository
    --all                 push all refs
    --mirror              mirror all refs
    --delete              delete refs
    --tags                push tags (can't be used with --all or --mirror)
    -n, --dry-run         dry run
    --porcelain           machine-readable output
    -f, --force           force updates
    --thin                use thin pack
    --receive-pack <receive-pack>
                          receive pack program
    --exec <receive-pack>
                          receive pack program
    -u, --set-upstream    set upstream for git pull/status
    --progress            force progress reporting

""")

git.add_command(name='remote', func=print_args,
    doc="""
usage: git remote [-v | --verbose]
       git remote add [-t <branch>] [-m <master>] [-f] [--mirror] <name> <url>
       git remote rename <old> <new>
       git remote rm <name>
       git remote set-head <name> (-a | -d | <branch>)
       git remote [-v | --verbose] show [-n] <name>
       git remote prune [-n | --dry-run] <name>
       git remote [-v | --verbose] update [-p | --prune] [(<group> | <remote>)...]
       git remote set-branches <name> [--add] <branch>...
       git remote set-url <name> <newurl> [<oldurl>]
       git remote set-url --add <name> <newurl>
       git remote set-url --delete <name> <url>

    -v, --verbose         be verbose; must be placed before a subcommand
""")


def fallback(cmd, args):
    print("%s is not a git.py command. See 'git help'." % cmd)

if __name__ == '__main__':
    git.run('<command>', default_command='help', fallback=fallback)
