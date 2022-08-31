import glob
import os

submit_info_dir = 'U:/mesDocuments/dev/deadline_resubmit_batch/submission_params/'
args_file_path = "U:/mesDocuments/dev/deadline_resubmit_batch/args.txt"
auxiliary_ext = '*.hiplc'

job_plugin_info = glob.glob(submit_info_dir + '*.job')

print(job_plugin_info)
jobIds = []
for i in job_plugin_info:
    base = os.path.basename(i)
    id = base.split("_")[0]
    if id not in jobIds:
        jobIds.append(id)
        print(jobIds)


with open(args_file_path,'w+') as args:
    args.write("-SubmitMultipleJobs\n")

    for id in jobIds:
        args.write("-job\n")
        job_info_path = glob.glob('{}{}_jobInfo.job'.format(submit_info_dir, id))[0]
        plugin_info_path = glob.glob('{}{}_pluginInfo.job'.format(submit_info_dir,id))[0]
        aux_path = glob.glob('{}{}_auxiliaryinfo/{}'.format(submit_info_dir, id, auxiliary_ext))[0]
        args.write("{0}\n{1}\n{2}\n".format(job_info_path, plugin_info_path, aux_path))

os.system('deadlinecommand.exe {}'.format(args_file_path))