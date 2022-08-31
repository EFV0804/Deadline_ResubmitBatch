import subprocess

# Get Job Info for a given Job Id
job_id=None
file = subprocess.check_output('./deadlinecommand.exe GetJob {job_id} true'.format(job_id=job_id))

print(file)