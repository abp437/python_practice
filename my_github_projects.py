# My Github Profile Repos
# https://api.github.com/users/abp437/repos

import requests

username = input("Enter your Github username to get the list of all your repos along with it's url: ")

resp = requests.get(f"https://api.github.com/users/{username}/repos")

if resp.status_code == 200:
  my_repos = resp.json()

  for repo in my_repos:
    print(f'{repo["name"]}\n=> {repo["html_url"]}\n')
else:
  print("Error in fetching your Repos")
