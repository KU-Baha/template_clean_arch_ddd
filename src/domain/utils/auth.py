import json
import logging
import traceback
from gettext import gettext

import requests

from application.base.exception import BusinessException


def send_access_req(
    auth_service: str,
    project_name: str,
    service: str,
    username: str,
    password: str,
) -> bool:
    data = {
        'project': project_name,
        'component': service,
        'is_edit': False
    }

    try:
        response = requests.post(
            f"{auth_service}/auth.has_access",
            json=data,
            verify=False,
            auth=(
                username,
                password
            )
        )

        if response.status_code != 200:
            raise BusinessException(-100, gettext('Authorization server is not available'))

        resp_json = json.loads(response.text)

        if resp_json['result'] != 0:
            raise BusinessException(resp_json['result'], resp_json.get('message'))

        return resp_json.get('has_access')

    except Exception as e:
        if isinstance(e, BusinessException):
            raise e

        logging.info(traceback.format_exc())
        raise BusinessException(-100, gettext('Authorization server is not available'))
