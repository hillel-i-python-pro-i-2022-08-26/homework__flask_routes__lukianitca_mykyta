# Training Flask Project

![example](https://github.com/hillel-i-python-pro-i-2022-08-26/homework__flask_routes__lukianitca_mykyta/actions/workflows/code-check.yml/badge.svg)
***


## Run configuration

`make init-dev`\
`make homework-i-run`

## Available paths

### Mini-wiki paths:
* `/`
* `/requirements`
* `/generate-users` or `/generate_users?users_num=<int>`
* `/space`
* `/mean`

### Contacts book paths
* `/read-all`
* `/read/<int>`
* `/add-new-contact?contact_name=<str>&phone_number=<phone_number>`
* `/update-contact?user_id=<int>&contact_name=var&phone_number=var`
* `/delete-contact/<int>`