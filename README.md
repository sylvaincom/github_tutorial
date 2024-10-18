# A basic introduction to GitHub and GitHub actions by using GitHub Desktop

> 🙏 Forked from https://github.com/mathurinm/github-assignment, a project started by Mathurin Massias, Thomas Moreau, and Alexandre Gramfort.

## ⚙️ Prerequisites

- Download [Visual Studio Code](https://code.visualstudio.com/download).
- Set up your GitHub account.
  - Create a [GitHub](https://github.com/login) account.
    - 🚨 Strong recommendation: use a personal email to create your GitHub account and not the one from your company.
      - 💡 Your company will add your GitHub handle to their organization. The day you leave that company, you will be excluded from that organization but still keep your other private GitHub repositories on your account.
    - 💡 Choose your GitHub handle wisely, try to keep it professional.
  - Do the following: [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account). 💡 Basically, this allows you to authenticate with your GitHub account when pushing your code.
    - 🚨 With SSH, you have a private key and a public key. *Never* share your private key. Do not push any keys on a GitHub repository.
- Download [GitHub Desktop](https://desktop.github.com/download/) and sign in (with your GitHub account).

## 👨‍💻 Doing a basic pull request (PR) by using GitHub Desktop

####  Fork and clone this GitHub repository:
- From this GitHub repository (on the web navigator), fork the repository by clicking on the `Fork` button on the upper right corner, then `Create a new fork`.
- Clone the repository (of your fork):
  - From the web navigator, click on `Code` then `Open with GitHub Desktop`. This will automatically open GitHub Desktop.
  - Once on GitHub Desktop, click on `Clone`. This will clone the GitHub repository which corresponds to your fork.
  - When asked _How are you planning to use this fork?_, select _To contribute to the parent project_.
- Create a branch called `<student_branch>` (for example called it `john_d` if your name is "John Doe") and switch to this branch (it should be done for you by default, check `Current branch`).
- Click on `Publish branch`.

#### Do your modifications:
- Click on `Open in Visual Studio Code` to open the code, corresponding to this branch of your forked repository, on VS Code. 💡 Visual Studio Code must be selected as your *external editor* on GitHub Desktop.
  - On VS Code, on the bottom left, check that you are in the correct branch called `<student_branch>` (it should be done for you by default).
  - Select the `students.txt` file.
  - Modify this file by adding a ` -> done` at the end of the row with your name.
  - ⚠️ Do not forget to save the file after your modification!

#### Publish your modifications and send a pull request (PR):
- Go back to GitHub Desktop.
  - Select the changed file called `students.txt` (it should be done for you by default).
  - Add a commit message (by default it should be `Update students.txt`, which is fine). 💡 A commit message is for documentation purposes.
  - Click on `Commit to <student_branch>` to commit your changes on your branch.
  - Click on `Pull origin`.
    - 💡 If GitHub says that there is a conflict (because you modified lines that were modified by another student at the same time), solve them.
  - Click on `Push origin`.
  - Click on `Preview Pull Request`.
  - Click on `Create pull request`. This will automatically open a web navigator. 💡 You can see that you are in `sylvaincom/github_tutorial` so you are trying to apply changes on the original GitHub repository, and not only yours.
- On the automatically opened web navigator:
  - Click on `Create pull request`.
  - Now, the owner of the GitHub repository (here, your teacher with the `sylvaincom` GitHub handle) will have to approve your pull request.
    - 💡 For information, if your PR looks good, the way a collaborator of the repository (owner, maintainer, etc) would do it is by clicking on your PR on the web navigator then clicking on `Merge pull request` then `Confirm merge`. This collaborator undergoes a [PR review](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews) to approve (or not) your changes.
    - Do not hesitate to let your teacher know that you created a PR so that he can manually merge it.
  - Once your pull request has been merged: you will see `Pull request succesfully merged and close`. Click on `Delete branch`. Indeed, you no longer need this branch.
    - 💡 You should not be able to delete a branch if this branch is currently opened.
      - Close the repository from VS Code.
      - On GitHub Desktop, switch to the `main` branch.
    - 💡 After your PR has been merged, you can also delete your fork, but do *not* delete your fork yet as we will use it in the second part of this lab.
    - 💡 You can also delete a branch from GitHub Desktop. Right click on your branch `<student_branch>`, then click on `Delete`, then confirm with `Delete`. Same for your fork.
  - You can check that your modifications have been applied by looking at the original GitHub repository on the web navigator, on the `main` branch, and clicking on `students.txt`, thus at https://github.com/sylvaincom/github_tutorial/blob/main/students.txt.

### 💡 Some notes

- On the web navigator, on the page corresponding to your GitHub PR, you might see: `This branch is out-of-date with the base branch. Merge the latest changes from main into this branch.`. This means that while you were doing some changes in your branch, some changes from other users have been merged to the main branch, so you must retrieve these changes from the main branch and apply them to your branch.
  - On GitHub Desktop, when you are on your branch, click on the top menu on `Branch` then `Update from main` (that is not the same as `Fetch origin`). Then, click on `Push origin`.
  - On the web navigator, on your GitHub PR, you will then see the following commit comment: `Merge branch 'main' into <student_branch>`.

## 🚀 Doing an advanced PR with GitHub Actions (by using GitHub Desktop)

- On GitHub Desktop:
  - Create a branch called `<student_assignment_branch>` (for example call it `john_d_assignment` if your name is John Doe). Switch to this branch.
  - Open in VS Code.
  - Publish this branch (but do *not* create a pull request yet).
- On VS Code:
  - Open `numpy_question.py`.
  - Read the instructions at the beginning of `numpy_question.py`.
  - Modify `numpy_question.py` according to the instructions.
  - ⚠️ Do *not* modify `test_numpy_question.py`. 💡 More generally, do *not* modify Python files that start with `test_`: as their name suggests, they perform the tests (checks) on your submitted code.
- Create a pull request.
  - 💡 Instead of creating a (normal) PR, you can create a draft PR and convert it to ready for review only once you have finished your changes.
- See if all tests have passed (✅).
  - If not, if a check has failed (❌), keep pushing to your branch (*the same one*) until the continuous integration (CI) system is green (✅).
  - ⚠️ Do *not* open a new pull request every time you push.
- When `All tests have passed` (✅), you have finished this lab!
  - 💡 The teacher will *not* merge your PR, or all students would have your correct answer.

## 👨‍🏫 Some key take-aways

- always know where you are
  - which virtual environment
  - which directory
  - which GitHub repository (the original one or your fork)
  - in which branch you are

## 📚 About `git`

By using GitHub Desktop, you did not see all the `git` commands that you would have to be run from your shell.

Basically, imagine that there is a specific `git` command for all the clicks you do on GitHub Desktop (so it is quite difficult to teach them in a short lecture).

It is recommended to learn `git` from the command line on your own. Here are some resources:
- [Mathurin Massias' lecture notes](https://github.com/mathurinm/github-assignment?tab=readme-ov-file#general-information). Also see [Mathurin Massias' lab](https://github.com/mathurinm/github-assignment?tab=readme-ov-file#i-the-assignment) which is the equivalent of this lab you did using GitHub Desktop but with `git` commands. Notice how more complicated it looks...
- [Lino Galiana's lecture](https://pythonds.linogaliana.fr/content/git/): in French
- [Software Carpentry's lecture](https://swcarpentry.github.io/git-novice/)
- [Git documentation](documentation)
- http://try.github.io

More on GitHub Desktop:
- [GitHub Desktop documentation](https://docs.github.com/en/desktop)