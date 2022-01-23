import git 


def gitDiff(branch1, branch2):
    format = '--name-only'
    commits = []
    g = git.Git('/path/to/git/repo')
    differ = g.diff('%s..%s' % (branch1, branch2), format).split("\n")
    for line in differ:
        if len(line):
            commits.append(line)

    #for commit in commits:
    #    print '*%s' % (commit)
    return commits