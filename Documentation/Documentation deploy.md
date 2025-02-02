# Deployment documentation of Quasar Framework

This file contains the documentation of the deployment process of Quasar Framework.

## Dependencies

The deployment must be performed on a server, which run a GitHub Action workflow. For do that the following dependencies must be installed on the server:

- pip3: `yum install -y python3-pip`
- Python 3.8 or higher: `yum install -y python3`
- textlive: `yum install texlive-*`
- Github Action CLI: go to Setting section of your repository, then click on Runners and add the runner, then execute all the command shown on the server.

## Workflow

The workflow has the following steps:

1. Define version name: in this step the action define the version name for the deployment. There are two cases:
   - Release creation: the version name is the name of the release.
   - New commit on master: the version name is `latest`.
2. Install dependencies: the action install the dependencies of the project.
3. Create the folder for the deployment
4. Build HTML documentation: the action build the documentation in HTML format using sphinx command.
5. Build PDF and ePUB files: the action build the documentation in PDF and ePUB format using sphinx commands.
6. Update the server: the action update the NGINX server with the new files.

## New release creation

When a new release is created, a GitHub Action workflow is executed, this action create the new folder for the content of this release, but to show this new version on the website must update also the [version.json](./source/_static/versions.json). This file contains the list of all the versions to show on the website. Also can mark specific versions with warnings of rename with a new label. The structure of this file is the following:

```json
{ 
  // The list of versions to show on the website, is like a whitelist.
  "versions": [ "latest", "1.8.1" ],
  
  // This section contains the labels to rename the versions.
  // If the version is not in this list, the label will be the same defined on "versions" list below
  "labels": {
    "latest": "Latest"
  },

  // This section contains the warnings to show on the website.
  "warnings": {
    // This list can contains one o more of the following: "outdated", "unreleased" and "prereleased".
    "1.8.1": ["outdated"]
  }
}
```

## Troubleshooting

During the execution of the GitHub action there may occur problems in which its execution is interrupted, this may be due to a problem with the action or during the execution of one of the action steps.


- Problems during an Action update: if the action does not attend any more executions, it may stop during the runner update and show no progress. In this situation you have to delete the action folder (~/action-runner) and reinstall the GitHub Action as described in "Dependencies on server".
- Problems during the execution of an action step: the action may have started correctly but one of its steps may not finish successfully. In this case, the error caused in the step must be analyzed in order to make the pertinent changes, it may be due to permissions or directory changes.
