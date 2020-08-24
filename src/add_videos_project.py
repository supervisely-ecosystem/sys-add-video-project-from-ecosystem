import os
import json
import supervisely_lib as sly

#context = json.loads(os.environ.get('CONTEXT', {}))
#state = json.loads(os.environ.get('STATE', {}))

team_id = 7#state["destination"]["teamId"]
workspace_id = 47#state["destination"]["workspaceId"]
name = "v_01" #state["name"]

github_token = os.environ.get('GITHUB_TOKEN', "")
github_url = "https://github.com/supervisely-ecosystem/video-project-example.git" #context["githubUrl"]

dest_dir = "/sly_task_data/repo"
sly.fs.clean_dir(dest_dir)
sly.git.download(github_url, dest_dir, github_token)

api = sly.Api.from_env()
project_name = sly.fs.get_file_name(github_url)
project_id, res_project_name = sly.upload_video_project(dest_dir, api, workspace_id, project_name, log_progress=True)
sly.logger.info("Project info: id={!r}, name={!r}".format(project_id, res_project_name))

# to show created project in tasks list (output column)
sly.logger.info('PROJECT_CREATED', extra={'event_type': sly.EventType.PROJECT_CREATED, 'project_id': project_id})