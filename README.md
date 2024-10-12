# GitHub lab: A basic introduction to GitHub and GitHub actions by using GitHub Desktop

> Forked from https://github.com/mathurinm/github-assignment, a project started by Mathurin Massias, Thomas Moreau, and Alexandre Gramfort.

## Prerequisite

- Download [Visual Studio Code](https://code.visualstudio.com/download).
- Set up your GitHub account.
  - Create a [GitHub](https://github.com/login) account.
  - Do the following: [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account). (Basically, this allows you to authenticate with your GitHub account when pushing your code.)
- Download [GitHub Desktop](https://desktop.github.com/download/) and sign in (with your GitHub account).

## Doing a basic pull request (PR) by using GitHub Desktop

#### Fork and clone this GitHub repository:
- From this GitHub repository (on the web navigator), fork the repository by clicking on the `Fork` button on the upper right corner, then `Create a new fork`.
- Clone the repository (of your fork):
  - From the web navigator, click on `Code` then `Open with GitHub Desktop`. This will automatically open GitHub Desktop.
  - On GitHub Desktop, click on `Clone`. This will automatically open the GitHub repository which corresponds to your fork.
  - When asked _How are you planning to use this fork?_, select _To contribute to the parent project_.
- Create a branch called `student_name` and switch to this branch (it should be done by default, see `Current branch`).
- Click on `Publish branch`.

#### Do your modifications:
- Click on `Open in Visual Studio Code` to open the code in this GitHub repository on this branch of your forked repository on VS Code. (Note that Visual Studio Code must be select as your *external editor* on GitHub Desktop.)
  - In VS Code, on the bottom left, check that you are the correct branch `student_name` (it should be done by default).
  - Select the file `students.txt`.
  - Modify this file by adding a ` -> done` at the end of the row with your name. Do not forget to save the file after your modification!

#### Publish your modifications and send a pull request (PR):
- Go back to GitHub Desktop.
  - Select the changed file called `students.txt` (it should be done by default).
  - Add a commit message (by default it should be `Update students.txt`, which is fine). Note that the commit message is for documentation purposes.
  - Click on `Commit to student_name` to commit your changes on your branch.
  - Click on `Pull origin`. If GitHub says that there is a conflict (because you modified lines that were modified by another student at the same time), solve them.
  - Click on `Push origin`.
  - Click on `Preview Pull Request`.
  - Click on `Create pull request`. This will automatically open a web navigator. You can see that you are in `sylvaincom/github_lab` so you are trying to apply changes on the original GitHub repository, and not only yours.
- On the automatically opened web navigator:
  - Click on `Create pull request`.
  - Now, the owner of the GitHub repository (here, your teacher Sylvain) will have to accept your pull request by clicking on it then clicking on `Merge pull request` then `Confirm merge`. (Do not hesitate to let your teacher know that you created a PR so that he can manually merge it.)
  - Once your pull request has been merged: you will see `Pull request succesfully merged and close`. Click on `Delete branch`. Indeed, you no longer need this branch.
    - (You can also delete a branch from GitHub Desktop. Right click on your branch `student_name`, then click on `Delete`, then confirm with `Delete`.)
  - (On GitHub Desktop, switch to the `main` branch, then click on `Fetch origin`.)
  - You can check that your modifications have been applied by looking at the GitHub repository on the web navigator, on the `main` branch, and clicking on `students.txt`, thus at https://github.com/sylvaincom/github_lab/blob/main/students.txt.

## Doing an advanced PR with GitHub Actions (by using GitHub Desktop)

- From GitHub Desktop, create a branch called `student_name_assignment` (for example `paul_assignment`). Switch to this branch. Open in VS Code.
- From VS Code, open `numpy_question.py`.
  - Read the instructions at the beginning of `numpy_question.py`.
  - Modify `numpy_question.py` according to the instructions.
  - Do *not* modify `test_numpy_question` (more generally, do *not* modify Python files that start with `test_`).
- Create a pull request.
- See if all tests have passed. If not, keep pushing to your branch (the same one) until the continuous integration (CI) system is green. Do *not* open a new pull request every time you push.
- When `All tests have passed` (green), you are done. (The teacher will *not* merge your PR, or all students would have your correct answer.)

## `git`

By using GitHub Desktop, you did not see all the `git` commands that you would have to be run from your shell.

Basically, imagine that there is a specific `git` command for all the clicks you do on GitHub Desktop (so it is quite difficult to teach them in a short lecture).

It is recommended to learn `git` from the command line on your own. Here are some resources:
- [Mathurin Massias' lecture notes](https://github.com/mathurinm/github-assignment?tab=readme-ov-file#general-information). Also see [Mathurin Massias' lab](https://github.com/mathurinm/github-assignment?tab=readme-ov-file#i-the-assignment) which is the equivalent of this lab you did using GitHub Desktop but with `git` commands. Notice how more complicated it looks...
- [Lino Galiana's lecture](https://pythonds.linogaliana.fr/content/git/) (in French)
- [Software Carpentry's lecture](https://swcarpentry.github.io/git-novice/)
- [Git documentation](documentation)
- http://try.github.io