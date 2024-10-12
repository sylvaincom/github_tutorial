# GitHub lab: Working with git and GitHub

> Forked from https://github.com/mathurinm/github-assignment, a project started by Mathurin Massias, Thomas Moreau, and Alexandre Gramfort.

## Prerequisite

- Download [Visual Studio Code](https://code.visualstudio.com/download).
- Set up your GitHub account.
  - Create a [GitHub](https://github.com/login) account.
  - Do the following: [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account). (Basically, this allows you to authenticate with your GitHub account when pushing your code.)
- Download [GitHub Desktop](https://desktop.github.com/download/) and sign in (with your GitHub account).

## Doing a basic pull request (PR) using GitHub Desktop

#### Fork and clone this GitHub repository:
- From this GitHub repository (on the web navigator), fork the repository by clicking on the `Fork` button on the upper right corner, then `Create a new fork`.
- Clone the repository of your fork: click on `Code` then `Open with GitHub Desktop`,
  - When asked _How are you planning to use this Fork_, select _To contribute to the parent project_
- Create a branch called `student_name` and switch to this branch (it should be done by default, see `Current branch`).
- Click on `Publish branch`.

#### Do your modifications:
- Click on `Open in Visual Studio Code` to open the code in this GitHub repository on this branch of your forked repository on VS Code. (Note that Visual Studio Code must be select as your *external editor* on GitHub Desktop.)
  - (Check that you are the correct branch.)
  - Select the file `students.txt`.
  - Modify this file by adding an `X` at the end of the row with your name. Do not forget to save the file after your modification!

#### Publish your modifications and send a pull request (PR):
- Go back to GitHub Desktop.
  - Select the changed file called `students.txt` (it should be done by default).
  - Add a commit message (by default it should be `Update students.txt`, which is fine). Note that the commit message is for documentation purposes.
  - Click on `Commit to student_name` to commit your changes on your branch.
  - Click on `Pull origin`. If GitHub says that there is a conflict (because you modified lines that were modified by another student at the same time), solve them.
  - Click on `Push origin`.
  - Click on `Preview Pull Request`.
  - Click on `Create pull request`. This will automatically open a web navigator. You can see that you are in `sylvaincom/github_lab` so you are trying to apply changes on the original GitHub repository, and not only yours.
- On the automatically opened web navigator, click on `Create pull request`.
- Now, the owner of the GitHub repository (here, your teacher Sylvain) will have to accept your pull request by clicking on it then clicking on `Merge pull request` then `Confirm merge`. (Do not hesitate to let your teacher know that you created a PR so that he can manually merge it.)
- Once your pull request has been merged: you will see `Pull request succesfully merged and close`. Click on `Delete branch`.
  - You can also delete a branch from GitHub Desktop. Right click on your branch `student_name`, then click on `Delete`, then confirm with `Delete`. (Indeed, you no longer need this branch.)
- (On GitHub Desktop, switch to the `main` branch then click on `Fetch origin`.)
- You can check that your modifications have been applied by looking at the GitHub repository on the web navigator and clicking on `students.txt`!