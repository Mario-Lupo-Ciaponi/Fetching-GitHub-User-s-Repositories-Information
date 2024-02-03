import requests


def fetch_user_repositories(username):
    """
      This function gets all the information about the user's repositories.
    """
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error!")
        return None


def display_repository_info(user_name, repositories):
    print(f"{user_name}'s repositories: \n")

    for repository in repositories:
        print(f"Repository's name: {repository["name"]}")
        print(f"Description: {repository["description"]}")
        print(f"Language used: {repository["language"]}")
        print(f"Stars received: {repository["stargazers_count"]}")
        print(f"Number of watchers: {repository["watchers"]}")
        print(f"Number of forks: {repository["forks"]}")
        print()


def main():
    github_username = input("Please, type the user's GitHub username: ")
    repositories = fetch_user_repositories(github_username)

    if repositories:
        display_repository_info(github_username, repositories)


if __name__ == "__main__":
    main()
