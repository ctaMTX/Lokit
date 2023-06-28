class Repository:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.commits = []
        self.branches = []

    def create_commit(self, message, author):
        commit = Commit(message, author)
        self.commits.append(commit)
        return commit

    def create_branch(self, name):
        branch = Branch(name)
        self.branches.append(branch)
        return branch

    def get_commit_history(self):
        for commit in self.commits:
            print(f"{commit.author}: {commit.message}")

    def get_branches(self):
        for branch in self.branches:
            print(branch.name)


class Commit:
    def __init__(self, message, author):
        self.message = message
        self.author = author


class Branch:
    def __init__(self, name):
        self.name = name


class User:
    def __init__(self, name):
        self.name = name
        self.repositories = []

    def create_repository(self, name):
        repository = Repository(name, self)
        self.repositories.append(repository)
        return repository
