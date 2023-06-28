from lokit import Repository, User

# Get user input for name
user_name = input("Enter your name: ")
pass_word = input("Enter your password: ")
repo_name = input("Enter your desired repo name: ")

# Create User instance
user1 = User(user_name)

# Usage example
repository1 = user1.create_repository(repo_name)
branch1 = repository1.create_branch("main")
commit1 = repository1.create_commit("Initial commit", user_name)
commit2 = repository1.create_commit("Add feature X", user_name)

print(f"Repository: {repository1.owner.name}/{repository1.name}")
print("Commits:")
repository1.get_commit_history()
print("Branches:")
repository1.get_branches()
