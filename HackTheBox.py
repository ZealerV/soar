"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'execute_program_1' block
    execute_program_1(container=container)

    return

def scan_network_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('scan_network_1() called')
    
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'scan_network_1' call

    parameters = []
    
    # build parameters list for 'scan_network_1' call
    parameters.append({
        'portlist': "",
        'script-args': "-A",
        'script': "",
        'ip_hostname': "10.10.10.161",
        'udp_scan': "",
    })

    phantom.act("scan network", parameters=parameters, assets=['nmap'], callback=prompt_1, name="scan_network_1", parent_action=action)

    return

def execute_program_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('execute_program_1() called')

    # collect data for 'execute_program_1' call

    parameters = []
    
    # build parameters list for 'execute_program_1' call
    parameters.append({
        'command': "sudo openvpn /home/user/sorsnce.ovpn &",
        'timeout': "",
        'ip_hostname': "phantom.sorsnce.com",
        'script_file': "",
    })

    phantom.act("execute program", parameters=parameters, assets=['phantom-ssh'], callback=scan_network_1, name="execute_program_1")

    return

def prompt_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('prompt_1() called')
    
    # set user and message variables for phantom.prompt call
    user = "admin"
    message = """TEST

{0}"""

    # parameter list for template variable replacement
    parameters = [
        "scan_network_1:action_result.data.*.tcp.*.state",
    ]

    #responses:
    response_types = [
        {
            "prompt": "",
            "options": {
                "type": "message",
            },
        },
    ]

    phantom.prompt2(container=container, user=user, message=message, respond_in_mins=30, name="prompt_1", parameters=parameters, response_types=response_types)

    return

def on_finish(container, summary):
    phantom.debug('on_finish() called')
    # This function is called after all actions are completed.
    # summary of all the action and/or all detals of actions 
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    return