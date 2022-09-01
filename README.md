# Deadline - Batch Resubmit
## Description
This script resubmits Deadline Jobs in batch. It requires the job parameters and auxilliary files to be exported and stored, before resubmitting.
The deadline_submit_info script return the job info for a given job ID.

## How To
To resubmit jobs in batch, the job informations need to be exported from Deadline to the 'submission_param' folder.

![Capture](https://user-images.githubusercontent.com/72398192/187688056-1d9eb221-f8bd-4d0d-a3ff-58f8409dcf70.PNG)
![Capture2](https://user-images.githubusercontent.com/72398192/187688165-1975c0a1-be45-47ab-b506-e80aa273bce9.PNG)

Once the jobs information has been exported and saved, from a CLI pointing to the Deadline bin directory (ex: C:/ProgramFiles/Thinkbox/Deadline10/bin):

            python 'path/to/this/script.py'

Make sure the paths for the args.txt file and the submission_params folder in the script are correct for your config.

## Credits
- [MenhirFX](www.menhirfx.com)
