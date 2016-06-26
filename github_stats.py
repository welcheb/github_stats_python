#!/usr/bin/env python

import os
import requests
import json
from time import gmtime, strftime

# gtihub credentials from secret variables assigned as properties of this gitlab project
user = os.environ['GITHUB_USER']
token = os.environ['GITHUB_API_TOKEN']

# github api url
api_url = 'https://api.github.com'

# rate limit information
r = requests.get(api_url+'/rate_limit', auth=(user, token))
rate_limit_data = json.loads(r.text)

rate_limit_data['_request_time_gmt'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())

# write rate_limit data to json file
with open('rate_limit.json', 'w') as outfile:
    json.dump(rate_limit_data, outfile, indent=4, sort_keys=True)

# ISMRM MR Hub information
ismrm_mr_hub_repos = ('mrirecon/bart','gadgetron/gadgetron','andyschwarzl/gpuNUFFT','ismrmrd/ismrmrd')

# data fields of interests
repo_data_fields_of_interest = ('forks_count','watchers_count','stargazers_count')

# represent as a dictionary
ismrm_mr_hub_data = {}
ismrm_mr_hub_data['_request_time_gmt'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())

# loop over list of repos
ismrm_mr_hub_data['repos'] = []
for repo in ismrm_mr_hub_repos:

    # api url for this repo
    repo_api_url = api_url + '/repos/' + repo

    # repo info is a dictionary
    repo_info = {}
    repo_info['_repo_api_url'] = repo_api_url

    # api request
    r = requests.get(repo_api_url, auth=(user, token))
    data_repo = json.loads(r.text)

    # keep info of interest
    for field_of_interest in repo_data_fields_of_interest:
        repo_info[field_of_interest] = data_repo[field_of_interest]

    # each entry in the repos list is a dictionary
    ismrm_mr_hub_data['repos'].append(repo_info)

# write ismrm_mr_hub data to json file
with open('ismrm_mr_hub.json', 'w') as outfile:
    json.dump(ismrm_mr_hub_data, outfile, indent=4, sort_keys=True)
